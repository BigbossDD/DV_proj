import pandas as pd

def extract_issue_ids(df):
    issues = {}

    # -------------------------------
    # 1. Negative values (numeric)
    # -------------------------------
    numeric_cols = df.select_dtypes(include=['number']).columns

    for col in numeric_cols:
        mask = df[col] < 0
        if mask.any():
            issues[f'negative_{col}'] = df.loc[mask, 'trip_id']

    # -------------------------------
    # 2. Outliers (IQR method)
    # -------------------------------
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        mask = (df[col] < lower) | (df[col] > upper)
        if mask.any():
            issues[f'outlier_{col}'] = df.loc[mask, 'trip_id']

    # -------------------------------
    # 3. Zero distance but fare > 0
    # -------------------------------
    mask = (df['trip_distance'] == 0) & (df['fare_amount'] > 0)
    issues['zero_distance_nonzero_fare'] = df.loc[mask, 'trip_id']

    # -------------------------------
    # 4. Distance > 0 but fare = 0
    # -------------------------------
    mask = (df['trip_distance'] > 0) & (df['fare_amount'] == 0)
    issues['nonzero_distance_zero_fare'] = df.loc[mask, 'trip_id']

    # -------------------------------
    # 5. Total amount mismatch
    # -------------------------------
    components = (
        df['fare_amount'].fillna(0) +
        df['extra'].fillna(0) +
        df['mta_tax'].fillna(0) +
        df['tip_amount'].fillna(0) +
        df['tolls_amount'].fillna(0) +
        df['improvement_surcharge'].fillna(0) +
        df['congestion_surcharge'].fillna(0) +
        df['Airport_fee'].fillna(0) +
        df['cbd_congestion_fee'].fillna(0)
    )

    mask = abs(df['total_amount'] - components) > 0.01
    issues['total_mismatch'] = df.loc[mask, 'trip_id']

    # -------------------------------
    # 6. Invalid payment_type
    # -------------------------------
    valid_payment = [0, 1, 2, 3, 4, 5, 6]
    mask = ~df['payment_type'].isin(valid_payment)
    issues['invalid_payment'] = df.loc[mask, 'trip_id']

    # -------------------------------
    # 7. Invalid RatecodeID
    # -------------------------------
    valid_rate = [1, 2, 3, 4, 5, 6, 99]
    mask = ~df['RatecodeID'].isin(valid_rate)
    issues['invalid_ratecode'] = df.loc[mask, 'trip_id']

    # -------------------------------
    # 8. Invalid store flag
    # -------------------------------
    mask = ~df['store_and_fwd_flag'].isin(['Y', 'N'])
    issues['invalid_store_flag'] = df.loc[mask, 'trip_id']

    # -------------------------------
    # 9. Same pickup & dropoff
    # -------------------------------
    mask = df['PULocationID'] == df['DOLocationID']
    issues['same_location'] = df.loc[mask, 'trip_id']

    # High distance same location
    mask = (df['PULocationID'] == df['DOLocationID']) & (df['trip_distance'] > 5)
    issues['same_location_high_distance'] = df.loc[mask, 'trip_id']

    # -------------------------------
    # 10. Temporal issues
    # -------------------------------
    # dropoff before pickup
    mask = df['tpep_dropoff_datetime'] < df['tpep_pickup_datetime']
    issues['invalid_time'] = df.loc[mask, 'trip_id']

    # extreme duration (> 24h)
    duration = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 3600
    mask = duration > 24
    issues['extreme_duration'] = df.loc[mask, 'trip_id']

    # -------------------------------
    # 11. CBD fee before Jan 5
    # -------------------------------
    mask = (
        (df['tpep_pickup_datetime'] < pd.Timestamp('2025-01-05')) &
        (df['cbd_congestion_fee'] > 0)
    )
    issues['cbd_before_jan5'] = df.loc[mask, 'trip_id']

    # -------------------------------
    # 12. Duplicates (excluding trip_id)
    # -------------------------------
    dup_mask = df.duplicated(subset=df.columns.drop('trip_id'), keep=False)
    issues['duplicates'] = df.loc[dup_mask, 'trip_id']

    return issues
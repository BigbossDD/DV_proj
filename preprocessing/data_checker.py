import pandas as pd
import numpy as np

def full_data_quality_audit(df, zone_lookup=None):

    results = {}

    # ===============================
    # 1. BASIC
    # ===============================
    results['shape'] = df.shape
    results['missing'] = df.isnull().sum()

    # ===============================
    # 2. NEGATIVE VALUES
    # ===============================
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    neg_report = {}
    for col in numeric_cols:
        neg_report[col] = int((df[col] < 0).sum())
    results['negative_values'] = neg_report

    # ===============================
    # 3. OUTLIERS (IQR)
    # ===============================
    outliers = {}
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outliers[col] = int(((df[col] < lower) | (df[col] > upper)).sum())
    results['outliers'] = outliers

    # ===============================
    # 4. TEMPORAL CONSISTENCY
    # ===============================
    results['invalid_time'] = len(
        df[df['tpep_dropoff_datetime'] < df['tpep_pickup_datetime']]
    )

    df['trip_duration_min'] = (
        (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime'])
        .dt.total_seconds() / 60
    )

    results['extreme_duration'] = len(df[df['trip_duration_min'] > 1440])

    # ===============================
    # 5. LOGICAL CHECKS
    # ===============================

    # fare vs distance
    results['fare_distance_mismatch'] = len(
        df[(df['trip_distance'] > 50) & (df['fare_amount'] < 20)]
    )

    # total vs components
    calc_total = (
        df['fare_amount'] + df['extra'] + df['mta_tax'] +
        df['tip_amount'] + df['tolls_amount'] +
        df['improvement_surcharge'] +
        df['congestion_surcharge'].fillna(0) +
        df['Airport_fee'].fillna(0)
    )

    results['total_mismatch'] = len(
        df[abs(df['total_amount'] - calc_total) > 2]
    )

    # ===============================
    # 6. ZERO ANOMALIES
    # ===============================
    results['zero_distance_nonzero_fare'] = len(
        df[(df['trip_distance'] == 0) & (df['fare_amount'] > 0)]
    )

    results['zero_fare_nonzero_distance'] = len(
        df[(df['fare_amount'] == 0) & (df['trip_distance'] > 0)]
    )

    # ===============================
    # 7. CATEGORY VALIDATION
    # ===============================
    results['invalid_payment'] = len(
        df[~df['payment_type'].isin([0,1,2,3,4,5,6])]
    )

    results['invalid_ratecode'] = len(
        df[~df['RatecodeID'].isin([1,2,3,4,5,6,99])]
    )

    results['invalid_store_flag'] = len(
        df[~df['store_and_fwd_flag'].isin(['Y','N'])]
    )

    # ===============================
    # 8. BUSINESS RULES
    # ===============================

    # tip rule
    results['tip_non_cc'] = len(
        df[(df['payment_type'] != 1) & (df['tip_amount'] > 0)]
    )

    # CBD rule
    results['cbd_before_jan5'] = len(
        df[
            (df['tpep_pickup_datetime'] < '2025-01-05') &
            (df['cbd_congestion_fee'] > 0)
        ]
    )

    # ===============================
    # 9. LOCATION CHECKS
    # ===============================
    results['same_location_high_distance'] = len(
        df[(df['PULocationID'] == df['DOLocationID']) &
           (df['trip_distance'] > 5)]
    )

    # ===============================
    # 10. DUPLICATES
    # ===============================
    cols = [c for c in df.columns if c != 'trip_id']
    results['duplicates'] = len(df) - len(df.drop_duplicates(subset=cols))

    print("\n=== FULL DATA QUALITY REPORT ===")
    for k, v in results.items():
        print(f"{k}: {v}")

    return results
import pandas as pd 
#from preprocessing.Data_Quality_Review.data_desc import data_desc
def read_data():
    # the path of data 
    path = '~/Downloads/Project_student.parquet'
    data = pd.read_parquet(path)
    ### print(data.head(3))
    # checking the data type checking if their is anything not numrical 


    for column in data.columns:
        pass
      ###  print(column , ' : ' , data[column].dtype)
    # after checking , their are data type , and string type we will keep that 
    #in mind for now 



    #data_desc(data)

    # print(data.duplicated().sum()) # no duplicats 


    # we added some useful columns to the data to make it easier for us to do some analysis on it

    data['month'] = data['tpep_pickup_datetime'].dt.month

    data['pickup_hour'] = pd.to_datetime(data['tpep_pickup_datetime']).dt.hour

    data['pickup_weekday'] = pd.to_datetime(data['tpep_pickup_datetime']).dt.day_name()


    # checking for duplicates & removing them :
    # cols = [c for c in data.columns if c != 'trip_id']
    # df_clean = data.drop_duplicates(subset=cols)

    # print(f"Rows before : {len(data)}")
    # print(f"Rows after  : {len(df_clean)}")
    # print(f"Duplicates removed : {len(data) - len(df_clean)}")
    # data = df_clean

    '''
    Rows before : 11200280
    Rows after  : 11198026
    Duplicates removed : 2254 
    '''
    # not much value of them as we have 11m row so they wont have that big of an effect 

    # near duplicates 
  

    # df = data.copy()

    # # -------------------------------
    # # 1. Create time-based features
    # # -------------------------------
    # df['pickup_time'] = pd.to_datetime(df['tpep_pickup_datetime'])
    # df['dropoff_time'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    # df['trip_duration_min'] = (df['dropoff_time'] - df['pickup_time']).dt.total_seconds() / 60

    # # -------------------------------
    # # 2. Define grouping keys
    # # (core idea: same trip pattern)
    # # -------------------------------
    # group_cols = [
    #     'PULocationID',
    #     'DOLocationID',
    #     'passenger_count',
    #     'payment_type'
    # ]

    # # -------------------------------
    # # 3. Sort for stable comparison
    # # -------------------------------
    # df = df.sort_values(by=['pickup_time'])

    # # -------------------------------
    # # 4. Detect near duplicates
    # # Logic:
    # # same route + same passenger + close time window
    # # -------------------------------
    # df['time_diff'] = df['pickup_time'].diff().dt.total_seconds().fillna(999999)

    # # condition for "possible near duplicate"
    # near_dup_condition = (
    #     (df['PULocationID'] == df['PULocationID'].shift()) &
    #     (df['DOLocationID'] == df['DOLocationID'].shift()) &
    #     (df['passenger_count'] == df['passenger_count'].shift()) &
    #     (df['payment_type'] == df['payment_type'].shift()) &
    #     (df['time_diff'] <= 120)  # within 2 minutes
    # )

    # near_duplicates = df[near_dup_condition]

    # print("=== NEAR DUPLICATE ANALYSIS ===")
    # print(f"Total rows: {len(df)}")
    # print(f"Near duplicates found: {len(near_duplicates)}")

    # # -------------------------------
    # # 5. Optional: strength check
    # # (distance + fare similarity)
    # # -------------------------------
    # if len(near_duplicates) > 0:
    #     print("\nSample near duplicates:")
    #     print(
    #         near_duplicates[
    #             ['trip_id',
    #              'pickup_time',
    #              'trip_distance',
    #              'fare_amount',
    #              'PULocationID',
    #              'DOLocationID']
    #         ].head(10)
    #     )

    #print(near_duplicates)

    return data
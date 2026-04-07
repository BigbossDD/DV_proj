import pandas as pd 

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





    # print(data.duplicated().sum()) # no duplicats 


    # we added some useful columns to the data to make it easier for us to do some analysis on it

    data['month'] = data['tpep_pickup_datetime'].dt.month

    data['pickup_hour'] = pd.to_datetime(data['tpep_pickup_datetime']).dt.hour

    data['pickup_weekday'] = pd.to_datetime(data['tpep_pickup_datetime']).dt.day_name()


    # checking for duplicates & removing them :
    #cols = [c for c in data.columns if c != 'trip_id']
    #df_clean = data.drop_duplicates(subset=cols)

    #print(f"Rows before : {len(data)}")
    #print(f"Rows after  : {len(df_clean)}")
    #print(f"Duplicates removed : {len(data) - len(df_clean)}")
    #data = df_clean

    '''
    Rows before : 11200280
    Rows after  : 11198026
    Duplicates removed : 2254 
    '''
    # not much value of them as we have 11m row so they wont have that big of an effect 
    return data
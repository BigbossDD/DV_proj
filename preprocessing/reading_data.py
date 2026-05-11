from importlib.resources import path

import pandas as pd 
#from preprocessing.Data_Quality_Review.data_desc import data_desc
def read_data():
    ## the path of data 
  #path = '~/Downloads/Project_master_clean.parquet' # if you dont have the clean data uncomment
   
   
  path = 'cleaned_data.parquet' # if you have the cleaned data
    
  
  data = pd.read_parquet(path) 
#### also add these 3 lines to the main function to make the cleaned data if you dont have it
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


    # not much value of them as we have 11m row so they wont have that big of an effect 

    

  return data

'''
    Rows before : 11200280
    Rows after  : 11198026
    Duplicates removed : 2254 
    '''
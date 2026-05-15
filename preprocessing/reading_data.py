from importlib.resources import path
import pandas as pd 

def read_data():
    ## the path of data 
  #path = '~/Downloads/Project_master_clean.parquet' # if you dont have the clean data uncomment
   
   
  path = 'cleaned_data.parquet' # if you have the cleaned data
    
  
  data = pd.read_parquet(path) 
#### 

  '''
  creating new columns for the analysis section to use them without the need to create them again and again
  '''

  data['month'] = data['tpep_pickup_datetime'].dt.month

  data['pickup_hour'] = pd.to_datetime(data['tpep_pickup_datetime']).dt.hour

  data['pickup_weekday'] = pd.to_datetime(data['tpep_pickup_datetime']).dt.day_name()

################
  '''
  if you want to check for duplicates & remove them , uncomment the code below 
  '''
    # checking for duplicates & removing them :
    # cols = [c for c in data.columns if c != 'trip_id']
    # df_clean = data.drop_duplicates(subset=cols)

    # print(f"Rows before : {len(data)}")
    # print(f"Rows after  : {len(df_clean)}")
    # print(f"Duplicates removed : {len(data) - len(df_clean)}")
    # data = df_clean

  return data

'''
    Rows before : 11200280
    Rows after  : 11198026
    Duplicates removed : 2254 
    '''
    # not much value of them as we have 11m row so they wont have that big of an effect 
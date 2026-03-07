import pandas as pd 


# the path of data 
path = 'C:/Users/USER/OneDrive/Desktop/PSUT/Data Visualization/Project_student.parquet'
data = pd.read_parquet(path)
print(data.store_and_fwd_flag.head(3))
# checking the data type checking if their is anything not numrical 


for column in data.columns:
    
    print(column , ' : ' , data[column].dtype)
# after checking , their are data type , and string type we will keep that 
#in mind for now 





#checking for nulls 

print(data.isnull().sum())
# nulls do exisit in and how we will dealwith it  {passenger_count:mean/mode ,RatecodeID: ?,  store_and_fwd_flag:mode ,payment_type : ??? , 
# congestion_surcharge : mode ,Airport_fee : mean}

data['passenger_count'].fillna(data['passenger_count'].mean(), inplace=True)
data['store_and_fwd_flag'].fillna(data['store_and_fwd_flag'].mode()[0], inplace=True)
data['congestion_surcharge'].fillna(data['congestion_surcharge'].mode()[0], inplace=True)
data['Airport_fee'].fillna(data['Airport_fee'].mean(), inplace=True)        
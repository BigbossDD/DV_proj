import pandas as pd 

def read_data():
    # the path of data 
    path = 'C:/Users/USER/OneDrive/Desktop/PSUT/Data Visualization/Project_student.parquet'
    data = pd.read_parquet(path)
    ### print(data.head(3))
    # checking the data type checking if their is anything not numrical 


    for column in data.columns:
        pass
      ###  print(column , ' : ' , data[column].dtype)
    # after checking , their are data type , and string type we will keep that 
    #in mind for now 





    #checking for nulls 

    ###print(data.isnull().sum())
    # nulls do exisit in and how we will dealwith it  {
    # passenger_count:mean'it make sense that we fill it with the mean as the ppl in the city are the same and that is there pattern' 
    # ,RatecodeID: mean 'it actally better as it help the company look good'
    # ,store_and_fwd_flag:mode 'as the higher precentge of ppl will be either y or n and the probablity that all these null '
    # ,payment_type : mode' as the there is a higher chance that those nulls follow the majority in the payment method ' , 
    # congestion_surcharge : mean ''
    # ,Airport_fee : mean ''
    # }

    data['passenger_count']=data['passenger_count'].fillna(data['passenger_count'].mean())
    data['RatecodeID']=data['RatecodeID'].fillna(data['RatecodeID'].mean())
    data['store_and_fwd_flag']=data['store_and_fwd_flag'].fillna(data['store_and_fwd_flag'].mode()[0])
    data['payment_type']=data['payment_type'].fillna(data['payment_type'].mode()[0])
    data['congestion_surcharge']=data['congestion_surcharge'].fillna(data['congestion_surcharge'].mode()[0])
    data['Airport_fee']=data['Airport_fee'].fillna(data['Airport_fee'].mean())        

    ### print(data.isnull().sum())

    ##### after dealing with the nulls we will check for duplicates
    # print(data.duplicated().sum()) # no duplicats 
    return data
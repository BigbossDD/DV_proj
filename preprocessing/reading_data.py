import pandas as pd 


# the path of data 
path = 'C:/Users/USER/OneDrive/Desktop/PSUT/Data Visualization/Project_student.parquet'
data = pd.read_parquet(path)
print(data.store_and_fwd_flag.head(3))
# checking the data type checking if their is anything not numrical 


for column in data.columns:
    
    print(column , ' : ' , data[column].dtype)
# after checking , their are data type , and string type  


#checking for nulls 


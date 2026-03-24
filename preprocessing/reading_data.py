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
    return data
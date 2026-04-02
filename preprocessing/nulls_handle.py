#this section deals with missing data 

def handle_nulls(data):

    #checking for nulls 

    

    #print(data.isnull().sum())
    # nulls do exisit in and how we will dealwith it  {
    # passenger_count:mean'it make sense that we fill it with the mean as the ppl in the city are the same and that is there pattern' 
    # ,RatecodeID: mean 'it actally better as it help the company look good'
    # ,store_and_fwd_flag:mode 'as the higher precentge of ppl will be either y or n and the probablity that all these null '
    # ,payment_type : mode' as the there is a higher chance that those nulls follow the majority in the payment method ' , 
    # congestion_surcharge : mean ''
    # ,Airport_fee : mean ''
    # }

    data['passenger_count']=data['passenger_count'].fillna(data['passenger_count'].mean()).round()  
    data['RatecodeID']=data['RatecodeID'].fillna(data['RatecodeID'].mean()).round()
    data['store_and_fwd_flag']=data['store_and_fwd_flag'].fillna(data['store_and_fwd_flag'].mode()[0])
    data['payment_type']=data['payment_type'].fillna(data['payment_type'].mode()[0]).round()
    data['congestion_surcharge']=data['congestion_surcharge'].fillna(data['congestion_surcharge'].mode()[0]).round()
    data['Airport_fee']=data['Airport_fee'].fillna(data['Airport_fee'].mean())

    ### print(data.isnull().sum())

    ##### after dealing with the nulls we will check for duplicates
    return data

'''
trip_id                        0
VendorID                       0
tpep_pickup_datetime           0
tpep_dropoff_datetime          0
passenger_count          2267572
trip_distance                  0
RatecodeID               2264213
store_and_fwd_flag       2264213
PULocationID                   0
DOLocationID                   0
payment_type                1702
fare_amount                    0
extra                          0
mta_tax                        0
tip_amount                     0
tolls_amount                   0
improvement_surcharge          0
total_amount                   0
congestion_surcharge     2264213
Airport_fee              2263828
cbd_congestion_fee             0
source_month                   0
'''

#print(data[data.payment_type.isnull()]['payment_type'])
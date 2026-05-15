#@#$#@#@$@#@#@#@##@##@#@@#@#@#@#@#@#@##@#@##@#@#@##@#@#@#@###@#@#@#@#@#@#@#@#@#@#@#@#
#@#$#@#@$@#@#@#@##@##@#@@#@#@#@#@#@#@##@#@##@#@#@##@#@#@#@###@##@#@#@#@#@#@#@#@#@#@#@#
#
#   this section deals with missing data 
#
def handle_nulls(data):

    
    # methods to handle nulls we used : 

    data['passenger_count'] = data['passenger_count'].fillna(data['passenger_count'].mode()[0])

    data['RatecodeID']=data['RatecodeID'].fillna(99)

    data['store_and_fwd_flag']=data['store_and_fwd_flag'].fillna(data['store_and_fwd_flag'].mode()[0])

    #data['payment_type']=data['payment_type'].fillna(5) --> **was solved by the client** 

    data['congestion_surcharge']=data['congestion_surcharge'].fillna(0)
    data['Airport_fee']=data['Airport_fee'].fillna(0)

    ### print(data.isnull().sum())

  
    return data

'''
trip_id                        0
VendorID                       0
tpep_pickup_datetime           0
tpep_dropoff_datetime          0
passenger_count          2267572
trip_distance                  0
RatecodeID               2264213 we could turn it into 99 which is the null flag for this col 
store_and_fwd_flag       2264213
PULocationID                   0
DOLocationID                   0
payment_type                1702 --> **was solved by the client** 
fare_amount                    0
extra                          0
mta_tax                        0
tip_amount                     0
tolls_amount                   0
improvement_surcharge          0
total_amount                   0
congestion_surcharge     2264213 we could say that it and the one below it could be zero as it is like a special additive to the cost 
Airport_fee              2263828
cbd_congestion_fee             0
source_month                   0
'''


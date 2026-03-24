import pandas as pd
from preprocessing.reading_data import read_data
from Analytical_section.Univariate_EDA.fare_amount import analyze_fare_amount
from Analytical_section.Univariate_EDA.trip_dist import trip_dist
from Analytical_section.Univariate_EDA.payment_type import payment_type
from Analytical_section.Univariate_EDA.rate_code import rate_code
from Analytical_section.Univariate_EDA.dist_passenger import dist_passenger
from Analytical_section.Univariate_EDA.count_trips_over_time import passenger_count_over_time
from preprocessing.nulls_handle import handle_nulls
from preprocessing.anomlies import detect_anomalies

def main():
    #Reading the data section
    print("Reading data...")
    data = read_data()
    #######
    #preprocessing
    print("Preprocessing data...")


    data = handle_nulls(data)
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
    #data = detect_anomalies(data)








    ###################################
    print('Starting analysis...')
    
    #
     
    print(data['RatecodeID'].value_counts())
    
    #UNIVARIATE ANALYSIS
    
    #analyze_fare_amount(data) # need work
    
    #trip_dist(data) # --> DONE , maybe color
    
    #payment_type(data) # --> need more on the color and the x axis numbers are bad looking 
    #rate_code(data) #--> the cols one of them is too tall it is basicly dominating the plot so we will need to change the width of the bars and maybe the color

    #dist_passenger(data) # --> DONE , maybe color and x axis numbers are bad looking
    
    #passenger_count_over_time(data)

    #multivariate analysis
    
    #bivariate analysis

if __name__ == "__main__":
    main()

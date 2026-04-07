import pandas as pd
from Analytical_section.Univariate_EDA.VendorID_trips_count_for_each import VendorID_trips_count_for_each
from Analytical_section.Bivariate_EDA.hour_x_trip_volume import hour_x_trip_volume
from Analytical_section.Bivariate_EDA.paymentType_X_totalAmount import paymentType_X_totalAmount
from Analytical_section.Bivariate_EDA.weekDay_X_demand import weekDay_x_trip_volume
from preprocessing.reading_data import read_data
from Analytical_section.Univariate_EDA.fare_amount import analyze_fare_amount
from Analytical_section.Univariate_EDA.trip_dist import trip_dist
from Analytical_section.Univariate_EDA.payment_type import payment_type
from Analytical_section.Univariate_EDA.rate_code import rate_code
from Analytical_section.Univariate_EDA.dist_passenger import dist_passenger
from Analytical_section.Univariate_EDA.passenger_count_over_time import passenger_count_over_time
from preprocessing.nulls_handle import handle_nulls
from preprocessing.anomlies import detect_anomalies
import seaborn as sns 
import matplotlib.pyplot as plt 

def main():
    #Reading the data section
    print("Reading data...")
    data = read_data()
    
    #######
    #preprocessing
    print("Preprocessing data...")
    #####
    
    data = handle_nulls(data)

    #data = detect_anomalies(data)

    ################### NOTE this section is MICS so delete when done 

    missing_cols = [
        'passenger_count',
        'RatecodeID',
        'store_and_fwd_flag',
        'payment_type',
        'congestion_surcharge',
        'Airport_fee'
    ]
    
    
###################################
    print('Starting analysis...')
    
    #
     
    
    #UNIVARIATE ANALYSIS
    
    #analyze_fare_amount(data) # -->DONE
    
    #trip_dist(data) # --> DONE , maybe color
    
    #payment_type(data) # --> need more on the color and the x axis numbers are bad looking 
    #rate_code(data) #--> the cols one of them is too tall it is basicly dominating the plot so we will need to change the width of the bars and maybe the color

    #dist_passenger(data) # --> check again 
    
    #passenger_count_over_time(data)

    VendorID_trips_count_for_each(data) # DONE

###################
    #bivariate analysis

    #hour_x_trip_volume(data)
    #weekDay_x_trip_volume(data)
    #paymentType_X_totalAmount(data)
    
    
###################
    #multivariate analysis
    
    

if __name__ == "__main__":
    main()

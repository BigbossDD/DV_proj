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
from Analytical_section.Bivariate_EDA.day_of_week_X_hours_X_total_count_of_trips import facet_hour_x_weekday
import seaborn as sns 
import matplotlib.pyplot as plt 

def main():
    #Reading the data section
    print("Reading data...")
    data = read_data()
    #df = data.copy()
      
    ########
    # #preprocessing
    print("Preprocessing data...")
   
    
    #data = handle_nulls(data)

    #data = detect_anomalies(data)

    ################### NOTE this section is MICS so delete when done 

    
    
###################################
    print('Starting analysis...')
    
    #
     
    
    #UNIVARIATE ANALYSIS
    #DONE section 
    '''
    dist_passenger(data) 

    analyze_fare_amount(data) 

    trip_dist(data) 
    
    rate_code(data)
    VendorID_trips_count_for_each(data)  --> maybe just humnize the code 
    '''
    
    payment_type(data)
    #passenger_count_over_time(data)

    # DONE

###################
    #bivariate analysis
    #DONE section : 
    '''
    hour_x_trip_volume(data)
    weekDay_x_trip_volume(data)
    facet_hour_x_weekday(data) 
    '''
    #
    
    #paymentType_X_totalAmount(data)--> check this again the box is ugly as f
    
    
###################
    #multivariate analysis
    
    

if __name__ == "__main__":
    main()

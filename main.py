#import pandas as pd
from Analytical_section.Bivariate_EDA.did_demand_increase_over_time import  demand_over_time
from Analytical_section.Multivariate_EDA import distance_fare_payment, distance_fare_tip_relationship, month_hour_demand_
from Analytical_section.Multivariate_EDA.cbd_congestion_before_after import cbd_effect_analysis
from Analytical_section.Multivariate_EDA.hour_revenue_trend_ import hour_revenue_trend
from Analytical_section.Multivariate_EDA.payment_hour_revenue_heatmap import payment_hour_revenue
from Analytical_section.Multivariate_EDA.revenue_efficiency_fare_per_mile import fare_per_mile_analysis
from Analytical_section.Multivariate_EDA.vendor_market_share import vendor_market_share__
from Analytical_section.Univariate_EDA.Top_pickUp_and_dropOff_loc import  top_locations_side_by_side
from Analytical_section.Univariate_EDA.VendorID_trips_count_for_each import VendorID_trips_count_for_each
from Analytical_section.Bivariate_EDA.hour_x_trip_volume import hour_x_trip_volume
from Analytical_section.Bivariate_EDA.paymentType_X_totalAmount import paymentType_X_totalAmount
from Analytical_section.Bivariate_EDA.weekDay_X_demand import weekDay_x_trip_volume
from Analytical_section.Univariate_EDA.vendors_share_of_market import vendor_market_share
from preprocessing.Data_Quality_Review import data_desc
from preprocessing.data_checker import full_data_quality_audit
from preprocessing.data_scan import data_quality_scan
from preprocessing.extract_ID_issue_rows import extract_issue_ids
from preprocessing.make_csv_file_for_issues import issues_to_csv
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
from Analytical_section.Multivariate_EDA.Hour_PaymentType_Demand import hour_payment_demand
import seaborn as sns 
from Analytical_section.Multivariate_EDA.month_hour_demand_ import month_hour_demand
from Analytical_section.Multivariate_EDA.hour_revenue_trend_ import hour_revenue_trend
from Analytical_section.Multivariate_EDA.distance_fare_payment import distance_fare_payments
import matplotlib.pyplot as plt 

def main():
    #Reading the data section
    print("Reading data...")
    data = read_data() # main data src
    
    ########
    # #preprocessing
    print("Preprocessing data...")
    
   
    ##if you want to make clean the data , uncomment 
    #the 3 lines below , and you need only to do it once if you dont have the data 
    #data = handle_nulls(data)
   
    #data = detect_anomalies(data)
    
    #data.to_parquet('cleaned_data.parquet', index=False)
######################################################################
    ################### NOTE this section is MICS so delete when done 
    # print(data.isna().sum())
    # print(data.describe())
######################################################################################
    print('Starting analysis...')
    
    #
    ######
    #UNIVARIATE ANALYSIS
     
    
    #dist_passenger(data) 
    #analyze_fare_amount(data)  
    #trip_dist(data) #NOTE
    #top_locations_side_by_side(data)  
    #rate_code(data) #NULL issue
    #VendorID_trips_count_for_each(data) 
    payment_type(data)
    #vendor_market_share(data)  #NOTE
    #passenger_count_over_time(data) 

###################
    #bivariate analysis
   
    #hour_x_trip_volume(data)
    #weekDay_x_trip_volume(data)
    #facet_hour_x_weekday(data) 
    #demand_over_time(data) 
    #paymentType_X_totalAmount(data) 
    
    
###################
    #multivariate analysis

    #hour_payment_demand(data)
    #hour_revenue_trend(data) # DONE 
    #distance_fare_payments(data) #BAD look
    #month_hour_demand(data)
    #fare_per_mile_analysis(data) #BAD look 
    #distance_fare_tip_relationship.distance_fare_tip_relationship__(data)
    #payment_hour_revenue(data)  

   # cbd_effect_analysis(data)       #BAD
           #color bad 
    
    #vendor_market_share__(data)  #BAD
if __name__ == "__main__":
    main()
    
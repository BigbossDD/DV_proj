import pandas as pd
from preprocessing.reading_data import read_data
from Analytical_section.Univariate_EDA.fare_amount import analyze_fare_amount
from Analytical_section.Univariate_EDA.trip_dist import trip_dist
from Analytical_section.Univariate_EDA.payment_type import payment_type
def main():
    #Reading the data section
    print("Reading data...")
    data = read_data()
    print('Starting analysis...')
    
    #
    
    #print(data.head(10))
    
    #UNIVARIATE ANALYSIS
    
    # analyze_fare_amount(data) # need work
    
    # trip_dist(data) # --> DONE , maybe color
    
    payment_type(data) # --> need more on the color and the x axis numbers are bad looking 
    
    #multivariate analysis
    
    #bivariate analysis

if __name__ == "__main__":
    main()

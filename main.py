import pandas as pd
from preprocessing.reading_data import read_data
#from Analytical_section.Univariate_EDA.fare_amount import analyze_fare_amount
from Analytical_section.Univariate_EDA.trip_dist import trip_dist

def main():
    data = read_data()

    
    #UNIVARIATE ANALYSIS
    #analyze_fare_amount(data)
    trip_dist(data)
    
    #multivariate analysis
    
    #bivariate analysis

if __name__ == "__main__":
    main()

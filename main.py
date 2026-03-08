import pandas as pd
from preprocessing.reading_data import read_data
from Analytical_section.Univariate_EDA.fare_amount import analyze_fare_amount
def main():
    data = read_data()

    
    #first we will explore the fare amount  -- uni
    analyze_fare_amount(data)
    
    
    
    
if __name__ == "__main__":
    main()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
def analyze_fare_amount(data):
    #NOTE this is a univariate analysis of the fare amount variable for only the trips with fare amount less than 150 
    # to remove outliers and negative values as more thann 90% of the data is less than 150 fare amount
    
    
    #a qucik preprocessing to remove outliers and negative values
    data=data[data.fare_amount < 150    ]
    data = data[data.fare_amount > 0    ]
    #######################
    plt.style.use('fast')
    plt.figure( figsize=(10, 6) )

    sns.histplot(x = data.fare_amount , bins = 220 , kde = False , color = 'lightgray'  ) 

    plt.axvline(x=data.fare_amount.mean(), color='black', linestyle='--', label='Mean')
  
    plt.axvline(x=data.fare_amount.median()  , color='darkgreen', label='Median')

    plt.legend()

    plt.title('Distribution of fare amount')
    plt.xlabel('Fare amount')
    plt.ylabel('Number of Trips')

    sns.despine() # to look like R classic
    plt.savefig('analyze_fare_amount')
    plt.show()    
    
    return
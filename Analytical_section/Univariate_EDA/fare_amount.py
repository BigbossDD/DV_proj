import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
def analyze_fare_amount(data):
    
    
    
    #NOTE : remove those later 
    data=data[data.fare_amount < 150    ]
    data = data[data.fare_amount > 0    ]
    
    plt.style.use('fast')
    plt.figure( figsize=(10, 6) )
    sns.histplot(x = data.fare_amount , bins = 220 , kde = False , color = 'lightgray'  ) # we are using fd to determin the bins    
    
    plt.axvline(x=data.fare_amount.mean(), color='black', linestyle='--', label='Mean')
    plt.text(data.fare_amount.mean(), plt.ylim()[1]*0.9, f'  Mean: {data.fare_amount.mean():.2f}', color='black')
    
    plt.axvline(x=data.fare_amount.median()  , color='darkgreen', label='Median')
    plt.text(data.fare_amount.median()   , plt.ylim()[1]*0.75, f'  median: {data.fare_amount.median():.2f}', color='black' , ha = 'left')
    
    plt.title('Distribution of fare amount')
    plt.xlabel('Fare amount')
    plt.ylabel('frequency of trips')

    sns.despine() # to look like R classic
    plt.savefig('analyze_fare_amount')
    plt.show()    
    
    return
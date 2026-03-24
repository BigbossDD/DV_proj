import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
def analyze_fare_amount(data):
    
    
    
    
    
     
    
    
    plt.figure()
    sns.displot(x = data.fare_amount , bins = 'fd' , kde = True , color = 'darkblue') # we are using fd to determin the bins    
    plt.title('Distribution of fare amount')
    plt.xlabel('Fare amount')

    plt.ylabel('Count')
    plt.savefig('analyze_fare_amount')
    plt.show()    
    
    return
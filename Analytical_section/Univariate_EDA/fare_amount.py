import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
def analyze_fare_amount(data):
    
    print(data.fare_amount.max())
    
    #now it gave 86k as a fare amount so for me it is odd so i will investigate
    
    #sns.boxplot(x  = data.fare_amount)
    #plt.show()
    
    # after checking the plot , there is  3 points of intrest , one at 5k other at 15k while the last at 86k 
    #so clearly they are outliers , and they wont be of any use to us , as even if they are real , 
    #they will be one in life anomaly rather than something you can study 
    #so we will remove them 
    
    data = data[data.fare_amount < 5000]
    
     
    #sns.boxplot(x  = data.fare_amount )
    #plt.show()

    # also after looking at the plot we can see some negative values which doesnt make any sense so we will 
    # multiply them by -1  , as it make sense that it is a mistake made when entering the value 
    data.fare_amount = data.fare_amount.apply(lambda x : -x if x < 0 else x)
    #sns.boxplot(x  = data.fare_amount )
    #plt.show()
    
    ##########
    #now the analysis 
    # we are looking for how economic valueable venturing into this market is 
    
    
    return
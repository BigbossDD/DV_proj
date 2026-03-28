#this section for unusal values  that isnt in the 
#look up table 
#as well outliers
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def detect_anomalies(data):

# 1- fare amount 
    #now it gave 86k as a max for fare amount so for me it is odd so i will investigate
    
    sns.boxplot(x  = data.fare_amount)
    plt.show()
    
    # after checking the plot , there is  7029 points of intrest , one at 5k other at 130k while the last at 863k 
    #so clearly they are outliers , and they wont be of any use to us , as even if they are real , 
    #they will be one in life anomaly rather than something you can study
    # there is no way someone is paying more than 150 to a taxi even in the worst scams  
    #so we will remove them 
    #data = data[data.fare_amount < 5000]

    # the rows that has this issue are : 
    #via -->
    x = data[data.fare_amount > 150 ]
    print(len(x[['trip_id', 'fare_amount','total_amount']]))

    

    #sns.boxplot(x  = data.fare_amount )
    #plt.show()

    # also after looking at the plot we can see some negative values which doesnt make any sense so we will 
    # multiply them by -1  , as it make sense that it is a mistake made when entering the value 
    data.fare_amount = data.fare_amount.apply(lambda x : -x if x < 0 else x)
    #sns.boxplot(x  = data.fare_amount )
    #plt.show()
    x = data[data.fare_amount <0]
    print(len(x[['trip_id', 'fare_amount','total_amount']]))

########
#2 - passenger count & tpep_pickup_datetime
    #first we will need to turn the date data into either years only or month and years 
    #in a way we will need to turn them  into groups/bins 

    # we sample 70 random
    #print(data.tpep_pickup_datetime.sample(70))

    #so after investigating the data is in this shape --> 2025-02-16 16:55:47
    # and it is all in 2025 so we will create bins for the months only and then we 
    # will count the number of trips in each month and then we will plot it

    data['month'] = data['tpep_pickup_datetime'].dt.month
    print(data['month'].value_counts())

    # after we checked the data we found that we have 6 month presented with these values : 
    #3     4146032
    #2     3578244
    #1     3475980
    #12         22
    #4           2
    # so from it  we can see clearly that we must remove month 12 and 4 as they are not representative
    #  and they are basically outliers and they will affect our analysis
    
    data = data[(data['month'] != 12) & (data['month'] != 4)]

    #ALSO in passenger_count there exist 1.2888 as a passenger_count which is not possible so it will need to be turned into 
    # 1 as it is the closest value to it and it is the most likely value to be the real one

#####################################
# 3- RatecodeID

    # in it exist values not in the look up table which are : 
    print(data['RatecodeID'].value_counts())
    '''
RatecodeID
 1.000000     8391091   OKAY
 2.459329     2264213   BAD  --> TURN TO 2 LOGICLY AS 2 MUST BE HIGHER THAN 3 
 2.000000      288617   OKAY
 99.000000     125079   OKAY
 5.000000       81028   OKAY
 3.000000       27176   OKAY
 4.000000       21318   OKAY
-1.000000         607   BAD --> TURN TO 1
 12.000000        607   BAD --> UNKNOWN
 88.000000        533   BAD --> TURN TO 99
 6.000000          11   OKAY
 '''
    

##############################################


    return  data 



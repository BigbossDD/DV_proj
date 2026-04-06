#this section for unusal values  that isnt in the 
#look up table 
#as well outliers
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def detect_anomalies(data):
#################
# NOTE this is UNivarite related : 
# 1- fare amount 
    #now it gave 86k as a max for fare amount so for me it is odd so i will investigate
    
    #sns.boxplot(x  = data.fare_amount)
    #plt.show()
    
    # after checking the plot , there is  7029 points of intrest , one at 5k other at 130k while the last at 863k 
    #so clearly they are outliers , and they wont be of any use to us , as even if they are real , 
    #they will be one in life anomaly rather than something you can study
    # there is no way someone is paying more than 150 to a taxi even in the worst scams  
    #so we will remove them 
    #data = data[data.fare_amount < 5000]

    # the rows that has this issue are : 
    #via -->
    #x = data[data.fare_amount > 150 ]
    #print(len(x[['trip_id', 'fare_amount','total_amount']]))


    # and above 500 there is 146 so a i can remove them as they will not affect the data 
    #x = data[data.fare_amount > 500 ]
    #print(len(x[['trip_id', 'fare_amount','total_amount']]))
    
    # so i will remove whats above 500 as it is not a real value and it will affect the data
    data = data[data.fare_amount < 500]


    
    

    #sns.boxplot(x  = data.fare_amount )
    #plt.show()

    # also after looking at the plot we can see some negative values which doesnt make any sense so we will 
    # multiply them by -1  , as it make sense that it is a mistake made when entering the value 
    data.fare_amount = data.fare_amount.apply(lambda x : -x if x < 0 else x)
    #sns.boxplot(x  = data.fare_amount )
    #plt.show()
    #x = data[data.fare_amount <0]
    #print(len(x[['trip_id', 'fare_amount','total_amount']]))

########
#2 - passenger count & tpep_pickup_datetime
    #first we will need to turn the date data into either years only or month and years 
    #in a way we will need to turn them  into groups/bins 

    # we sample 70 random
    #print(data.tpep_pickup_datetime.sample(70))

    #so after investigating the data is in this shape --> 2025-02-16 16:55:47
    # and it is all in 2025 so we will create bins for the months only and then we 
    # will count the number of trips in each month and then we will plot it

    
    #print(data['month'].value_counts())

    # after we checked the data we found that we have 6 month presented with these values : 
    #3     4146032
    #2     3578244
    #1     3475980
    #12         22
    #4           2
    # so from it  we can see clearly that we must remove month 12 and 4 as they are not representative
    #  and they are basically outliers and they will affect our analysis
    #print(data[data.month == 12][['trip_id','month']])
    #print(data[data.month == 4][['trip_id','month']])
    # the exact rows that has this issue : 
    '''        trip_id  month
    605          606     12
    687          688     12
    688          689     12
    861          862     12
    1108        1109     12
    1312        1313     12
    2276        2277     12
    3941        3942     12
    3942        3943     12
    4324        4325     12
    4370        4371     12
    4654        4655     12
    4655        4656     12
    5217        5218     12
    5335        5336     12
    7623        7624     12
    7624        7625     12
    7625        7626     12
    17542      17543     12
    20611      20612     12
    20612      20613     12
    7880444  7880445     12
            trip_id  month
    10278974  10278975      4
    10280573  10280574      4
'''
    data = data[(data['month'] != 12) & (data['month'] != 4)]

    #ALSO in passenger_count there exist 1.2888 as a passenger_count which is not possible so it will need to be turned into 
    # 1 as it is the closest value to it and it is the most likely value to be the real one
    data['passenger_count'] = data['passenger_count'].round().astype(int) #NOTE
#####################################
# 3- RatecodeID

    # in it exist values not in the look up table which are : 
    #print(data['RatecodeID'].value_counts())
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
    # so we will need to turn 2.459329 to 2 as it is the closest value to it and it is the most likely value to be the real one
    # also we will need to turn -1 to 1 as it is the closest value to it and it is the most likely value to be the real one
    # also we will need to turn 12 to unknown as it is not in the look up table and it is not a valid value
    # also we will need to turn 88 to 99 as it is the closest value to it and it is the most likely value to be the real one

    data['RatecodeID'] = data['RatecodeID'].apply(lambda x : 2 if x == 2.459329 else x)#NOTE
    data['RatecodeID'] = data['RatecodeID'].apply(lambda x : 1 if x == -1 else x)
    data['RatecodeID'] = data['RatecodeID'].apply(lambda x : 6 if x == 12 else x)
    data['RatecodeID'] = data['RatecodeID'].apply(lambda x : 99 if x == 88 else x)
#########################
#4- 
# in the trip dist col there are extreme values , like 300k miles which is not possible , and many outliers 
#so investgation where done and here it is its resluts : 

    # step 1 — understand the scale of the problem
    #print(data['trip_distance'].describe())

    # step 2 — bucket it to see where the junk starts
    #bins = [0, 10, 50, 100, 500, 1000, 10000, float('inf')]
    #labels = ['0-10', '10-50', '50-100', '100-500', '500-1k', '1k-10k', '10k+']
    #print(pd.cut(data['trip_distance'], bins=bins, labels=labels).value_counts().sort_index())

    # step 3 — cross check with fare_amount
    # a 300k mile trip should have an astronomical fare — if fare is $12, it's fake
    #print(data[data['trip_distance'] > 100000][['trip_id', 'trip_distance', 'fare_amount']].head(20))
    '''
    count    1.120028e+07
    mean     6.177720e+00
    std      5.817647e+02
    min     -3.809000e+01
    25%      1.000000e+00
    50%      1.720000e+00
    75%      3.240000e+00
    max      3.201363e+05
    Name: trip_distance, dtype: float64
    trip_distance
    0-10       10161809
    10-50        740724
    50-100         1033
    100-500         121
    500-1k            5
    1k-10k           40
    10k+            382
    Name: count, dtype: int64
                  trip_id  trip_distance  fare_amount
        2956166  2956167      158925.09        10.82
        2993346  2993347      121555.16         6.96
        2993436  2993437      143712.27         8.51
        2998745  2998746      101607.42        -1.50
        3009250  3009251      156037.94        28.74
        3027695  3027696      118435.89        18.09
        3034143  3034144      134033.15        18.14
        3049345  3049346      104448.07        15.38
        3069039  3069040      181139.99         6.33
        3070619  3070620      124083.23        12.14
        3081597  3081598      189687.43        12.70
        3107124  3107125      106629.95        12.55
        3112173  3112174      206137.99        24.89
        3138510  3138511      164959.95        14.05
        3151556  3151557      107806.31        24.25
        3188501  3188502      276099.95         9.13
        3195037  3195038      167452.94        -4.00
        3238331  3238332      114364.71        27.90
        3240337  3240338      222167.49        31.19
        3259180  3259181      121799.97        21.82
    '''
    # looking at the data above we can clearly see that fare amount in no way matches the dist covered 
    # no getting the mean for all the data point that have a dist above 100 miles

    #suspicious = data[data['trip_distance'] > 100][['trip_id', 'trip_distance', 'fare_amount']]

    #print(f"Count  : {len(suspicious)}")
    #print(f"\ntri_distance stats:")
    #print(suspicious['trip_distance'].describe())
    #print(f"\nfare_amount stats:")
    #print(suspicious['fare_amount'].describe())

    # the key ratio — if distance is 100k+ but fare is normal, it's corrupted
    #print(f"\nMean distance : {suspicious['trip_distance'].mean():,.2f} miles")
    #print(f"Mean fare     : {suspicious['fare_amount'].mean():,.2f} USD")
    #print(f"\nExpected fare at mean distance (at $3/mile) : ${suspicious['trip_distance'].mean() * 3:,.2f}")
    #print(f"Actual mean fare                             : ${suspicious['fare_amount'].mean():,.2f}")
    #Mean distance : 62,167.25 miles    
    #Mean fare     : 187.47 USD
    #Expected fare at mean distance (at $3/mile) : $186,501.75
    #Actual mean fare                             : $187.47
    '''
    Count  : 548 --> DATA points with trip distance above 100 miles

tri_distance stats:
count       548.000000
mean      62167.249069
std       55303.315991
min         100.170000
25%        1963.365000
50%       67088.645000
75%       89797.267500
max      320136.290000
Name: trip_distance, dtype: float64

fare_amount stats:
count      548.000000
mean       187.471880
std       1996.344116
min      -1807.600000
25%         11.200000
50%         19.910000
75%         36.560000
max      46263.880000
Name: fare_amount, dtype: float64
    '''
    #so a desion was taken to remove all the data points that have a trip distance above 100 miles as they are not real and they will affect our analysis
    data = data[data['trip_distance'] <= 100]
##############################################
#################
# NOTE this is bi-variate related : 
# 1- in payment type   
    '''
    payment_type
1.0    7483941 --> OK
0.0    2262858 --> OK
2.0    1135221  --> OK
4.0     241126  --> OK
3.0      72464  --> OK
8.0        605  --> BAD
9.0        559 --> BAD
7.0        549 --> BAD
5.0          1 --> OK , BUT it is only one value and it is called unknown so is it like a null value  ? 
<MIA> --> 6  and it is actually called voided so investgate ?
'''


    #print(data.payment_type.value_counts())

#2 - in total amount there exist some negative values which doesnt make any sense as it is the total amount that the 
# passenger paid so it will need to be turned into positive values as it is the most 
# likely case that it is a mistake made when entering the value 

     # amount of negative values is 186936 , which is high 

    data.total_amount = data.total_amount.apply(lambda x : -x if x < 0 else x)

##############################################
#################
# NOTE this is multi-variate related :
    return  data 



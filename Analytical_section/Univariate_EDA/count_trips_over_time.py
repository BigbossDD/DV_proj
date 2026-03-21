import matplotlib.pyplot as plt 
import seaborn as sns 

def passenger_count_over_time(data):
    # first we will need to turn the date data into either years only or month and years 
    #in a way we will need to turn them  into groups/bins 

    # we sample 70 random
    #print(data.tpep_pickup_datetime.sample(70))

    #so after investigating the data is in this shape --> 2025-02-16 16:55:47
    # and it is all in 2025 so we will create bins for the months only and then we 
    # will count the number of trips in each month and then we will plot it

    data['month'] = data['tpep_pickup_datetime'].dt.month
    #print(data['month'].value_counts())

    # after we checked the data we found that we have 6 month presented with these values : 
    #3     4146032
    #2     3578244
    #1     3475980
    #12         22
    #4           2
    # so from it  we can see clearly that we must remove month 12 and 4 as they are not representative
    #  and they are basically outliers and they will affect our analysis
    
    data = data[(data['month'] != 12) & (data['month'] != 4)]

    plt.style.use('classic')
    plt.figure(figsize=(12, 6))
    
    
    sns.countplot(
        data=data, 
        x='month', 
        hue='passenger_count', 
        palette='Set2',
       
    )
    
    #plt.title('Frequencies of Payment Types')
    #plt.xlabel('Payment Type')
    #plt.ylabel('Frequency')
    
    
    sns.despine() 
    
    plt.savefig('passenger_count_over_time.png')
    plt.show()
    
    
    
    return 


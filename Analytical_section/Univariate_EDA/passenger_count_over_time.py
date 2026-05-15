import matplotlib.pyplot as plt 
import seaborn as sns 
import matplotlib.ticker as mticker

def passenger_count_over_time(data):
    #preprocessing the data for the plot
    data = data[(data['month'] != 12) & (data['month'] != 4)]
    
    plt.style.use('fast')
    plt.figure(figsize=(12, 6))
    
    
    sns.countplot(
        data=data, 
        x='month', 
        hue='passenger_count', 
        palette='Set2',
       
    )
    
    plt.title('Passenger Count Distribution Over Months')
    plt.xlabel('Month')
    plt.ylabel('Number of Trips')
    
    plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
   
    sns.despine() 
    
    plt.savefig('passenger_count_over_time.png')
    plt.show()
    
    
    
    return 


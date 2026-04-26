import matplotlib.pyplot as plt 
import seaborn as sns 

def passenger_count_over_time(data):
    #

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
    import matplotlib.ticker as mticker
    plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
    #plt.yscale('log')
    sns.despine() 
    
    plt.savefig('passenger_count_over_time.png')
    plt.show()
    
    
    
    return 


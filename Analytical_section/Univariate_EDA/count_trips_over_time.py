import matplotlib.pyplot as plt 
import seaborn as sns 

def passenger_count_over_time(data):
    #

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


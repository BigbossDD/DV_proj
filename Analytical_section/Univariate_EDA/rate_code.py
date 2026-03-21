import matplotlib.pyplot as plt 
import seaborn as sns 

def rate_code(data):
   
    

    ##############
    plt.style.use('classic')
    plt.figure()
    
    #in it use tpep_pickup_datetime col , and passenger_count
    
    sns.countplot(y=data.RatecodeID,
                       width=0.6 , 
                       palette='Set2' , order = data.RatecodeID.value_counts().index)  
        

    
   # plt.yticks(ticks=[0, 1, 2, 3, 4, 5 ,6],
    #            labels=['Standard rate', 'JFK', 'Newark', 'Nassau or Westchester', 'Negotiated fare', 'Group ride', 'unknown' ])
    
    #plt.title('Frequencies of Payment Types')
    #plt.xlabel('Payment Type')
    #plt.ylabel('Frequency')
    
    
    sns.despine() 
    
    plt.savefig('rate_code_freq.png')
    plt.show()
    
    
    
    return 
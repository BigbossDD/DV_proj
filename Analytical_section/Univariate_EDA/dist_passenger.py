import matplotlib.pyplot as plt
import seaborn as sns

def dist_passenger(df):
    
    ##
    plt.style.use('fast')
    plt.figure()
     # also we want it hori and we want them ordered 

    sns.histplot(y = df.passenger_count, bins=9, kde=False, color='lightgray' ,  linewidth=2 , fill=True   )# we are using fd to determin the bins
    
    plt.title('Distribution of Trip Distance')
    plt.xlabel('Trip Distance (miles)')
    plt.ylabel('Frequency')
    
    plt.axvline(x=df.passenger_count.mean(), color='black', linestyle='--', label='Mean')
    #adding the value of the mean in numbers 
    plt.text(df.passenger_count.mean(), plt.ylim()[1]*0.9, f'  Mean: {df.passenger_count.mean():.2f}', color='black')
    
    plt.axvline(x=df.passenger_count.median(), color='darkgreen', linestyle='--', label='Median')
    plt.text(df.passenger_count.median(), plt.ylim()[1]*0.9, f'  median: {df.passenger_count.median():.2f}', color='black')
    
    plt.legend()
    
    sns.despine()
    #plt.xlim(0, 50)  # ?????Limit x-axis to focus on the majority of trips
    sns.despine()
    #now we will save the plot as an image file
    plt.savefig('dist_passenger.png')
    plt.show()

#
#Note : 
#from it we can tell that majority of the trips has 1 passenger






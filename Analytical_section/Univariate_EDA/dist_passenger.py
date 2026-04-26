import matplotlib.pyplot as plt
import seaborn as sns

def dist_passenger(df):
    
    ##
    sns.set_style('whitegrid')
    
    plt.figure( figsize=(10, 6) )
     # also we want it hori and we want them ordered 
    sns.countplot(x=df.passenger_count, color='lightgray')
    
    plt.title('Distribution of Passenger Count', fontsize=16)
    plt.xlabel('Passenger Count')
    plt.ylabel('Frequency')
    
    
    sns.despine()
    #now we will save the plot as an image file
    import matplotlib.ticker as mticker
    plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
    plt.savefig('dist_passenger.png')
    plt.show()





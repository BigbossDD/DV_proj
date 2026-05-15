import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.ticker as mticker


def dist_passenger(df):
    
    
    sns.set_style('whitegrid')
    
    plt.figure( figsize=(10, 6) )
     
    sns.countplot(x=df.passenger_count, color='lightgray')
    
    plt.title('Distribution of Passenger Count', fontsize=16)
    plt.xlabel('Passenger Count')
    plt.ylabel('Frequency')
    
    
    sns.despine()

    
    plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
    plt.savefig('dist_passenger.png')
    plt.show()


#.


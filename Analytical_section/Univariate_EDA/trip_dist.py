import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker
import pandas as pd
def trip_dist(df):
    #NOTE we sampled 200k rows to make the plot more readable and faster to run , 
    # you can change the number of rows by changing the number in the sample() function

    df = df.sample(200000, random_state=42)

    #################################################
    plt.style.use('fast')
    plt.figure(figsize=(10, 6))

    ax = sns.histplot(df['trip_distance'], bins=50, kde=False, color='lightgray')

    
    ax.xaxis.set_major_locator(mticker.MultipleLocator(0.5 ))   

    #
    plt.title('Distribution of Trip Distance')
    plt.xlabel('Trip Distance (miles)')
    plt.ylabel('Frequency')

    #  mean & Median of the cols :
    mean_val = df['trip_distance'].mean()
    median_val = df['trip_distance'].median()

    plt.axvline(x=mean_val, color='black', linestyle='--', label='Mean')
    plt.text(mean_val, plt.ylim()[1]*0.95, f'  Mean: {mean_val:.2f}', color='black')

    plt.axvline(x=median_val, color='darkgreen', label='Median')


    plt.text(median_val - 0.2,plt.ylim()[1] * 0.97,f'Median: {median_val:.2f}',
        color='darkgreen',
        ha='right')
    plt.legend()

    #
    sns.despine()

    plt.savefig('trip_distance_distribution.png')
    plt.show()
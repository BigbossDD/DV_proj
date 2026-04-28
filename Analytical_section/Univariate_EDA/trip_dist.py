import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker

def trip_dist(df):
    #NOTE remove later
    Q1 = df['trip_distance'].quantile(0.25)
    Q3 = df['trip_distance'].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df['trip_distance'] >= Q1 - 1.5 * IQR) & (df['trip_distance'] <= Q3 + 1.5 * IQR)]
    df = df[df['trip_distance'] > 0]

    plt.style.use('fast')
    plt.figure(figsize=(10, 6))

    ax = sns.histplot(df['trip_distance'], bins=50, kde=False, color='lightgray')

    
    ax.xaxis.set_major_locator(mticker.MultipleLocator(0.5))   # change to 0.25 if you want even more detail

    plt.title('Distribution of Trip Distance')
    plt.xlabel('Trip Distance (miles)')
    plt.ylabel('Frequency')

    # Mean & Median
    mean_val = df['trip_distance'].mean()
    median_val = df['trip_distance'].median()

    plt.axvline(x=mean_val, color='black', linestyle='--', label='Mean')
    plt.text(mean_val, plt.ylim()[1]*0.95, f'  Mean: {mean_val:.2f}', color='black')

    plt.axvline(x=median_val, color='darkgreen', label='Median')


    plt.text(median_val - 0.2,plt.ylim()[1] * 0.97,f'Median: {median_val:.2f}',
        color='darkgreen',
        ha='right')
    plt.legend()
    sns.despine()

    plt.savefig('trip_distance_distribution.png')
    plt.show()
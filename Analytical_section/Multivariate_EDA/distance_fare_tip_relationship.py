import matplotlib.pyplot as plt
import seaborn as sns


def distance_fare_tip_relationship__(data):

    df = data.copy()
    df = df[df['trip_distance'] <= 50]
    df =df[df.tip_amount > 0 ]
    plt.style.use('fast')
    plt.figure(figsize=(10, 6))
    
    #we will sample the data 
    sns.scatterplot(
        data=df.sample(150000, random_state=42),
        x='trip_distance',
        y='total_amount',
        hue='tip_amount',
        palette='coolwarm',
        alpha=0.4
    )

    plt.title('Distance vs Total Amount (Tip Intensity)')
    plt.xlabel('Trip Distance')
    plt.ylabel('Total Amount')

    plt.legend(title='Tip Amount')

    sns.despine()
    plt.tight_layout()
    plt.savefig('distance_fare_tip.png', dpi=150)
    plt.show()
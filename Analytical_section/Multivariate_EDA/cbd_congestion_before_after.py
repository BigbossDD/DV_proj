import matplotlib.pyplot as plt
import seaborn as sns

# cbd_congestion_before_after.py
def cbd_effect_analysis(df):

    #removing all totallamounts above 150 to avoid outliers
    df=df[df.total_amount < 150 ]
    

    df['period'] = df['tpep_pickup_datetime'] >= '2025-01-05'
    df['period'] = df['period'].map({True: 'After CBD Fee', False: 'Before CBD Fee'})

    plt.style.use('fast')
    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=df,
        x='period',
        y='total_amount',
        palette='Set2'
    )

    plt.title('Impact of CBD Congestion Fee (Before vs After Jan 5)')
    plt.xlabel('Period')
    plt.ylabel('Total Amount')

    sns.despine()
    plt.tight_layout()
    plt.savefig('cbd_before_after.png', dpi=150)
    plt.show()
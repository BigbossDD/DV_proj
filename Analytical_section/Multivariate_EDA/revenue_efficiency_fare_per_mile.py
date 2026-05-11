import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker

def fare_per_mile_analysis(data):

    df = data.copy()

    df = df[df['trip_distance'] > 0]
    df['fare_per_mile'] = df['total_amount'] / df['trip_distance']
    df = df[df['fare_per_mile'] < 200]

    plt.style.use('fast')
    plt.figure(figsize=(10, 6))

    ax = sns.histplot(
        df['fare_per_mile'],
        bins=100,
        kde=True,
        color='steelblue'
    )

    plt.title('Fare Efficiency (Revenue per Mile)')
    plt.xlabel('Fare per Mile')
    plt.ylabel('Frequency')

    # 👇 remove scientific notation (LE6 problem)
    plt.gca().yaxis.set_major_formatter(
        mticker.StrMethodFormatter('{x:,.0f}')
    )

    sns.despine()
    plt.tight_layout()
    plt.savefig('fare_per_mile.png', dpi=150)
    plt.show()
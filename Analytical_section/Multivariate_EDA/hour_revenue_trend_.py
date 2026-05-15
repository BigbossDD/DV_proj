import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker

def hour_revenue_trend(data):

    plt.style.use('fast')

    df = data.groupby('pickup_hour').agg({
        'trip_id': 'count',
        'total_amount': 'sum'
    }).reset_index()

    fig, ax1 = plt.subplots(figsize=(12,6))

  
    sns.lineplot(
        data=df,
        x='pickup_hour',
        y='trip_id',
        ax=ax1,
        marker='o',
        label='Trips'
    )

    ax1.set_title('Hourly Demand vs Revenue')

    ax1.set_xlabel('Hour of Day')
    ax1.set_ylabel('Number of Trips')

    
    ax1.set_xticks(range(24))

    
    ax1.yaxis.set_major_formatter(
        mticker.StrMethodFormatter('{x:,.0f}')
    )

    
    ax2 = ax1.twinx()

    sns.lineplot(
        data=df,
        x='pickup_hour',
        y='total_amount',
        ax=ax2,
        color='orange',
        marker='o',
        label='Revenue'
    )

    ax2.set_ylabel('Revenue (USD)')

    
    ax2.ticklabel_format(style='plain', axis='y')


    ax2.yaxis.set_major_formatter(
        mticker.StrMethodFormatter('${x:,.0f}')
    )

    
    lines1, labels1 = ax1.get_legend_handles_labels()
    
    
    lines2, labels2 = ax2.get_legend_handles_labels()

    ax1.legend(
        lines1 + lines2,
        labels1 + labels2,
        loc='upper left'
    )

    sns.despine()

    plt.tight_layout()

    plt.savefig('hour_revenue_trend.png', dpi=150)

    plt.show()
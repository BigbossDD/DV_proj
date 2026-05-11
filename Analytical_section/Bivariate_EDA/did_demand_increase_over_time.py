import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker

def demand_over_time(data):
    plt.style.use('fast')
    plt.figure(figsize=(12, 6))

    # ensure datetime
    data['tpep_pickup_datetime'] = pd.to_datetime(data['tpep_pickup_datetime'])

    # keep only assignment scope
    data = data[
        (data['tpep_pickup_datetime'].dt.year == 2025) &
        (data['tpep_pickup_datetime'].dt.month.isin([1, 2, 3]))
    ]

    # aggregate by day
    data['date'] = data['tpep_pickup_datetime'].dt.date
    daily_trips = data.groupby('date').size().reset_index(name='trip_count')

    # main trend
    #sns.lineplot(
    #    x='date',
    #    y='trip_count',
    #    data=daily_trips,
    #    label='Daily Trips'
    #)

    # 7-day rolling average
    daily_trips['rolling_avg'] = daily_trips['trip_count'].rolling(7).mean()

    sns.lineplot(
        x='date',
        y='rolling_avg',
        data=daily_trips,
       # linestyle='--',
        label='7-Day Average'
    )

    plt.title('Taxi Demand Trend (Jan–Mar 2025)')
    plt.xlabel('Date')
    plt.ylabel('Number of Trips')

    plt.gca().yaxis.set_major_formatter(
        mticker.StrMethodFormatter('{x:,.0f}')
    )

    plt.xticks(rotation=45)
    plt.legend()
    sns.despine()

    plt.tight_layout()
    plt.savefig('demand_over_time.png', dpi=150)
    plt.show()
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


def weekDay_x_trip_volume(data):
    plt.style.use('fast')
    plt.figure(figsize=(10, 6))

    

    # Group by weekday and count trips
    weekday_trips = data.groupby('pickup_weekday').size().reset_index(name='trip_count')
    # Define the order of weekdays
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',  'Saturday', 'Sunday']

# Plotting
    
    ax = sns.barplot(y='pickup_weekday', x='trip_count', data=weekday_trips, palette='viridis', order=weekday_order)


    for p in ax.patches:
        width = p.get_width()
        ax.annotate(
            f'{int(width):,}',   # formatted with commas
            (width, p.get_y() + p.get_height()/2),
            ha='left',
            va='center',
            xytext=(5, 0),       # small offset to the right
            textcoords='offset points'
        )
    import matplotlib.ticker as mticker
    plt.gca().xaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))

    plt.title('Trip Volume by Day of the Week')
    plt.ylabel('Day of the Week')
    plt.xlabel('Number of Trips')
    sns.despine()
    # Save the plot as an image file
    plt.savefig('weekday_x_trip_volume.png')
    plt.show()


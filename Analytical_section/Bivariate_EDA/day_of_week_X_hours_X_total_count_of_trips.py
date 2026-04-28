import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def facet_hour_x_weekday(df):
    plt.style.use('fast')

    # Aggregate data
    grouped = df.groupby(['pickup_weekday', 'pickup_hour']).size().reset_index(name='trip_count')

    # Weekday order
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    grouped['pickup_weekday'] = pd.Categorical(grouped['pickup_weekday'], categories=weekday_order, ordered=False)

    # Create FacetGrid
    g = sns.FacetGrid(
        grouped,
        col='pickup_weekday',
        col_wrap=3,              # 3 plots per row
        height=3.5,
        sharey=True             # important for comparison
    )

    # Map barplot to each facet
    g.map_dataframe(
        sns.barplot,
        x='pickup_hour',
        y='trip_count',
        palette='viridis'
    )

    # Titles and labels
    g.set_titles("{col_name}")
    g.set_axis_labels("Hour of Day", "Number of Trips")

    # Rotate x labels slightly for readability
    for ax in g.axes.flat:
        ax.tick_params(axis='x', rotation=45 , labelsize=6)

    sns.despine()

    plt.subplots_adjust(top=0.9)
    g.fig.suptitle('Trip Volume by Hour for Each Day of the Week')

    plt.savefig('facet_hour_x_weekday.png')
    plt.show()
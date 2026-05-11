import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker

def month_hour_demand(data):

    # remove inconsistent months
    data = data[(data['month'] != 12) & (data['month'] != 4)]

    plt.style.use('fast')

    # group data
    df = (
        data
        .groupby(['month', 'pickup_hour'])
        .size()
        .reset_index(name='trip_count')
    )

    # facet plot
    g = sns.FacetGrid(
        df,
        col='month',
        col_wrap=3,
        height=4,
        sharey=False
    )

    g.map_dataframe(
        sns.lineplot,
        x='pickup_hour',
        y='trip_count',
        marker='o'
    )

    # titles + labels
    g.set_titles("Month {col_name}")
    g.set_axis_labels("Hour of Day", "Number of Trips")

    # axis formatting
    for ax in g.axes.flat:

        ax.set_xticks(range(24))

        # rotate labels
        ax.tick_params(
            axis='x',
            rotation=45,
            labelsize=6
        )

        # align labels nicely
        for label in ax.get_xticklabels():
            label.set_horizontalalignment('right')

        # nicer y-axis formatting
        ax.yaxis.set_major_formatter(
            mticker.StrMethodFormatter('{x:,.0f}')
        )

    # extra spacing between facets
    g.fig.subplots_adjust(
        wspace=0.25,
        hspace=0.35
    )

    sns.despine()

    plt.savefig('month_hour_demand.png', dpi=150)

    plt.show()
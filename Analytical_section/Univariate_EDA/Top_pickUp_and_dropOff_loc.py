import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker

def top_locations_side_by_side(data):
    plt.style.use('fast')

    # ---- Mapping (ONLY top IDs) ----
    zone_map = {
        161: 'Midtown Center',
        237: 'Upper East Side South',
        236: 'Upper East Side North',
        132: 'JFK Airport',
        230: 'Times Sq/Theatre District',
        186: 'Penn Station/Madison Sq West',
        162: 'Midtown East',
        142: 'Lincoln Square East',
        234: 'Union Sq',
        170: 'Murray Hill',
        239: 'Upper West Side South',
        68:  'East Chelsea',
        141: 'Lenox Hill West'
    }

    # ---- Prepare data ----
    top_pickup = data['PULocationID'].value_counts().loc[
        [161,237,236,132,230,186,162,142,234,170]
    ]

    top_dropoff = data['DOLocationID'].value_counts().loc[
        [236,237,161,230,170,142,239,162,68,141]
    ]

    # map names
    top_pickup.index = [zone_map[i] for i in top_pickup.index]
    top_dropoff.index = [zone_map[i] for i in top_dropoff.index]

    # sort for clean horizontal bars
    top_pickup = top_pickup.sort_values()
    top_dropoff = top_dropoff.sort_values()

    # ---- Plot ----
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))

    # -------- Pickup --------
    ax = axes[0]
    ax.barh(top_pickup.index, top_pickup.values, color='#4C72B0')

    ax.set_title('Top 10 Pickup Locations', fontsize=13, fontweight='bold')
    ax.set_xlabel('Number of Trips')
    ax.set_ylabel('Zone')

    ax.xaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))

    for i, v in enumerate(top_pickup.values):
        ax.text(v, i, f' {v:,}', va='center')

    # -------- Dropoff --------
    ax = axes[1]
    ax.barh(top_dropoff.index, top_dropoff.values, color='#55A868')

    ax.set_title('Top 10 Dropoff Locations', fontsize=13, fontweight='bold')
    ax.set_xlabel('Number of Trips')
    ax.set_ylabel('Zone')

    ax.xaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))

    for i, v in enumerate(top_dropoff.values):
        ax.text(v, i, f' {v:,}', va='center')

    # ---- Final touches ----
    sns.despine()
    plt.tight_layout()
    plt.savefig('top_locations_side_by_side.png', dpi=150)
    plt.show()
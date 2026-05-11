import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def hour_payment_demand(data):

    plt.style.use('fast')

    # payment type labels
    payment_map = {
        0: 'Flex Fare',
        1: 'Credit Card',
        2: 'Cash',
        3: 'No Charge',
        4: 'Dispute',
        5: 'Unknown',
        6: 'Voided Trip'
    }

    # keep only valid payment types
    df = data[data['payment_type'].isin(payment_map.keys())].copy()

    # map labels
    df['payment_label'] = df['payment_type'].map(payment_map)

    # group
    grouped = (
        df
        .groupby(['pickup_hour', 'payment_label'])
        .size()
        .reset_index(name='trip_count')
    )

    # pivot
    pivot = grouped.pivot(
        index='pickup_hour',
        columns='payment_label',
        values='trip_count'
    )

    # column order
    ordered_cols = [
        'Credit Card',
        'Cash',
        'Flex Fare',
        'No Charge',
        'Dispute',
        'Unknown',
        'Voided Trip'
    ]

    pivot = pivot.reindex(columns=ordered_cols)

    # plot
    plt.figure(figsize=(12,6))

    sns.heatmap(
        pivot,
        cmap='viridis', # a more formal color scheme is : 'viridis' or 'plasma'
        linewidths=0.3
    )

    plt.title('Demand by Hour and Payment Type')

    plt.xlabel('Payment Type')
    plt.ylabel('Hour of Day')

    plt.tight_layout()

    plt.savefig('hour_payment_demand.png', dpi=150)

    plt.show()
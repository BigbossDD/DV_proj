import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker

# payment_hour_revenue_heatmap.py
def payment_hour_revenue(data):

    payment_map = {
        0: 'Flex Fare',
        1: 'Credit Card',
        2: 'Cash',
        3: 'No Charge',
        4: 'Dispute',
        5: 'Unknown',
        6: 'Voided Trip'
    }

    df = data[data['payment_type'].isin(payment_map.keys())].copy()

    df['payment_label'] = df['payment_type'].map(payment_map)

    grouped = (
        df.groupby(['pickup_hour', 'payment_label'])['total_amount']
        .sum()
        .reset_index()
    )

    pivot = grouped.pivot(
        index='pickup_hour',
        columns='payment_label',
        values='total_amount'
    )

    plt.style.use('fast')
    plt.figure(figsize=(12, 6))

    ax = sns.heatmap(
        pivot,
        cmap='viridis',
        cbar_kws={
            'format': mticker.StrMethodFormatter('{x:,.0f}')
        }
    )

    plt.title('Revenue by Hour and Payment Type')
    plt.xlabel('Payment Type')
    plt.ylabel('Hour of Day')

    plt.tight_layout()

    plt.savefig('payment_hour_revenue.png', dpi=150)

    plt.show()
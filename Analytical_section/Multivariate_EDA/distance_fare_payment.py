import matplotlib.pyplot as plt
import seaborn as sns

def distance_fare_payments(data):
    #only keeping dist that is less than 100m
    data = data[data['trip_distance'] < 40]
    # sample for performance
    df = data.sample(200000, random_state=42)
    
    plt.style.use('fast')
    plt.figure(figsize=(12, 6))

    ax = sns.scatterplot(
        data=df,
        x='trip_distance',
        y='fare_amount',
        hue='payment_type',
        alpha=0.4,
        palette='Set2'
    )

    # payment type labels
    payment_labels = {
        '0': 'Flex Fare',
    '1': 'Credit Card',
    '2': 'Cash',
    '3': 'No Charge',
    '4': 'Dispute',
    '5': 'Unknown',
    '6': 'Voided Trip',
    }

    # edit legend labels
    handles, labels = ax.get_legend_handles_labels()

    new_labels = [
        payment_labels.get(label, label)
        for label in labels
    ]

    ax.legend(handles, new_labels, title='Payment Type')

    plt.title('Distance vs Fare by Payment Type')

    plt.xlabel('Trip Distance (miles)')
    plt.ylabel('Fare Amount (USD)')

    sns.despine()

    plt.tight_layout()

    plt.savefig('distance_fare_payment.png', dpi=150)

    plt.show()
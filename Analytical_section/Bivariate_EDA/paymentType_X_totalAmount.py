import matplotlib.pyplot as plt
import seaborn as sns

def paymentType_X_totalAmount(data):
    #NOTE REMOVE LATER: 
    data = data[data['payment_type'].isin([0, 1, 2, 3, 4, 5 , 6 ])]

    df = data.sample(n=200_000, random_state=42)

    plt.style.use('classic')
    plt.figure(figsize=(12, 5))


    # map values to labels before plotting
    mapping = {
    0: 'Flex Fare',
    1: 'Credit Card',
    2: 'Cash',
    3: 'No Charge',
    4: 'Dispute',
    5: 'Unknown',
    6: 'Voided Trip'
    }

    order = data['payment_type'].value_counts().index


    #data['PaymentType_label'] = data['PaymentType'].map(label_map)

    sns.boxplot(
        x=df['payment_type'],
        y=df['total_amount'],
        palette='Set2'
        ,order=order
    )
    plt.xticks(
        ticks=range(len(order)),
        labels=[mapping[i] for i in order]
    )   
    
    plt.title('Total Amount by Payment Type')
    plt.xlabel('Payment Type')
    plt.ylabel('Total Amount')
    sns.despine()
    plt.tight_layout()
    plt.savefig('paymentType_X_totalAmount.png')
    plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

def paymentType_X_totalAmount(data):
    plt.style.use('classic')
    plt.figure(figsize=(12, 5))

    # map values to labels before plotting
    label_map = {
        1.0 : 'Credit card',
        2.0 : 'Cash',
        3.0 : 'No charge',
        4.0 : 'Dispute',
        5.0 : 'Unknown',
        6.0 : 'Voided trip'
    }

    #data['PaymentType_label'] = data['PaymentType'].map(label_map)

    sns.boxplot(
        x=data['payment_type'],
        y=data['total_amount'],
        palette='Set2'
    )

    plt.title('Total Amount by Payment Type')
    plt.xlabel('Payment Type')
    plt.ylabel('Total Amount')
    sns.despine()
    plt.tight_layout()
    plt.savefig('paymentType_X_totalAmount.png')
    plt.show()
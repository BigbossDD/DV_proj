#  frequencies of payment type

import matplotlib.pyplot as plt 
import seaborn as sns 

import matplotlib.ticker as mticker

def payment_type(data):
    
  
    sns.set_style('whitegrid') 
    plt.figure(figsize=(10, 6))
    
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

    ax = sns.countplot(
    y=data['payment_type'],
    order=order,
    palette='Set2'
)

    for container in ax.containers:
        ax.bar_label(container, fmt='{:,.0f}', padding=3)
        plt.yticks(
            ticks=range(len(order)),
            labels=[mapping[i] for i in order]
        )

    plt.title('Frequencies of Payment Types')
    plt.xlabel('Number of Trips')
    plt.ylabel('Payment Type')
        
   
    

    ax = plt.gca()
    ax.xaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_major_locator(mticker.MaxNLocator(nbins=6))
    
    plt.xticks(rotation=30)   
    
    sns.despine() 
    
    plt.savefig('payment_type_frequencies.png')
    plt.show()
    
    
    
    return 
    
    
    
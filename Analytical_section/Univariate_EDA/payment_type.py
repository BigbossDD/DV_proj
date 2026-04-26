#  frequencies of payment type

import matplotlib.pyplot as plt 
import seaborn as sns 

def payment_type(data):
    #NOTE REMOVE LATER: 

    data = data[data['payment_type'].isin([0, 1, 2, 3, 4, 5 , 6 ])]

    # payment type : 
    #0 : Flex Fare trip  1: credit card 2: cash 3: no charge 4: dispute 5: unknown 6: voided trip
    sns.set_style('whitegrid') # to have a nice background for the plot
    plt.figure()
    # we will do coord_flip() and make the bars horizontal
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

    sns.countplot(
        y=data['payment_type'],
        order=order,
        palette='Set2'
    )

    plt.yticks(
        ticks=range(len(order)),
        labels=[mapping[i] for i in order]
    )

    plt.title('Frequencies of Payment Types')
    plt.xlabel('Number of Trips')
    plt.ylabel('Payment Type')
        
    import matplotlib.ticker as mticker
    plt.gca().xaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
    
    sns.despine() # to look like R classic 
    # we will save the plot as an image file
    plt.savefig('payment_type_frequencies.png')
    plt.show()
    
    
    
    return 
    
    
    
#  frequencies of payment type

import matplotlib.pyplot as plt 
import seaborn as sns 

def payment_type(data):
    
    # payment type : 
    #0 : Flex Fare trip  1: credit card 2: cash 3: no charge 4: dispute 5: unknown 6: voided trip
    plt.style.use('classic')
    plt.figure()
    # we will do coord_flip() and make the bars horizontal
    sns.countplot(y=data['payment_type'], palette='Set2', order=data['payment_type'].value_counts().index , width=0.5  ) 
    # we will add the names of each payment type on the x-axis
    plt.yticks(ticks=[0, 1, 2, 3, 4, 5, 6], labels=['Flex Fare', 'Credit Card', 'Cash', 'No Charge', 'Dispute', 'Unknown', 'Voided Trip'])
    
    plt.title('Frequencies of Payment Types')
    plt.xlabel('Payment Type')
    plt.ylabel('Frequency')
    
    # we will have a classic background
    
    sns.despine() # to look like R classic 
    # we will save the plot as an image file
    plt.savefig('payment_type_frequencies.png')
    plt.show()
    
    
    
    return 
    
    
    
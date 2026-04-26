import matplotlib.pyplot as plt
import seaborn as sns


def rate_code(data):
    plt.style.use('classic')
    plt.figure(figsize=(12, 5))

    # map values to labels before plotting
    label_map = {
        1.0  : 'Standard rate',
        2.0  : 'JFK',
        3.0  : 'Newark',
        4.0  : 'Nassau or Westchester',
        5.0  : 'Negotiated fare',
        6.0  : 'Group ride',
        99.0 : 'Unknown'
    }

    data['RatecodeID_label'] = data['RatecodeID'].map(label_map)

    sns.countplot(
        y=data['RatecodeID_label'],
        width=0.8,
        palette='Set2',
        order=data['RatecodeID_label'].value_counts().index
    )

    plt.title('Frequencies of RateCode Types')
    plt.xlabel('Number of Trips')
    plt.ylabel('Rate Code')
    
    sns.despine()
    plt.tight_layout()
    
    plt.savefig('rate_code_freq.png')
    plt.show()
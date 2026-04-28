import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker

def VendorID_trips_count_for_each(data):
    
    plt.style.use('fast')
    plt.figure(figsize=(12, 6))

    vendor_map = {
        1: 'Creative Mobile Technologies',
        2: 'Crub Mobility',
        6: 'Myle Technologies',
        7: 'Helix'
    }

    data['VendorName'] = data['VendorID'].map(vendor_map)

    ax = sns.countplot(
        y=data.VendorName,
        palette='Set2',
        order=data.VendorName.value_counts().index
    )


    ax.xaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))

    
    for container in ax.containers:
        ax.bar_label(container, label_type='edge', padding=3, fmt='{:,.0f}')

    plt.title('Trip Count by Vendor', fontsize=14, fontweight='bold')
    plt.ylabel('Vendor')
    plt.xlabel('Number of Trips')

    sns.despine()
    plt.savefig('VendorID_trips_count_for_each.png', dpi=150, bbox_inches='tight')
    plt.show()
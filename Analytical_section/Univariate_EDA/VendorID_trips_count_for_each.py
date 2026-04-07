
import matplotlib.pyplot as plt
import seaborn as sns


def VendorID_trips_count_for_each(data):
    
    plt.style.use('bmh')
    plt.figure(figsize=(12, 6))

    '''
    1 = Creative Mobile Technologies, LLC
    2 = Crub Mobility LLC
    6 = Myle Technologies, Inc.
    7 = Helix
    '''
    vendor_map = {
    1: 'Creative Mobile Technologies',
    2: 'Crub Mobility',
    6: 'Myle Technologies',
    7: 'Helix'
}

    data['VendorName'] = data['VendorID'].map(vendor_map)



    ax = sns.countplot(y=data.VendorName  , palette='Set2' , order=data.VendorName.value_counts().index)

   
    for container in ax.containers:
         ax.bar_label(container, label_type='edge', padding=3 , fmt='%.0f')

    plt.title('Total Amount Distribution by VendorID', fontsize=14, fontweight='bold')

    
    plt.ylabel('VendorID', fontsize=12)
    
    plt.xlabel('Trip Count (in millions)', fontsize=12)

    plt.yticks(rotation=45)  



    sns.despine()
    plt.savefig('VendorID_trips_count_for_each.png', dpi=150, bbox_inches='tight')

    plt.show()

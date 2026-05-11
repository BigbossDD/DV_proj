import matplotlib.pyplot as plt
import pandas as pd
import squarify
import seaborn as sns
def vendor_market_share(data):
    
    plt.style.use('fast')
    plt.figure(figsize=(10, 8))

    vendor_map = {
        1: 'Creative Mobile Technologies',
        2: 'Crub Mobility',
        6: 'Myle Technologies',
        7: 'Helix'
    }

    data['VendorName'] = data['VendorID'].map(vendor_map)

    # count trips per vendor
    counts = data['VendorName'].value_counts()

    # convert to percentages
    total = counts.sum()
    percentages = (counts / total * 100).round(2)

    # labels (name + %)
    labels = [f"{name}\n{percent}%" for name, percent in zip(counts.index, percentages)]

    # plot treemap
    squarify.plot(
        sizes=counts.values,
        label=labels,
        alpha=0.8 , 
        color=['#4C72B0', '#55A868', '#C44E52', "#000000"],
    )

    plt.title('Market Share of Vendors (by Trip Volume)', fontsize=14, fontweight='bold')
    plt.axis('off')

    plt.savefig('vendor_market_share_treemap.png', dpi=150, bbox_inches='tight')
    plt.show()
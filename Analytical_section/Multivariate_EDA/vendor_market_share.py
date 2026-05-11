import matplotlib.pyplot as plt
import seaborn as sns

# vendor_market_share.py
def vendor_market_share__(data):

    vendor_map = {
        1: 'Creative Mobile Technologies',
        2: 'Crub Mobility',
        6: 'Myle Technologies',
        7: 'Helix'
    }

    df = data.copy()
    df['VendorName'] = df['VendorID'].map(vendor_map)

    vendor_counts = df['VendorName'].value_counts()

    plt.style.use('fast')
    plt.figure(figsize=(8, 8))

    plt.pie(
        vendor_counts,
        labels=vendor_counts.index,
        autopct='%1.1f%%',
        startangle=140
    )

    plt.title('Vendor Market Share (Trip Volume)')

    plt.tight_layout()
    plt.savefig('vendor_market_share.png', dpi=150)
    plt.show()
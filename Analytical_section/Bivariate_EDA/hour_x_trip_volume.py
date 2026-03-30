import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
def hour_x_trip_volume(df):
    plt.style.use('fast')
    plt.figure(figsize=(10, 6))
    
    # Extract hour from pickup_datetime
    df['pickup_hour'] = pd.to_datetime(df['tpep_pickup_datetime']).dt.hour
    
    # Group by hour and count trips
    hourly_trips = df.groupby('pickup_hour').size().reset_index(name='trip_count')
    
    # Plotting
    sns.barplot(x='pickup_hour', y='trip_count', data=hourly_trips, palette='viridis')
    
    plt.title('Trip Volume by Hour of the Day')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Trips')
    
    sns.despine()
    
    # Save the plot as an image file
    plt.savefig('hour_x_trip_volume.png')
    plt.show()
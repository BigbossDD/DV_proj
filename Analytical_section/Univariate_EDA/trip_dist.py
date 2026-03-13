# the distributions of trip distance
#
import matplotlib.pyplot as plt
import seaborn as sns

def trip_dist(df):
    
   #first checking for outliers 
    #sns.boxplot(x=df['trip_distance'])
    #plt.title('Boxplot of Trip Distance')
    #plt.show()
    ###
    # so they do exist , we will remove them 
    Q1 = df['trip_distance'].quantile(0.25)
    Q3 = df['trip_distance'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df['trip_distance'] >= lower_bound) & (df['trip_distance'] <= upper_bound)]
    
    #sns.boxplot(x=df['trip_distance'])
    #plt.title('Boxplot of Trip Distance')
    #plt.show()
    ####
    sns.set_style('whitegrid')
    plt.figure(figsize=(10, 6))
    # we are using fd to determin the bins 
    #sns.ecdfplot(df['trip_distance'] )
    sns.histplot(df['trip_distance'], bins='fd', kde=True, color='blue')
    plt.title('Distribution of Trip Distance')
    plt.xlabel('Trip Distance (miles)')
    plt.ylabel('Frequency')
    #we will have a classic background 
    plt.style.use('classic')
    #plt.xlim(0, 50)  # ?????Limit x-axis to focus on the majority of trips
    #now we will save the plot as an image file
    plt.savefig('trip_distance_distribution.png')
    plt.show()

#a quick note a 1 mile is ~1.6 km 
#
#






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
    #######################################################################
    ## Now to ploting
    ##
    plt.style.use('classic')
    plt.figure()
     
    #sns.histplot(df['trip_distance'], bins='fd', kde=True, palette='set2' , fill= True  )# we are using fd to determin the bins
    # Replace your histplot line with this:
    sns.kdeplot(df['trip_distance'], fill=True, color='#4C72B0',palette='Set2' , alpha=0.6)  # KDE plot with fill and color
    
    plt.title('Distribution of Trip Distance')
    plt.xlabel('Trip Distance (miles)')
    plt.ylabel('Frequency')
    
    plt.axvline(x=df['trip_distance'].mean(), color='black', linestyle='--', label='Mean')
    #adding the value of the mean in numbers 
    plt.text(df['trip_distance'].mean(), plt.ylim()[1]*0.9, f'  Mean: {df["trip_distance"].mean():.2f}', color='black')
    
    plt.axvline(x=df['trip_distance'].median(), color='darkgreen', linestyle='--', label='Median')
    plt.legend()
    
    #we will have a classic background 
   
    
    #plt.xlim(0, 50)  # ?????Limit x-axis to focus on the majority of trips
    #now we will save the plot as an image file
    plt.savefig('trip_distance_distribution.png')
    plt.show()

#a quick note a 1 mile is ~1.6 km 
# remove the lines that indicate max value it reachecd to 
#






# Create a bar chart to show the count of each 'service_type'.

import seaborn as sns

sns.countplot(data=analysis_df, x='service_type')
plt.xlabel('Service Type')
plt.ylabel('Count')
plt.title('Count of Service Types')
plt.xticks(rotation=45)
plt.show()


import pandas as pd

# Load your dataset into a DataFrame (replace 'your_dataset.csv' with your actual data file)
df = pd.read_csv('transformed_data.csv')

# Now, you can use the df DataFrame in your Folium code
import folium

# Create a map centered on a specific location (e.g., Australia)
m = folium.Map(location=[-25, 135], zoom_start=4)

# Add markers for each service location
for index, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['service_name'],
        icon=folium.Icon(icon='cloud')  # You can customize the icon here
    ).add_to(m)

# Display the map
m

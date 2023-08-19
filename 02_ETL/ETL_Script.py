## Extract The Data


import pandas as pd

df = pd.read_csv('suez_data.csv')



df.head()

# Data cleaning (removing duplicates)
df = df.drop_duplicates()

# Save the transformed data to a new CSV file
df.to_csv('transformed_data.csv', index=False)


# Load the transformed data for analysis
analysis_df = pd.read_csv('transformed_data.csv')

# Display the first few rows of the DataFrame
print(analysis_df.head())

# Calculate summary statistics
summary_stats = analysis_df.describe()


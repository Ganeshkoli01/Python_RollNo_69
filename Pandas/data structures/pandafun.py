import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Sneha'],
    'Age': [25, 28, 22, 26],
    'City': ['Mumbai', 'Delhi', 'Pune', 'Bangalore']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:\n", df)

# Show first 2 rows
print("\nFirst 2 rows:\n", df.head(2))

# Show information about the DataFrame
print("\nInfo about DataFrame:")
print(df.info())

# Describe numeric data
print("\nStatistics:\n", df.describe())

# Access a column
print("\nNames column:\n", df['Name'])

# Filter rows
print("\nPeople older than 24:\n", df[df['Age'] > 24])

# Add a new column
df['Country'] = 'India'
print("\nDataFrame after adding Country:\n", df)

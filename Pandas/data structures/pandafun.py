import pandas as pd

data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Sneha'],
    'Age': [25, 28, 22, 26],
    'City': ['Mumbai', 'Delhi', 'Pune', 'Bangalore']
}

df = pd.DataFrame(data)


print("DataFrame:\n", df)

print("\nFirst 2 rows:\n", df.head(2))


print("\nInfo about DataFrame:")
print(df.info())


print("\nStatistics:\n", df.describe())


print("\nNames column:\n", df['Name'])


print("\nPeople older than 24:\n", df[df['Age'] > 24])


df['Country'] = 'India'
print("\nDataFrame after adding Country:\n", df)

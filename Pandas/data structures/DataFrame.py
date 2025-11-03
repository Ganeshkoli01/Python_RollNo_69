import pandas as pd


data = {
    'Name': ['atharv', 'abhi', 'niru' ,'Ganesh'],
    'Age': [25, 30, 22 ,21],
    'Salary': [45000, 54000, 32000 ,1200000]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

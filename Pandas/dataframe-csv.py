import pandas as pd

data = pd.read_excel('data.xlsx', sheet_name='Sheet1')

print(data)

data2 = pd.read_csv('data.csv')

print(data2)

data3 = pd.read_json('data.json')
print(data3)

# Fetching the data set from the URL 

data4 = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
print(data4)

print(data4.info())
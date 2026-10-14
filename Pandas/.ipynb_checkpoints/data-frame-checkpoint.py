import pandas as pd

data = {
    "name":["Alice","Bob","Charlie"],
    "age":[25,45,78],
    "city":["Delhi","Mumbai","Banglore"]
}

df = pd.DataFrame(data)
print(df)

print(df.index)
print(df.columns)

df.index = ['a','b','c']
df.columns = ['Name','Age','City']

print(df.index)
print(df.columns)
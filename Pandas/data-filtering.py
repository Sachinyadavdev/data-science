import pandas as pd

data = pd.read_csv("financial_data.csv")

df = pd.DataFrame(data)

print(df)
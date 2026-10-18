import pandas as pd 

data = pd.read_csv("data.csv")

df = pd.DataFrame(data)

print(df)

filter_data = df['Marks']>80

print(filter_data)

filter_data.to_csv("New_Filter_Data.csv", index=False)  # Adding the index false will remove the indexes in the exported sheet 


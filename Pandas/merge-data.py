import pandas as pd

data1 = {
    "Department": ["HR", "IT", "Marketing", "Sales","MIS"],
    "Team": ["A", "B", "C", "D", "E"],
    "Budget": [100000, 150000, 120000, 130000, 140000]
}
df1 = pd.DataFrame(data1)

data2 = {
    "Department": ["HR", "IT", "Marketing", "Sales","Management"],   
    "Team": ["A", "B", "C", "D", "F"],
    "Revenue": [200000, 250000, 220000, 230000, 240000]
}
df2 = pd.DataFrame(data2)

merged_df = pd.merge(df1, df2, on="Department")

print(merged_df)

left_merged_df = pd.merge(df1, df2, on="Department", how="left")
print(left_merged_df)
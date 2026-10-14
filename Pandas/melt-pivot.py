import pandas as pd

data = {
    "Name":['Alice','Shubham','Ramprakash'],
    "Maths":['80','92','76'],
    "Science":['67','83','96'],
    "English":['78','94','67']

}

df = pd.DataFrame(data)

print(df)

melt_data = df.melt(id_vars=["Name"], value_vars=["Maths","Science","English"], var_name="Subject", value_name="Score")

print(melt_data)
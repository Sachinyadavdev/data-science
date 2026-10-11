import pandas as pd

data = {
    "name":["Alice","Bob","Charlie"],
    "age":[25,45,78],
    "city":["Delhi","Mumbai","Banglore"]
}

df = pd.DataFrame(data)
print(df)
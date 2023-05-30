# pip install persian
# pip install pandas

import pandas as pd
from persian import convert_fa_numbers

data = pd.read_json("home_data.json")
df = pd.DataFrame.from_records(data)
df.dropna(inplace=True)
df.replace({'Elevator': {"آسانسور ندارد": 0}}, regex=True, inplace=True)
df.replace({'Elevator': {'آسانسور': 1}}, regex=True, inplace=True)
df.replace({'Parking': {'پارکینگ ندارد': 0}}, regex=True, inplace=True)
df.replace({'Parking': {'پارکینگ': 1}}, regex=True, inplace=True)
df.replace({'Warehouse': {'انباری ندارد': 0}}, regex=True, inplace=True)
df.replace({'Warehouse': {'انباری': 1}}, regex=True, inplace=True)
df["Floor"] = df['Floor'].str.split(' از ', expand=True)[0]
for i in df["Floor"].index:
    if df.loc[i, "Floor"] == "همکف":
        df.loc[i, "Floor"] = 0

df["Floor"] = df['Floor'].apply(lambda x: convert_fa_numbers(x))
for i in df["price"].index:
    df.loc[i, "price"] = df.loc[i, "price"].split("تومان")[0]
    x = df.loc[i, "price"].split("٬")
    num = ""
    for j in x:
        num += j
    df.loc[i, "price"] = (float(num) / 1000000000)
for i in df["price per meter"].index:
    df.loc[i, "price per meter"] = df.loc[i, "price per meter"].split("تومان")[0]
    x = df.loc[i, "price per meter"].split("٬")
    num = ""
    for j in x:
        num += j
    df.loc[i, "price per meter"] = (float(num) / 1000000000)
df["Elevator"] = df['Elevator'].apply(lambda x: int(x))
df["Parking"] = df['Parking'].apply(lambda x: int(x))
df["Warehouse"] = df['Warehouse'].apply(lambda x: int(x))
df.to_json("home_data_clean.json")
df.to_csv("home_data_clean.csv")

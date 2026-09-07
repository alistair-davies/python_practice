#Pandas Dataframe Practice
import pandas as pd

df = pd.read_csv("people.csv")
print(df)

df.columns = df.columns.str.strip()
df["name"] = df["name"].str.strip()
df["name"] = df["name"].str.ljust(df["name"].str.len().max())


df["age_plus_10"] = df["age"] +10
print(df)

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

print(df)

df["height_m"] = df["height_cm"] /100

print(df)

df["first_letter"] = df["name"].str[0]
print(df)

print(df[df["age"] >= 30])

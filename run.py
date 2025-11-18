import pandas as pd
from datetime import datetime

import seaborn as sns
import matplotlib.pyplot as plt


date = datetime(2020, 5, 26) # vælg date

path = date.strftime("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/"
                     "csse_covid_19_data/csse_covid_19_daily_reports/%m-%d-%Y.csv")

df = pd.read_csv(path)

print(df.head())
print(df.info())

#rename
df_clean = df.rename(columns={
    "Country_Region": "Country",
    "Lat": "Latitude",
    "Long_": "Longitude"
})

# choose x kolonne
df_clean = df_clean[["Country", "Latitude", "Longitude",
                     "Confirmed", "Deaths", "Recovered", "Active"]]

df_clean.head()

df_grouped = df_clean.groupby("Country")[["Confirmed", "Deaths"]].sum() #group

top10 = df_grouped.sort_values("Confirmed", ascending=False).head(10)
top10


plt.figure(figsize=(12,6))
sns.barplot(x=top10.index, y=top10["Confirmed"])
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 lande med flest COVID-19 smittede (2020-05-26)")
plt.ylabel("Antal bekræftede")
plt.show()

plt.figure(figsize=(8,8))
plt.pie(top10["Deaths"], labels=top10.index, autopct="%1.1f%%")
plt.title("Fordeling af dødsfald blandt top 10 lande")
plt.show()

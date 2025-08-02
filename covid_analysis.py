import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('covid_data.csv')

print(df.head())
print(df.columns)

country_total = df.groupby('Country')['Confirmed'].sum().sort_values(ascending=False).head(10)
print(country_total)

country_total.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Top 10 Countries - Total COVID-19 Confirmed Cases')
plt.xlabel('Country')
plt.ylabel('Total Confirmed Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

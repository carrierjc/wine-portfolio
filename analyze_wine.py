import pandas as pd

df = pd.read_csv("winemag-data-130k-v2.csv")

# Basic insights
print("Top 5 countries by wine count:")
print(df['country'].value_counts().head())

print("\nAverage rating by country:")
print(df.groupby('country')['points'].mean().sort_values(ascending=False).head())

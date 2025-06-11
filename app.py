import streamlit as st
import pandas as pd

df = pd.read_csv("winemag-data-130k-v2.csv")

st.title("Wine Review Explorer 🍷")
st.write("Explore 130,000 wine reviews from WineEnthusiast.")

st.subheader("Top Wine-Producing Countries")
top_countries = df['country'].value_counts().head(10)
st.bar_chart(top_countries)

st.subheader("Average Points by Country")
avg_points = df.groupby('country')['points'].mean().sort_values(ascending=False).head(10)
st.dataframe(avg_points)

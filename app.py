import streamlit as st
import pandas as pd

st.title("Student Analysis Dashboard")

# Load data
df = pd.read_csv("students.csv")

st.subheader("Student Data")
st.dataframe(df)

st.subheader("Summary")
st.write(df.describe())

st.subheader("Marks Chart")
st.bar_chart(df.select_dtypes(include="number"))
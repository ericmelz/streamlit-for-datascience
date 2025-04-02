import streamlit as st
import pandas as pd
from pathlib import Path
import numpy as np

data_file = Path.cwd() / ".." / "notes" / "2_api" / "tips.csv"
df = pd.read_csv(data_file)

st.header('Dataframe')
st.caption('Display a dataframe as an interactive table')
st.dataframe(df, width=600, height=400)

st.header('Static')
st.caption('Display static table')
st.table(df.head())

st.header('json')
st.caption('Display object or string as prettified json object')

json_values = df.head(3).to_dict()
st.json(json_values)

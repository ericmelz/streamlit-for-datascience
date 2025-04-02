import streamlit as st
import pandas as pd
import numpy as np

# display almost anything
st.write('Hello world')
st.write('Welcome to Streamlit App APIs')
st.write(1234)

df = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
})
st.write(df)

st.write(np.array([1, 2, 3, 4]))

## Magic
st.write('Magic Commands')

df1 = pd.DataFrame({'col1': [1, 2, 3, 4]})
df1

x = 10
x

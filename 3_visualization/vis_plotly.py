import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px

data = pd.read_csv('../notes/2_api/tips.csv')

# Reference URL: https://pltoy.com/python/plotly-express
# 1. Draw histogram for total bill
# 2. Draw histogram for total bill and color by sex
# 3. Draw histogram for total bill and color by (sex, smoker, day, time)
# 4. Draw Scatter plot between total_bill and tips and color by ('sex','day','smoker','time')
# 5. Sunburst chart on features

st.subheader('1. Draw histogram for total bill')

fig = px.histogram(data_frame=data, x='total_bill')
st.plotly_chart(fig, key=1)

st.subheader('2. Draw histogram for total bill and color by sex')
fig = px.histogram(data_frame=data, x='total_bill', color='sex')
st.plotly_chart(fig, key=2)

st.subheader('3. Draw histogram for total bill and color by (sex, smoker, day, time)')
select = st.selectbox('Select the category to color', ('sex', 'smoker', 'day', 'time'), key=3)
fig = px.histogram(data_frame=data, x='total_bill', color=select)
st.plotly_chart(fig, key=4)

st.subheader('4. Draw Scatter plot between total_bill and tips and color by (sex,day,smoker,time)')
color_option = st.selectbox('Select the category to color', ('sex', 'smoker', 'day', 'time'), key=5)
fig = px.scatter(data_frame=data, x='total_bill', y='tip', color=color_option)
st.plotly_chart(fig, key=6)

st.subheader('5. Sunburst chart on features')
path = st.multiselect('select the categorical features path',
                      ('sex', 'day', 'smoker', 'time'))
fig = px.sunburst(data_frame=data, path=path)
st.plotly_chart(fig, key=7)

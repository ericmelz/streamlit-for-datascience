import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.header('matplotlib and seaborn visualizations in streamlit')

df = pd.read_csv('../notes/2_api/tips.csv')
st.dataframe(df.head())

## Questions
# 1. Find number of Male and Female distribution (pie and bar chart)
# 2. Find distribution of Male and Female spent (boxplot or kdeplot)
# 3. Find distribution of average total_bill across each day by male and female
# 4. Find the relation between total_bill and tip on time (scatter plot)

st.markdown('---')
with st.container():
    st.write('1. Find number of Male and Female distribution (pie and bar chart)')
    value_counts = df['sex'].value_counts()

    col1, col2 = st.columns(2)

    # pie chart
    fig, ax = plt.subplots()
    ax.pie(value_counts, autopct='%0.1f%%', labels=['Male', 'Female'])
    col1.pyplot(fig)

    # bar chart
    fig, ax = plt.subplots()
    ax.bar(value_counts.index, value_counts)
    col2.pyplot(fig)

    # put this in expander
    with st.expander('Click here to display value counts'):
        st.dataframe(value_counts)

# streamlit widgets and charts
data_types = df.dtypes
cat_cols = data_types[data_types == 'object'].index

st.markdown('---')
with st.container():
    feature = st.selectbox('Select the feature to display', cat_cols)
    value_counts = df[feature].value_counts()

    col1, col2 = st.columns(2)

    # pie chart
    fig, ax = plt.subplots()
    ax.pie(value_counts, autopct='%0.1f%%', labels=value_counts.index)
    col1.pyplot(fig)

    # bar chart
    fig, ax = plt.subplots()
    ax.bar(value_counts.index, value_counts)
    col2.pyplot(fig)

    # put this in expander
    with st.expander('Click here to display value counts'):
        st.dataframe(value_counts)


# 2. Find distribution of Male and Female spent (boxplot or kdeplot)
st.markdown('---')
with st.container():
    st.write('Distribution of Male and Female spend')
    chart = ('box', 'violin', 'kdeplot', 'histogram')
    chart_selection = st.selectbox('Select chart type', chart)
    fig, ax = plt.subplots()
    if chart_selection == 'box':
        sns.boxplot(x='sex', y='total_bill', data=df, ax=ax, hue='sex')
    elif chart_selection == 'violin':
        sns.violinplot(x='sex', y='total_bill', data=df, ax=ax, hue='sex')
    elif chart_selection == 'kdeplot':
        sns.kdeplot(x=df['total_bill'], hue=df['sex'], ax=ax, fill=True)
    elif chart_selection == 'histogram':
        sns.histplot(x='total_bill', hue='sex', data=df, ax=ax)
    else:
        st.error(f'Internal Error: Unknown chart_section: {chart_selection}')
    st.pyplot(fig)


# 3. Find distribution of average total_bill across each day by male and female
st.markdown('---')

with st.container():
    # 1. include all categorical features (multiselect)
    # 2. bar, area, line
    # 3. stacked (radio)
    c1, c2, c3 = st.columns(3)
    with c1:
        group_cols = st.multiselect('select the features', cat_cols, cat_cols[0])
        features_to_groupby = group_cols
        n_features = len(features_to_groupby)

    with c2:
        chart_type = st.selectbox('Select Chart type', ('bar', 'area', 'line'))

    with c3:
        stack_option = st.radio('Stacked', ('Yes', 'No'))
        if stack_option == 'Yes':
            stacked = True
        else:
            stacked = False

    feature = ['total_bill']
    select_cols = feature + features_to_groupby
    avg_total_bill = df[select_cols].groupby(features_to_groupby).mean()
    if n_features > 1:
        for i in range(n_features - 1):
            avg_total_bill = avg_total_bill.unstack()
    avg_total_bill.fillna(0, inplace=True)

    fig, ax = plt.subplots()
    avg_total_bill.plot(kind=chart_type, ax=ax, stacked=stacked)
    ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    ax.set_ylabel('Avg total bill')
    st.pyplot(fig)

    with st.expander('click here to view values'):
        st.dataframe(avg_total_bill)

    # 4. Find the relation between total_bill and tip on time (scatter plot)
    st.markdown('---')
    st.write('4. Find the relation between total_bill and tip on time (scatter plot)')
    fig, ax = plt.subplots()
    hue_type = st.selectbox('Select the feature to hue', cat_cols)

    sns.scatterplot(x='total_bill', y='tip', hue=hue_type, ax=ax, data=df)
    st.pyplot(fig)

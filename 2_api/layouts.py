import streamlit as st
import pandas as pd
import time

side_bar = st.sidebar

side_bar.header('Sidebar st.sidebar')
side_bar.caption('elements in sidebar are pinned to left')

df = pd.read_csv('../notes/2_api/tips.csv')
st.dataframe(df)

columns = tuple(df.columns)
st.write(columns)

select_column = side_bar.selectbox(
    "Select the column you want to display",
    columns
)

side_bar.write(f'You selected column={select_column}')
st.dataframe(df[[select_column]])

# Layout columns
st.header('Columns')
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('column-1')
    st.image('../notes/2_api/media/image.jpg')

with col2:
    st.subheader('column-2')
    st.dataframe(df)

with col3:
    st.subheader('column-3')
    st.dataframe(df[[select_column]])

st.header('Expander: st.expander')
with st.expander('Some explanation'):
    st.write("""
    this is some text\n
    and some more text\n
    this is some more text about the expander\n
    yup
    
    uh huh
    ### a header
    ```
    import streamlit as st
    
    st.write('yay')
    ```
    """)

st.header('Container: st.container')
with st.container():
    st.write('you are inside the container')

st.header('Empty')

placeholder = st.empty()

for i in range(1, 11):
    placeholder.write(f'This message will disappear in {11-i} seconds!')
    time.sleep(1)

placeholder.empty()

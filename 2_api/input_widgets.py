import streamlit as st
import pandas as pd
import numpy as np
import os

# load data
data = pd.read_csv('../notes/2_api/tips.csv')


def display_data_random(df):
    return df.sample(5)


st.subheader('Displaying 5 random rows')
st.caption('Click on the button below to display the rows randomly')
button = st.button('Display 5 Random Rows')
if button:
    sample = display_data_random(data)
    st.dataframe(sample)

st.markdown('---')
st.subheader('st.checkbox')
agree = st.checkbox('I agree to terms and conditions')
st.write('checkbox status = ', agree)

with st.container():
    st.info('What technologies do you know?')
    python = st.checkbox('Python')
    datascience = st.checkbox('Data Science')
    ai_ml = st.checkbox('AI/ML')
    android = st.checkbox('android')
    react = st.checkbox('React')
    java = st.checkbox('Java')
    javascript = st.checkbox('JavaScript')
    tech_button = st.button('Submit')
    if tech_button:
        tech_dict = {
            'python': python,
            'datascience': datascience,
            'ai_ml': ai_ml,
            'android': android,
            'react': react,
            'java': java,
            'javascript': javascript,
        }
        st.json(tech_dict)

st.markdown('---')
st.subheader('Radio Buttons')
radio_buttons = st.radio('what is your favorite color?', ('White', 'Black', 'Pink', 'Red', 'Blue', 'Green'))
st.write(f'Your favorite color is {radio_buttons}')

st.markdown('---')
st.subheader('st.selectbox')
select_box = st.selectbox('What skill do you want to learn the most',
                          ('Java', 'Python', 'C', 'C++', 'JavaScript', 'HTML', 'Others'))
st.write(f'You want to learn {select_box}')

st.markdown('---')
st.subheader('st.multiselect')
options = st.multiselect('What kind of movies do you like?',
                         ['Comedy',
                          'Action',
                          'SciFi',
                          'Drama',
                          'Romance']
                         )
st.write(f'you selected {options}')

st.markdown('---')
st.subheader('st.slider')
loan = st.slider('What is the loan amount you are looking for?', 0, 100000, 2000, 1000)
st.write(f"Your loan amount is {loan}")

st.markdown('---')
st.subheader('st.text_input, st.number_input')

with st.container():
    name = st.text_input('Please enter your name')
    age = st.number_input('What is your age', min_value=0, max_value=150,value=25, step=1)
    describe = st.text_area('Describe yourself', height=150)
    dob = st.date_input('Select date of birth')
    submit_button2 = st.button('Submit 2')

    if submit_button2:
        info = {
            'name': name,
            'age': age,
            'describe': describe,
            'dob': dob,
        }
        st.json(info)

st.markdown('---')
st.subheader('st.fileuploader')

uploaded_file = st.file_uploader('Choose a file')
save_button = st.button('save file')
if save_button:
    if uploaded_file is not None:
        with open(os.path.join('./save_folder', uploaded_file.name), mode='wb') as f:
            f.write(uploaded_file.getbuffer())
        st.success('File uploaded successfully')
    else:
        st.warning('Please select the file you want to upload')



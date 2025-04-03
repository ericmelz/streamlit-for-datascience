import streamlit as st

st.header('Registration Form')

col1, col2, col3 = st.columns(3)
with col1:
    title = st.selectbox('', ['', 'Mr', 'Mrs', 'Ms'])

with col2:
    first_name = st.text_input('First Name')

with col3:
    last_name = st.text_input('Last Name')

designation = st.selectbox('Designation', ['Software', 'Hardware'])

dob = st.date_input('Date of Birth')

gender = st.radio('Gender', ('Male', 'Female', 'Prefer Not to Say'))

age = st.slider('Age', 1, 100, 50)

submit_button = st.button('Submit')

if submit_button:
    info = {
        'title': title,
        'first_name': first_name,
        'last_name': last_name,
        'designation': designation,
        'dob': dob,
        'gender': gender,
        'age': age
    }
    st.json(info)

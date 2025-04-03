import streamlit as st

with st.form('myform'):
    st.subheader('Registration Form')

    col1, col2, col3 = st.columns(3)
    title = col1.selectbox('', ['', 'Mr', 'Mrs', 'Ms'])
    first_name = col2.text_input('First Name')
    last_name = col3.text_input('Last Name')
    designation = st.selectbox('Designation', ['Software', 'Hardware'])
    dob = st.date_input('Date of Birth', '1960-01-01')
    gender = st.radio('Gender', ('Male', 'Female', 'Prefer Not to Say'))
    age = st.slider('Age', 1, 100, 50)

    submitted = st.form_submit_button('Submit')
    if submitted:
        st.success('Form Submitted Successfully')
        name = f'{title} {first_name} {last_name}'
        info = {
            'name': name,
            'designation': designation,
            'dob': dob,
            'gender': gender,
            'age': age
        }
        st.json(info)

import streamlit as st
import time

st.header('st.progress')
st.caption('Display a progress bar')


def progress_bar():
    for pct_complete in range(1, 101):
        time.sleep(0.02)
        my_bar.progress(pct_complete)


with st.spinner("Something is processing.  Wait for it"):
    my_bar = st.progress(0)
    progress_bar()

st.subheader('st.info')
st.info('This is information')

st.subheader('st.success')
st.success('This is success')

st.subheader('st.warning')
st.warning('this is warning')

st.subheader('st.error')
st.error('this is error')

time.sleep(2)
st.balloons()

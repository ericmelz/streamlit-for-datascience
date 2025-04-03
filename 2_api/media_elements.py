import streamlit as st
from pathlib import Path

st.header('Display image using st.image')
st.image(Path.cwd() / ".." / "notes" / "2_api" / "media" / "image.jpg", caption='Beautiful city', width=900)

st.header('Display video')
video_file = open(Path.cwd() / ".." / "notes" / "2_api" / "media" / "waterfalls.mp4", 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

st.header('Display audio')
audio_file = open(Path.cwd() / ".." / "notes" / "2_api" / "media" / "audio.mp3", 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')

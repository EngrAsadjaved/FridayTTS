import streamlit as st
from gtts import gTTS
from io import BytesIO

# Define the Streamlit interface
st.title("Text-to-Speech with gTTS")
text_input = st.text_area("Enter text to synthesize:", "Hello, this is a test using gTTS.")

if st.button("Generate Speech"):
    tts = gTTS(text_input, lang="en")
    audio_output = BytesIO()
    tts.write_to_fp(audio_output)
    audio_output.seek(0)
    st.audio(audio_output, format="audio/wav")

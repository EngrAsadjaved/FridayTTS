# Import required libraries
import streamlit as st
from TTS.api import TTS
import numpy as np
from io import BytesIO

# Initialize the Tacotron2-DDC model
MODEL_NAME = "tts_models/en/ljspeech/tacotron2-DDC"
tts = TTS(MODEL_NAME)

# Streamlit app title and description
st.title("Tacotron2-DDC Text-to-Speech")
st.write("Convert text to speech using the Tacotron2-DDC model from Hugging Face!")

# User input for text
text = st.text_area("Enter the text you want to convert to speech:", "Hello, my name is Engineer Asad Javed. Finally, I have run the Tacotron2 DDC text-to-speech model. Great Hurrah!")

# Button to trigger TTS
if st.button("Generate Speech"):
    if text:
        # Generate speech
        output = BytesIO()
        tts.tts_to_file(text=text, file_path=output)
        
        # Rewind the buffer to the start
        output.seek(0)
        
        # Display audio in Streamlit
        st.audio(output, format="audio/wav")
        st.success("Speech synthesis complete!")
    else:
        st.error("Please enter some text to generate speech.")

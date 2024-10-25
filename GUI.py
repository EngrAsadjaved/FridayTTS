import streamlit as st
from gtts import gTTS
from io import BytesIO

# Custom background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f4f4f8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Instructions
st.title("🎙️ Text-to-Speech Generator")
st.markdown("Convert your text into speech with ease! Customize the voice speed and language as you like.")

# Layout with columns
col1, col2 = st.columns([3, 1])
with col1:
    text_input = st.text_area("Enter Text to Synthesize", "Hello, this is a test using gTTS.")

with col2:
    st.markdown("### Voice Settings")
    language = st.selectbox("Choose Language", ("English", "Spanish", "French", "German"))
    speed = st.slider("Adjust Speech Speed", 0.5, 1.5, 1.0, 0.1)

# Generate and Play Audio
if st.button("🔊 Generate Speech"):
    lang_code = {"English": "en", "Spanish": "es", "French": "fr", "German": "de"}[language]
    tts = gTTS(text_input, lang=lang_code, slow=speed < 1.0)
    audio_output = BytesIO()
    tts.write_to_fp(audio_output)
    audio_output.seek(0)
    st.audio(audio_output, format="audio/wav")
    st.success("Speech generated successfully! 🎉")

# Footer
st.markdown("---")
st.markdown("**Created with 💻 using Streamlit and gTTS**")

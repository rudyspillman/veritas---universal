import streamlit as st

st.set_page_config(page_title="VERITAS AI", layout="wide", initial_sidebar_state="collapsed")

BACKGROUND_URL = "https://i.postimg.cc/Kzv816Jc/VERITAS_AI_Universal_Verification_Engine_IMAGEN.png"

st.markdown(f"""
<style>
.stApp {{
    background-image: url("{BACKGROUND_URL}");
    background-size: cover;
    background-position: center;
}}
.stButton > button {{
    background-color: rgba(0,0,0,0.7);
    color: #00ffff;
    border: 2px solid #00ffff;
    font-size: 20px;
    padding: 15px;
    border-radius: 10px;
}}
</style>
""", unsafe_allow_html=True)

# Texto/Email
if st.button("📝 TEXT / EMAIL", key="text"):
    st.write("Subir texto o email")
    text = st.text_area("Texto:")
    if st.button("Verificar"):
        st.write("Texto recibido")

# URL/Link  
if st.button("🔗 URL / LINK", key="url"):
    st.write("Ingresar URL")
    url = st.text_input("URL:")
    if st.button("Verificar"):
        st.write("URL recibida")

# Imagen
if st.button("🖼️ IMAGE", key="image"):
    st.write("Subir imagen")
    img = st.file_uploader("Imagen:", type=["jpg", "png"])
    if st.button("Verificar"):
        st.write("Imagen recibida")

# Video
if st.button("🎥 VIDEO", key="video"):
    st.write("Subir video")
    vid = st.file_uploader("Video:", type=["mp4"])
    if st.button("Verificar"):
        st.write("Video recibido")

# Audio
if st.button("🔊 AUDIO", key="audio"):
    st.write("Subir audio")
    aud = st.file_uploader("Audio:", type=["mp3"])
    if st.button("Verificar"):
        st.write("Audio recibido")

import streamlit as st
import base64

st.set_page_config(page_title="VERITAS AI", layout="wide", initial_sidebar_state="collapsed")

BACKGROUND_URL = "https://i.postimg.cc/Kzv816Jc/VERITAS_AI_Universal_Verification_Engine_IMAGEN.png"

# CSS simplificado
st.markdown(f"""
<style>
.stApp {{
    background-image: url("{BACKGROUND_URL}");
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position: center;
}}
[data-testid="stAppViewContainer"] {{
    background: transparent;
}}
</style>
""", unsafe_allow_html=True)

# Estado
if 'uploader' not in st.session_state:
    st.session_state.uploader = None

# Botones con st.columns
cols = st.columns(5)

with cols[0]:
    if st.button("📝 TEXT", use_container_width=True, key="btn1"):
        st.session_state.uploader = "text"
with cols[1]:
    if st.button("🔗 URL", use_container_width=True, key="btn2"):
        st.session_state.uploader = "url"
with cols[2]:
    if st.button("🖼️ IMAGE", use_container_width=True, key="btn3"):
        st.session_state.uploader = "image"
with cols[3]:
    if st.button("🎥 VIDEO", use_container_width=True, key="btn4"):
        st.session_state.uploader = "video"
with cols[4]:
    if st.button("🔊 AUDIO", use_container_width=True, key="btn5"):
        st.session_state.uploader = "audio"

# Uploaders
if st.session_state.uploader == "text":
    st.markdown("### 📝 TEXT/EMAIL")
    text = st.text_area("Paste text:")
    file = st.file_uploader("Or upload file:", type=["txt", "pdf"])
    if st.button("Verify"):
        st.write("Verifying...")
    if st.button("Close"):
        st.session_state.uploader = None

elif st.session_state.uploader == "url":
    st.markdown("### 🔗 URL/LINK")
    url = st.text_input("Enter URL:")
    if st.button("Verify"):
        st.write("Verifying...")
    if st.button("Close"):
        st.session_state.uploader = None

elif st.session_state.uploader == "image":
    st.markdown("### 🖼️ IMAGE")
    img = st.file_uploader("Upload image:", type=["jpg", "png"])
    if st.button("Verify"):
        st.write("Verifying...")
    if st.button("Close"):
        st.session_state.uploader = None

elif st.session_state.uploader == "video":
    st.markdown("### 🎥 VIDEO")
    vid = st.file_uploader("Upload video:", type=["mp4", "mov"])
    if st.button("Verify"):
        st.write("Verifying...")
    if st.button("Close"):
        st.session_state.uploader = None

elif st.session_state.uploader == "audio":
    st.markdown("### 🔊 AUDIO")
    aud = st.file_uploader("Upload audio:", type=["mp3", "wav"])
    if st.button("Verify"):
        st.write("Verifying...")
    if st.button("Close"):
        st.session_state.uploader = None

# CSS para posicionar botones sobre la imagen
st.markdown("""
<style>
div[data-testid="column"] {
    position: absolute !important;
}
div[data-testid="column"]:nth-child(1) {
    top: 18% !important;
    left: 60% !important;
}
div[data-testid="column"]:nth-child(2) {
    top: 18% !important;
    left: 22% !important;
}
div[data-testid="column"]:nth-child(3) {
    top: 42% !important;
    left: 18% !important;
}
div[data-testid="column"]:nth-child(4) {
    top: 55% !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
}
div[data-testid="column"]:nth-child(5) {
    top: 42% !important;
    left: 64% !important;
}
.stButton > button {
    width: 220px !important;
    height: 80px !important;
    background: rgba(0,0,0,0.7) !important;
    border: 2px solid #00ffff !important;
    color: #00ffff !important;
    font-size: 20px !important;
}
</style>
""", unsafe_allow_html=True)

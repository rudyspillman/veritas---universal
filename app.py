import streamlit as st

st.set_page_config(page_title="VERITAS AI", layout="wide", initial_sidebar_state="collapsed")

BACKGROUND_URL = "https://i.postimg.cc/Kzv816Jc/VERITAS_AI_Universal_Verification_Engine_IMAGEN.png"

st.markdown(f"""
<style>
.stApp {{
    background-image: url("{BACKGROUND_URL}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
#MainMenu, footer, header {{visibility: hidden;}}
.container {{position: relative; width: 100vw; height: 100vh;}}
</style>
""", unsafe_allow_html=True)

if 'current_uploader' not in st.session_state:
    st.session_state.current_uploader = None

# Botones con columnas para posicionamiento
st.markdown('<div class="container">', unsafe_allow_html=True)

# Crear 5 botones en posiciones específicas
positions = [
    ('📝 TEXT / EMAIL', 18, 60, 'text'),
    ('🔗 URL / LINK', 18, 22, 'url'),
    ('🖼️ IMAGE', 42, 18, 'image'),
    ('🎥 VIDEO', 55, 50, 'video'),
    ('🔊 AUDIO', 42, 64, 'audio')
]

for label, top, left, key in positions:
    col1, col2, col3 = st.columns([left, 100-left-20, 20])
    with col2 if key == 'video' else col1:
        if st.button(label, key=f"btn_{key}"):
            st.session_state.current_uploader = key
        st.markdown(f"""
        <style>
        div[data-testid="column"]:nth-of-type({positions.index((label, top, left, key))*3+1}) {{
            position: absolute;
            top: {top}%;
            left: {left}%;
            transform: {'translateX(-50%)' if key == 'video' else 'none'};
        }}
        .stButton > button {{
            min-width: 220px;
            padding: 22px 26px;
            background: rgba(0,0,0,0.65);
            border: 2px solid #00ffff;
            border-radius: 14px;
            color: #00ffff;
            font-size: 28px;
            font-weight: 600;
            box-shadow: 0 0 18px rgba(0,255,255,0.35);
            transition: all 0.25s ease-in-out;
        }}
        .stButton > button:hover {{
            background: #00ffff;
            color: #000;
            box-shadow: 0 0 28px #00ffff;
            transform: scale(1.05);
        }}
        </style>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Uploaders
if st.session_state.current_uploader == 'text':
    st.subheader("📝 TEXT / EMAIL VERIFICATION")
    text_input = st.text_area("Paste text or email content:", height=150)
    email_file = st.file_uploader("Or upload file:", type=["txt", "eml", "msg"], key="text_file")
    if st.button("Verify Text/Email"):
        if text_input or email_file:
            st.success("Processing...")
    if st.button("Close"):
        st.session_state.current_uploader = None

elif st.session_state.current_uploader == 'url':
    st.subheader("🔗 URL / LINK VERIFICATION")
    url_input = st.text_input("Enter URL or link:")
    if st.button("Verify URL"):
        if url_input:
            st.success("Processing...")
    if st.button("Close"):
        st.session_state.current_uploader = None

elif st.session_state.current_uploader == 'image':
    st.subheader("🖼️ IMAGE VERIFICATION")
    image_file = st.file_uploader("Upload image:", type=["jpg", "jpeg", "png", "gif", "bmp"], key="image_file")
    if st.button("Verify Image"):
        if image_file:
            st.success("Processing...")
    if st.button("Close"):
        st.session_state.current_uploader = None

elif st.session_state.current_uploader == 'video':
    st.subheader("🎥 VIDEO VERIFICATION")
    video_file = st.file_uploader("Upload video:", type=["mp4", "avi", "mov", "wmv", "flv"], key="video_file")
    if st.button("Verify Video"):
        if video_file:
            st.success("Processing...")
    if st.button("Close"):
        st.session_state.current_uploader = None

elif st.session_state.current_uploader == 'audio':
    st.subheader("🔊 AUDIO VERIFICATION")
    audio_file = st.file_uploader("Upload audio:", type=["mp3", "wav", "ogg", "m4a", "flac"], key="audio_file")
    if st.button("Verify Audio"):
        if audio_file:
            st.success("Processing...")
    if st.button("Close"):
        st.session_state.current_uploader = None

import streamlit as st

# =========================
# CONFIGURACIÓN GENERAL
# =========================
st.set_page_config(
    page_title="VERITAS AI — Universal Verification Engine",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# CSS GLOBAL
# =========================
BACKGROUND_URL = "https://i.postimg.cc/Kzv816Jc/VERITAS_AI_Universal_Verification_Engine_IMAGEN.png"

st.markdown(f"""
<style>
/* Fondo */
.stApp {{
    background-image: url("{BACKGROUND_URL}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* Ocultar elementos Streamlit */
#MainMenu, footer, header {{
    visibility: hidden;
}}

/* Contenedor overlay absoluto */
.overlay {{
    position: relative;
    width: 100%;
    height: 90vh;
}}

/* Botones flotantes */
.upload-btn {{
    position: absolute;
    min-width: 220px;
    padding: 22px 26px;
    background: rgba(0,0,0,0.65);
    border: 2px solid #00ffff;
    border-radius: 14px;
    color: #00ffff;
    font-size: 28px;
    font-weight: 600;
    text-align: center;
    cursor: pointer;
    box-shadow: 0 0 18px rgba(0,255,255,0.35);
    transition: all 0.25s ease-in-out;
    text-decoration: none;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}}

.upload-btn:hover {{
    background: #00ffff;
    color: #000;
    box-shadow: 0 0 28px #00ffff;
    transform: scale(1.05);
}}

/* POSICIONAMIENTO SIMÉTRICO */
.btn-text {{
    top: 18%;
    left: 60%;
}}

.btn-url {{
    top: 18%;
    left: 22%;
}}

.btn-image {{
    top: 42%;
    left: 18%;
}}

.btn-video {{
    top: 55%;
    left: 50%;
    transform: translateX(-50%);
}}

.btn-audio {{
    top: 42%;
    left: 64%;
}}

/* Estilos para los uploaders */
.uploader-container {{
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: rgba(0, 0, 0, 0.95);
    padding: 30px;
    border-radius: 15px;
    border: 2px solid #00ffff;
    box-shadow: 0 0 30px rgba(0,255,255,0.5);
    z-index: 2000;
    min-width: 400px;
    display: none;
}}

.uploader-container.active {{
    display: block;
}}

.close-btn {{
    position: absolute;
    top: 10px;
    right: 15px;
    color: #00ffff;
    font-size: 24px;
    cursor: pointer;
    background: none;
    border: none;
    z-index: 2001;
}}

.overlay-bg {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.8);
    z-index: 1999;
    display: none;
}}

.overlay-bg.active {{
    display: block;
}}
</style>
""", unsafe_allow_html=True)

# =========================
# JAVASCRIPT PARA LOS BOTONES
# =========================
st.markdown("""
<script>
function showUploader(type) {
    document.getElementById('overlay-bg').classList.add('active');
    document.getElementById(type + '-uploader').classList.add('active');
}

function hideUploader() {
    document.getElementById('overlay-bg').classList.remove('active');
    const uploaders = document.querySelectorAll('.uploader-container');
    uploaders.forEach(uploader => {
        uploader.classList.remove('active');
    });
}

// Cerrar al hacer clic fuera
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('overlay-bg').addEventListener('click', hideUploader);
});
</script>
""", unsafe_allow_html=True)

# =========================
# BOTONES PRINCIPALES
# =========================
st.markdown("""
<div class="overlay">
    <div class="upload-btn btn-text" onclick="showUploader('text')">📝 TEXT / EMAIL</div>
    <div class="upload-btn btn-url" onclick="showUploader('url')">🔗 URL / LINK</div>
    <div class="upload-btn btn-image" onclick="showUploader('image')">🖼️ IMAGE</div>
    <div class="upload-btn btn-video" onclick="showUploader('video')">🎥 VIDEO</div>
    <div class="upload-btn btn-audio" onclick="showUploader('audio')">🔊 AUDIO</div>
</div>
""", unsafe_allow_html=True)

# =========================
# CONTENEDOR PARA SUBIDAS (OVERLAY)
# =========================
st.markdown("""
<div class="overlay-bg" id="overlay-bg"></div>
""", unsafe_allow_html=True)

# =========================
# UPLOADERS INDIVIDUALES
# =========================
# Text/Email Uploader
st.markdown("""
<div class="uploader-container" id="text-uploader">
    <button class="close-btn" onclick="hideUploader()">×</button>
    <h3 style="color: #00ffff; margin-bottom: 20px;">📝 TEXT / EMAIL VERIFICATION</h3>
""", unsafe_allow_html=True)

text_input = st.text_area("Paste text or email content:", height=150)
email_file = st.file_uploader("Or upload text/email file:", type=["txt", "eml", "msg"])
if st.button("Verify Text/Email", key="verify_text"):
    if text_input or email_file:
        st.success("Text/Email submitted for verification!")
    else:
        st.warning("Please paste text or upload a file")
st.markdown("</div>", unsafe_allow_html=True)

# URL/Link Uploader
st.markdown("""
<div class="uploader-container" id="url-uploader">
    <button class="close-btn" onclick="hideUploader()">×</button>
    <h3 style="color: #00ffff; margin-bottom: 20px;">🔗 URL / LINK VERIFICATION</h3>
""", unsafe_allow_html=True)
url_input = st.text_input("Enter URL or link:")
if st.button("Verify URL", key="verify_url"):
    if url_input:
        st.success(f"URL submitted: {url_input}")
    else:
        st.warning("Please enter a URL")
st.markdown("</div>", unsafe_allow_html=True)

# Image Uploader
st.markdown("""
<div class="uploader-container" id="image-uploader">
    <button class="close-btn" onclick="hideUploader()">×</button>
    <h3 style="color: #00ffff; margin-bottom: 20px;">🖼️ IMAGE VERIFICATION</h3>
""", unsafe_allow_html=True)
image_file = st.file_uploader("Upload image:", type=["jpg", "jpeg", "png", "gif", "bmp"])
if st.button("Verify Image", key="verify_image"):
    if image_file:
        st.success("Image submitted for verification!")
    else:
        st.warning("Please upload an image")
st.markdown("</div>", unsafe_allow_html=True)

# Video Uploader
st.markdown("""
<div class="uploader-container" id="video-uploader">
    <button class="close-btn" onclick="hideUploader()">×</button>
    <h3 style="color: #00ffff; margin-bottom: 20px;">🎥 VIDEO VERIFICATION</h3>
""", unsafe_allow_html=True)
video_file = st.file_uploader("Upload video:", type=["mp4", "avi", "mov", "wmv", "flv"])
if st.button("Verify Video", key="verify_video"):
    if video_file:
        st.success("Video submitted for verification!")
    else:
        st.warning("Please upload a video")
st.markdown("</div>", unsafe_allow_html=True)

# Audio Uploader
st.markdown("""
<div class="uploader-container" id="audio-uploader">
    <button class="close-btn" onclick="hideUploader()">×</button>
    <h3 style="color: #00ffff; margin-bottom: 20px;">🔊 AUDIO VERIFICATION</h3>
""", unsafe_allow_html=True)
audio_file = st.file_uploader("Upload audio:", type=["mp3", "wav", "ogg", "m4a", "flac"])
if st.button("Verify Audio", key="verify_audio"):
    if audio_file:
        st.success("Audio submitted for verification!")
    else:
        st.warning("Please upload an audio file")
st.markdown("</div>", unsafe_allow_html=True)

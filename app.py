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
.btn {{
    display: block;
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
    text-decoration: none !important;
}}

.btn:hover {{
    background: #00ffff;
    color: #000;
    box-shadow: 0 0 28px #00ffff;
    transform: scale(1.05);
}}

/* POSICIONAMIENTO SIMÉTRICO */

/* TEXT / EMAIL */
#text {{
    top: 18%;
    left: 60%;
}}

/* URL / LINK */
#url {{
    top: 18%;
    left: 22%;
}}

/* IMAGE */
#image {{
    top: 42%;
    left: 18%;
}}

/* VIDEO */
#video {{
    top: 55%;
    left: 50%;
    transform: translateX(-50%);
}}

/* AUDIO */
#audio {{
    top: 42%;
    left: 64%;
}}
</style>
""", unsafe_allow_html=True)

# =========================
# URLs para cada funcionalidad
# =========================
# Reemplaza estas URLs con las tuyas
URLS = {
    "text": "https://tuejemplo.com/text",  # URL para texto/email
    "url": "https://tuejemplo.com/url",    # URL para enlaces
    "image": "https://tuejemplo.com/image", # URL para imágenes
    "video": "https://tuejemplo.com/video", # URL para videos
    "audio": "https://tuejemplo.com/audio"  # URL para audio
}

# =========================
# OVERLAY DE BOTONES CON ENLACES REALES
# =========================
st.markdown(f"""
<div class="overlay">
    <a href="{URLS['text']}" class="btn" id="text" target="_blank">📝 TEXT / EMAIL</a>
    <a href="{URLS['url']}" class="btn" id="url" target="_blank">🔗 URL / LINK</a>
    <a href="{URLS['image']}" class="btn" id="image" target="_blank">🖼️ IMAGE</a>
    <a href="{URLS['video']}" class="btn" id="video" target="_blank">🎥 VIDEO</a>
    <a href="{URLS['audio']}" class="btn" id="audio" target="_blank">🔊 AUDIO</a>
</div>
""", unsafe_allow_html=True)








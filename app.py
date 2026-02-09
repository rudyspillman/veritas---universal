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
}}

.btn:hover {{
    background: #00ffff;
    color: #000;
    box-shadow: 0 0 28px #00ffff;
    transform: scale(1.05);
}}

/* POSICIONAMIENTO SIMÉTRICO */

/* TEXT / EMAIL (arriba derecha, alineado al haz vertical) */
#text {{
    top: 18%;
    left: 60%;
}}

/* URL / LINK (arriba izquierda, misma distancia espejo) */
#url {{
    top: 18%;
    left: 22%;
}}

/* IMAGE (centro izquierda) */
#image {{
    top: 42%;
    left: 18%;
}}

/* VIDEO (centro inferior, alineado al eje) */
#video {{
    top: 55%;
    left: 50%;
    transform: translateX(-50%);
}}

/* AUDIO (centro derecha, más cerca del eje) */
#audio {{
    top: 42%;
    left: 64%;
}}
</style>
""", unsafe_allow_html=True)

# =========================
# OVERLAY DE BOTONES
# =========================
st.markdown("""
<div class="overlay">
    <div class="btn" id="text">📝 TEXT / EMAIL</div>
    <div class="btn" id="url">🔗 URL / LINK</div>
    <div class="btn" id="image">🖼️ IMAGE</div>
    <div class="btn" id="video">🎥 VIDEO</div>
    <div class="btn" id="audio">🔊 AUDIO</div>
</div>
""", unsafe_allow_html=True)








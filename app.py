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

/* Forzar overlay */
section.main > div {{
    position: relative;
    height: 90vh;
}}

/* Estilo base botones */
div[data-testid="stButton"] > button {{
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

div[data-testid="stButton"] > button:hover {{
    background: #00ffff;
    color: #000;
    box-shadow: 0 0 28px #00ffff;
    transform: scale(1.05);
}}

/* POSICIONES */
#btn-text button {{ top: 18%; left: 60%; }}
#btn-url button {{ top: 18%; left: 22%; }}
#btn-image button {{ top: 42%; left: 18%; }}
#btn-video button {{ top: 55%; left: 50%; transform: translateX(-50%); }}
#btn-audio button {{ top: 42%; left: 64%; }}
</style>
""", unsafe_allow_html=True)

# =========================
# BOTONES FUNCIONALES
# =========================

if st.button("📝 TEXT / EMAIL", key="btn-text"):
    st.success("TEXT / EMAIL ACTIVADO")

if st.button("🔗 URL / LINK", key="btn-url"):
    st.success("URL / LINK ACTIVADO")

if st.button("🖼️ IMAGE", key="btn-image"):
    st.success("IMAGE ACTIVADO")

if st.button("🎥 VIDEO", key="btn-video"):
    st.success("VIDEO ACTIVADO")

if st.button("🔊 AUDIO", key="btn-audio"):
    st.success("AUDIO ACTIVADO")






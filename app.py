import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="VERITAS AI — Universal Verification Engine",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- GLOBAL STYLES ----------------
background_url = "https://i.postimg.cc/Kzv816Jc/VERITAS_AI_Universal_Verification_Engine_IMAGEN.png"

st.markdown(f"""
<style>
/* Fondo */
.stApp {{
    background-image: url("{background_url}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* Ocultar UI Streamlit */
#MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}
header {{visibility: hidden;}}

/* Capa UI */
.ui-layer {{
    position: relative;
    width: 100%;
    height: 100vh;
}}

/* Botones */
.btn {{
    position: absolute;
    padding: 20px 36px;
    font-size: 28px;
    font-weight: 600;
    color: #00ffff;
    border: 2px solid #00ffff;
    border-radius: 18px;
    background: rgba(0,0,0,0.7);
    cursor: pointer;
    text-align: center;
    white-space: nowrap;
    box-shadow: 0 0 14px rgba(0,255,255,0.35);
}}
.btn:hover {{
    background: #00ffff;
    color: #000;
}}

/* POSICIONES SIMÉTRICAS */

/* Izquierda */
.image {{ top: 24%; left: 8%; }}
.audio {{ top: 44%; left: 8%; }}

/* Derecha */
.text  {{ top: 24%; right: 8%; }}
.url   {{ top: 44%; right: 8%; }}

/* Centro */
.video {{
    top: 56%;
    left: 50%;
    transform: translateX(-50%);
}}
</style>
""", unsafe_allow_html=True)

# ---------------- UI ----------------
st.markdown("""
<div class="ui-layer">
    <div class="btn image">🖼️ IMAGE</div>
    <div class="btn audio">🔊 AUDIO</div>

    <div class="btn text">📝 TEXT / EMAIL</div>
    <div class="btn url">🔗 URL / LINK</div>

    <div class="btn video">🎥 VIDEO</div>
</div>
""", unsafe_allow_html=True)

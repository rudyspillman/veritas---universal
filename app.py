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
.stApp {{
    background-image: url("{BACKGROUND_URL}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

#MainMenu, footer, header {{
    visibility: hidden;
}}

.overlay {{
    position: relative;
    width: 100%;
    height: 90vh;
}}

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
    text-decoration: none;
    display: inline-block;
}}

.btn:hover {{
    background: #00ffff;
    color: #000;
    box-shadow: 0 0 28px #00ffff;
    transform: scale(1.05);
}}

/* POSICIONES */
#text {{ top: 18%; left: 60%; }}
#url {{ top: 18%; left: 22%; }}
#image {{ top: 42%; left: 18%; }}
#video {{ top: 55%; left: 50%; transform: translateX(-50%); }}
#audio {{ top: 42%; left: 64%; }}
</style>
""", unsafe_allow_html=True)

# =========================
# BOTONES FUNCIONALES
# =========================
st.markdown("""
<div class="overlay">
    <a href="/?mode=text" class="btn" id="text">📝 TEXT / EMAIL</a>
    <a href="/?mode=url" class="btn" id="url">🔗 URL / LINK</a>
    <a href="/?mode=image" class="btn" id="image">🖼️ IMAGE</a>
    <a href="/?mode=video" class="btn" id="video">🎥 VIDEO</a>
    <a href="/?mode=audio" class="btn" id="audio">🔊 AUDIO</a>
</div>
""", unsafe_allow_html=True)




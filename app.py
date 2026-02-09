import streamlit as st
from streamlit.components.v1 import html

# =========================
# CONFIGURACIÓN GENERAL
# =========================
st.set_page_config(
    page_title="VERITAS AI — Universal Verification Engine",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "mode" not in st.session_state:
    st.session_state.mode = None

# =========================
# CSS + JS
# =========================
BACKGROUND_URL = "https://i.postimg.cc/Kzv816Jc/VERITAS_AI_Universal_Verification_Engine_IMAGEN.png"

html(f"""
<style>
.stApp {{
    background-image: url("{BACKGROUND_URL}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

#MainMenu, footer, header {{ visibility: hidden; }}

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
}}

.btn:hover {{
    background: #00ffff;
    color: #000;
    box-shadow: 0 0 28px #00ffff;
    transform: scale(1.05);
}}

#text {{ top: 18%; left: 60%; }}
#url {{ top: 18%; left: 22%; }}
#image {{ top: 42%; left: 18%; }}
#video {{ top: 55%; left: 50%; transform: translateX(-50%); }}
#audio {{ top: 42%; left: 64%; }}
</style>

<div class="overlay">
    <div class="btn" id="text" onclick="send('text')">📝 TEXT / EMAIL</div>
    <div class="btn" id="url" onclick="send('url')">🔗 URL / LINK</div>
    <div class="btn" id="image" onclick="send('image')">🖼️ IMAGE</div>
    <div class="btn" id="video" onclick="send('video')">🎥 VIDEO</div>
    <div class="btn" id="audio" onclick="send('audio')">🔊 AUDIO</div>
</div>

<script>
function send(value) {{
    const streamlitDoc = window.parent.document;
    const input = streamlitDoc.querySelector('input[data-testid="stTextInput"]');
    input.value = value;
    input.dispatchEvent(new Event('input', {{ bubbles: true }}));
}}
</script>
""", height=900)

# =========================
# INPUT OCULTO FUNCIONAL
# =========================
mode = st.text_input("", label_visibility="collapsed")

if mode:
    st.session_state.mode = mode

# =========================
# RESULTADO
# =========================
if st.session_state.mode:
    st.success(f"MODO ACTIVO: {st.session_state.mode.upper()}")





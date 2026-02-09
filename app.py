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

/* Contenedor para los botones */
.button-container {{
    position: relative;
    width: 100%;
    height: 90vh;
}}

/* Estilos para los botones de Streamlit */
.stButton > button {{
    position: absolute !important;
    min-width: 220px !important;
    padding: 22px 26px !important;
    background: rgba(0,0,0,0.65) !important;
    border: 2px solid #00ffff !important;
    border-radius: 14px !important;
    color: #00ffff !important;
    font-size: 28px !important;
    font-weight: 600 !important;
    box-shadow: 0 0 18px rgba(0,255,255,0.35) !important;
    transition: all 0.25s ease-in-out !important;
}}

.stButton > button:hover {{
    background: #00ffff !important;
    color: #000 !important;
    box-shadow: 0 0 28px #00ffff !important;
    transform: scale(1.05) !important;
}}

/* POSICIONAMIENTO DE LOS BOTONES */
/* TEXT / EMAIL */
#text-btn {{
    top: 18% !important;
    left: 60% !important;
}}

/* URL / LINK */
#url-btn {{
    top: 18% !important;
    left: 22% !important;
}}

/* IMAGE */
#image-btn {{
    top: 42% !important;
    left: 18% !important;
}}

/* VIDEO */
#video-btn {{
    top: 55% !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
}}

/* AUDIO */
#audio-btn {{
    top: 42% !important;
    left: 64% !important;
}}
</style>
""", unsafe_allow_html=True)

# =========================
# FUNCIONES PARA CADA BOTÓN
# =========================
def handle_text():
    st.session_state['selected'] = 'text'
    # Aquí puedes redirigir o mostrar contenido diferente

def handle_url():
    st.session_state['selected'] = 'url'

def handle_image():
    st.session_state['selected'] = 'image'

def handle_video():
    st.session_state['selected'] = 'video'

def handle_audio():
    st.session_state['selected'] = 'audio'

# =========================
# BOTONES CON STREAMLIT
# =========================
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    # Botones posicionados con CSS
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    
    # Botón TEXT/EMAIL
    if st.button('📝 TEXT / EMAIL', key='text', help="Verificar texto o email"):
        handle_text()
    
    # Botón URL/LINK  
    if st.button('🔗 URL / LINK', key='url', help="Verificar enlace web"):
        handle_url()
        
    st.markdown('</div>', unsafe_allow_html=True)

# Agrega más columnas para los otros botones si es necesario
# O usa un contenedor absoluto con CSS

# Para un enfoque más simple, puedes usar este método:
st.markdown("""
<div style='position: relative; height: 90vh;'>
    <div style='position: absolute; top: 18%; left: 60%;'>
        <a href='https://tuejemplo.com/text' style='
            display: inline-block;
            padding: 22px 26px;
            background: rgba(0,0,0,0.65);
            border: 2px solid #00ffff;
            border-radius: 14px;
            color: #00ffff;
            font-size: 28px;
            font-weight: 600;
            text-decoration: none;
            box-shadow: 0 0 18px rgba(0,255,255,0.35);
            transition: all 0.25s ease-in-out;
        '>📝 TEXT / EMAIL</a>
    </div>
</div>
""", unsafe_allow_html=True)

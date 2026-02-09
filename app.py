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

/* Contenedor principal */
.main-container {{
    position: relative;
    width: 100%;
    height: 100vh;
}}

/* Botones */
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

/* POSICIONAMIENTO */
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
# INICIALIZAR ESTADO
# =========================
if 'show_uploader' not in st.session_state:
    st.session_state.show_uploader = None

# =========================
# FUNCIONES PARA MOSTRAR UPLOADERS
# =========================
def show_text_uploader():
    st.session_state.show_uploader = 'text'

def show_url_uploader():
    st.session_state.show_uploader = 'url'

def show_image_uploader():
    st.session_state.show_uploader = 'image'

def show_video_uploader():
    st.session_state.show_uploader = 'video'

def show_audio_uploader():
    st.session_state.show_uploader = 'audio'

def close_uploader():
    st.session_state.show_uploader = None

# =========================
# BOTONES PRINCIPALES
# =========================
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Botón TEXT/EMAIL
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button('📝 TEXT / EMAIL', key='text_btn'):
        show_text_uploader()

# Botón URL/LINK  
col4, col5, col6 = st.columns([1, 1, 1])
with col4:
    if st.button('🔗 URL / LINK', key='url_btn'):
        show_url_uploader()

# Botón IMAGE
col7, col8, col9 = st.columns([1, 1, 1])
with col7:
    if st.button('🖼️ IMAGE', key='image_btn'):
        show_image_uploader()

# Botón VIDEO
col10, col11, col12 = st.columns([1, 1, 1])
with col11:
    if st.button('🎥 VIDEO', key='video_btn'):
        show_video_uploader()

# Botón AUDIO
col13, col14, col15 = st.columns([1, 1, 1])
with col14:
    if st.button('🔊 AUDIO', key='audio_btn'):
        show_audio_uploader()

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# UPLOADERS (MODALES)
# =========================
if st.session_state.show_uploader == 'text':
    with st.container():
        st.markdown("---")
        st.header("📝 TEXT / EMAIL VERIFICATION")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            text_input = st.text_area("Paste text or email content:", height=150)
        with col2:
            email_file = st.file_uploader("Or upload file:", type=["txt", "eml", "msg"])
        
        col3, col4 = st.columns([1, 1])
        with col3:
            if st.button("Verify", key="verify_text"):
                if text_input or email_file:
                    st.success("Text/Email submitted for verification!")
                else:
                    st.warning("Please paste text or upload a file")
        with col4:
            if st.button("Close", key="close_text"):
                close_uploader()

elif st.session_state.show_uploader == 'url':
    with st.container():
        st.markdown("---")
        st.header("🔗 URL / LINK VERIFICATION")
        
        url_input = st.text_input("Enter URL or link:")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Verify", key="verify_url"):
                if url_input:
                    st.success(f"URL submitted: {url_input}")
                else:
                    st.warning("Please enter a URL")
        with col2:
            if st.button("Close", key="close_url"):
                close_uploader()

elif st.session_state.show_uploader == 'image':
    with st.container():
        st.markdown("---")
        st.header("🖼️ IMAGE VERIFICATION")
        
        image_file = st.file_uploader("Upload image:", type=["jpg", "jpeg", "png", "gif", "bmp"])
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Verify", key="verify_image"):
                if image_file:
                    st.success("Image submitted for verification!")
                else:
                    st.warning("Please upload an image")
        with col2:
            if st.button("Close", key="close_image"):
                close_uploader()

elif st.session_state.show_uploader == 'video':
    with st.container():
        st.markdown("---")
        st.header("🎥 VIDEO VERIFICATION")
        
        video_file = st.file_uploader("Upload video:", type=["mp4", "avi", "mov", "wmv", "flv"])
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Verify", key="verify_video"):
                if video_file:
                    st.success("Video submitted for verification!")
                else:
                    st.warning("Please upload a video")
        with col2:
            if st.button("Close", key="close_video"):
                close_uploader()

elif st.session_state.show_uploader == 'audio':
    with st.container():
        st.markdown("---")
        st.header("🔊 AUDIO VERIFICATION")
        
        audio_file = st.file_uploader("Upload audio:", type=["mp3", "wav", "ogg", "m4a", "flac"])
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Verify", key="verify_audio"):
                if audio_file:
                    st.success("Audio submitted for verification!")
                else:
                    st.warning("Please upload an audio file")
        with col2:
            if st.button("Close", key="close_audio"):
                close_uploader()

# Script JavaScript para posicionamiento exacto
st.markdown("""
<script>
// Posicionar botones exactamente
function positionButtons() {
    const buttons = document.querySelectorAll('.stButton > button');
    
    // TEXT / EMAIL
    if (buttons[0]) {
        buttons[0].style.position = 'absolute';
        buttons[0].style.top = '18%';
        buttons[0].style.left = '60%';
    }
    
    // URL / LINK
    if (buttons[1]) {
        buttons[1].style.position = 'absolute';
        buttons[1].style.top = '18%';
        buttons[1].style.left = '22%';
    }
    
    // IMAGE
    if (buttons[2]) {
        buttons[2].style.position = 'absolute';
        buttons[2].style.top = '42%';
        buttons[2].style.left = '18%';
    }
    
    // VIDEO
    if (buttons[3]) {
        buttons[3].style.position = 'absolute';
        buttons[3].style.top = '55%';
        buttons[3].style.left = '50%';
        buttons[3].style.transform = 'translateX(-50%)';
    }
    
    // AUDIO
    if (buttons[4]) {
        buttons[4].style.position = 'absolute';
        buttons[4].style.top = '42%';
        buttons[4].style.left = '64%';
    }
}

// Ejecutar después de que se cargue la página
setTimeout(positionButtons, 100);
window.addEventListener('load', positionButtons);
</script>
""", unsafe_allow_html=True)

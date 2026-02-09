import streamlit as st

st.set_page_config(page_title="VERITAS AI", layout="wide", initial_sidebar_state="collapsed")

BACKGROUND_URL = "https://i.postimg.cc/Kzv816Jc/VERITAS_AI_Universal_Verification_Engine_IMAGEN.png"

st.markdown(f"""
<style>
.stApp {{
    background-image: url("{BACKGROUND_URL}");
    background-size: cover;
    background-position: center;
}}
#MainMenu, footer, header {{display: none;}}
</style>
""", unsafe_allow_html=True)

# POSICIONES DE LOS BOTONES (top, left)
positions = {
    'text': ('📝 TEXT / EMAIL', '18%', '60%'),
    'url': ('🔗 URL / LINK', '18%', '22%'),
    'image': ('🖼️ IMAGE', '42%', '18%'),
    'video': ('🎥 VIDEO', '55%', '50%'),
    'audio': ('🔊 AUDIO', '42%', '64%')
}

# MOSTRAR BOTONES CON HTML
button_html = """
<div style="position: relative; width: 100vw; height: 100vh;">
"""
for key, (label, top, left) in positions.items():
    button_html += f"""
    <div style="position: absolute; top: {top}; left: {left}; transform: translateX(-50%);">
        <form id="form_{key}">
            <input type="hidden" name="action" value="{key}">
            <button type="submit" style="
                min-width: 220px;
                padding: 22px 26px;
                background: rgba(0,0,0,0.65);
                border: 2px solid #00ffff;
                border-radius: 14px;
                color: #00ffff;
                font-size: 28px;
                font-weight: 600;
                box-shadow: 0 0 18px rgba(0,255,255,0.35);
                cursor: pointer;
                transition: all 0.25s ease-in-out;
            " 
            onmouseover="this.style.background='#00ffff'; this.style.color='#000'; this.style.boxShadow='0 0 28px #00ffff'; this.style.transform='scale(1.05)'"
            onmouseout="this.style.background='rgba(0,0,0,0.65)'; this.style.color='#00ffff'; this.style.boxShadow='0 0 18px rgba(0,255,255,0.35)'; this.style.transform='scale(1)'">
                {label}
            </button>
        </form>
    </div>
    """
button_html += "</div>"

st.markdown(button_html, unsafe_allow_html=True)

# MANEJAR CLICS DE BOTONES
if 'action' in st.query_params:
    action = st.query_params['action']
    st.session_state.current_uploader = action

# SUBIR ARCHIVOS
if 'current_uploader' in st.session_state:
    if st.session_state.current_uploader == 'text':
        st.header("📝 TEXT / EMAIL VERIFICATION")
        st.text_area("Paste text or email:", height=150)
        st.file_uploader("Upload file:", type=["txt", "eml"])
        if st.button("Close"): st.session_state.current_uploader = None
        
    elif st.session_state.current_uploader == 'url':
        st.header("🔗 URL / LINK VERIFICATION")
        st.text_input("Enter URL:")
        if st.button("Close"): st.session_state.current_uploader = None
        
    elif st.session_state.current_uploader == 'image':
        st.header("🖼️ IMAGE VERIFICATION")
        st.file_uploader("Upload image:", type=["jpg", "png"])
        if st.button("Close"): st.session_state.current_uploader = None
        
    elif st.session_state.current_uploader == 'video':
        st.header("🎥 VIDEO VERIFICATION")
        st.file_uploader("Upload video:", type=["mp4", "avi"])
        if st.button("Close"): st.session_state.current_uploader = None
        
    elif st.session_state.current_uploader == 'audio':
        st.header("🔊 AUDIO VERIFICATION")
        st.file_uploader("Upload audio:", type=["mp3", "wav"])
        if st.button("Close"): st.session_state.current_uploader = None

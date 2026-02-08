import streamlit as st
import time
st.markdown("""
<style>
/* Agrandar botones al doble */
div.stButton > button {
    font-size: 24px;
    padding: 20px 40px;
    border-radius: 16px;
    width: 100%;
}

/* Contenedor centrado */
.button-container {
    max-width: 420px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="VERITAS AI - Universal Engine",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ESTILOS CSS (DISEÑO VISUAL) ---
background_url = "https://i.postimg.cc/Kzv816Jc/VERITAS_AI_Universal_Verification_Engine_IMAGEN.png"

st.markdown(f"""
    <style>
    /* Fondo */
    .stApp {{
        background-image: url("{background_url}");
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
    }}
    
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    /* Estilo de Botones (Neon/Tecno) */
    .stButton > button {{
        width: 100%;
        background-color: rgba(0, 0, 0, 0.7);
        color: #00ffff;
        border: 2px solid #00ffff;
        border-radius: 12px;
        font-weight: bold;
        font-size: 20px;
        text-transform: uppercase;
        padding: 15px;
        transition: all 0.3s;
        box-shadow: 0 0 10px rgba(0, 255, 255, 0.2);
    }}
    .stButton > button:hover {{
        background-color: #00ffff;
        color: black;
        box-shadow: 0 0 20px #00ffff;
        transform: scale(1.05);
    }}

    /* Cajas de Input (Cuando se abren) */
    .input-box {{
        background-color: rgba(0, 0, 0, 0.9);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #555;
        margin-top: 10px;
        margin-bottom: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# --- ESPACIADOR SUPERIOR (Para bajar todo el contenido) ---
st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)

# --- GRILLA PRINCIPAL DE 3 COLUMNAS ---
col_left, col_center, col_right = st.columns([1, 1, 1])

# --- LÓGICA DE INTERFAZ ---

with col_left:
    # --- BOTÓN 1: TEXT (Arriba Izquierda) ---
    if st.button("📝 TEXT / EMAIL"):
        with st.container():
            st.markdown('<div class="input-box">', unsafe_allow_html=True)
            txt = st.text_area("Paste suspicious text:", height=150)
            if st.button("Analyze Text"):
                st.warning("Analyzing Syntax & Semantics...")
                time.sleep(2)
                st.success("Analysis Complete: High probability of Phishing.")
            st.markdown('</div>', unsafe_allow_html=True)

    # Espacio para separar
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)

    # --- BOTÓN 2: IMAGE (Abajo Izquierda) ---
    if st.button("🖼️ IMAGE"):
        with st.container():
            st.markdown('<div class="input-box">', unsafe_allow_html=True)
            img = st.file_uploader("Upload Image:", type=['jpg', 'png'])
            if img:
                st.success("Image Loaded. Scanning pixels...")
            st.markdown('</div>', unsafe_allow_html=True)


with col_center:
    # Espacio gigante para empujar el botón VIDEO hasta abajo
    st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
    
    # --- BOTÓN 3: VIDEO (Centro Abajo) ---
    if st.button("🎥 VIDEO"):
        with st.container():
            st.markdown('<div class="input-box">', unsafe_allow_html=True)
            vid = st.file_uploader("Upload Video (MP4):", type=['mp4', 'mov'])
            if vid:
                st.success("Video Loaded. Frame-by-frame analysis...")
            st.markdown('</div>', unsafe_allow_html=True)


with col_right:
    # --- BOTÓN 4: URL (Arriba Derecha) ---
    if st.button("🔗 URL / LINK"):
        with st.container():
            st.markdown('<div class="input-box">', unsafe_allow_html=True)
            url = st.text_input("Paste URL:")
            if st.button("Check Link"):
                st.info("Scanning domain reputation...")
            st.markdown('</div>', unsafe_allow_html=True)

    # Espacio para separar
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)

    # --- BOTÓN 5: AUDIO (Abajo Derecha) ---
    if st.button("🔊 AUDIO"):
        with st.container():
            st.markdown('<div class="input-box">', unsafe_allow_html=True)
            aud = st.file_uploader("Upload Audio:", type=['mp3', 'wav'])
            if aud:
                st.success("Audio Loaded. Checking frequencies...")
            st.markdown('</div>', unsafe_allow_html=True)

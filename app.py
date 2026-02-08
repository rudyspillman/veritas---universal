import streamlit as st
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="VERITAS AI — Universal Verification Engine",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ESTILOS CSS PRINCIPALES ---
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

/* Botones (estructura intacta) */
.stButton > button {{
    width: 100%;
    background-color: rgba(0, 0, 0, 0.7);
    color: #00ffff;
    border: 2px solid #00ffff;
    border-radius: 12px;
    padding: 14px;
    transition: all 0.3s;
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.2);
}}

/* Hover */
.stButton > button:hover {{
    background-color: #00ffff;
    color: black;
    box-shadow: 0 0 20px #00ffff;
}}

/* SOLO texto e íconos x2 */
.stButton > button span {{
    font-size: 26px;
    font-weight: 600;
    letter-spacing: 1px;
}}

/* Cajas de input */
.input-box {{
    background-color: rgba(0, 0, 0, 0.9);
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #555;
    margin-top: 12px;
    margin-bottom: 20px;
}}

</style>
""", unsafe_allow_html=True)

# --- GRILLA PRINCIPAL SIMÉTRICA ---
col_left, col_center, col_right = st.columns([1.2, 0.6, 1.2])

# ===================== IZQUIERDA =====================
with col_left:
    st.markdown("<br>", unsafe_allow_html=True)

    # IMAGE (ocupa lugar anterior de VIDEO)
    if st.button("🖼️ IMAGE"):
        with st.container():
            st.markdown('<div class="input-box">', unsafe_allow_html=True)
            img = st.file_uploader("Upload Image:", type=["jpg", "png"])
            if img:
                st.success("Image loaded. Scanning pixels...")
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # AUDIO (acercado al haz)
    if st.button("🔊 AUDIO"):
        with st.container():
            st.markdown('<div class="input-box">', unsafe_allow_html=True)
            aud = st.file_uploader("Upload Audio:", type=["mp3", "wav"])
            if aud:
                st.success("Audio loaded. Analyzing frequencies...")
            st.markdown("</div>", unsafe_allow_html=True)


# ===================== CENTRO (EJE / HAZ) =====================
with col_center:
    st.markdown("")  # vacío intencional (respeta el haz de luz)


# ===================== DERECHA =====================
with col_right:
    st.markdown("<br>", unsafe_allow_html=True)

    # TEXT / EMAIL (simétrico a URL)
    if st.button("📝 TEXT / EMAIL"):
        with st.container():
            st.markdown('<div class="input-box">', unsafe_allow_html=True)
            txt = st.text_area("Paste suspicious text:", height=150)
            if st.button("Analyze Text"):
                st.warning("Analyzing semantics and intent...")
                time.sleep(2)
                st.success("High probability of phishing detected.")
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # VIDEO (debajo, cercano al eje)
    if st.button("🎥 VIDEO"):
        with st.container():
            st.markdown('<div class="input-box">', unsafe_allow_html=True)
            vid = st.file_uploader("Upload Video:", type=["mp4", "mov"])
            if vid:
                st.success("Video loaded. Frame-by-frame analysis...")
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # URL / LINK (simétrico a TEXT)
    if st.button("🔗 URL / LINK"):
        with st.container():
            st.markdown('<div class="input-box">', unsafe_allow_html=True)
            url = st.text_input("Paste URL:")
            if st.button("Check Link"):
                st.info("Checking domain reputation...")
            st.markdown("</div>", unsafe_allow_html=True)

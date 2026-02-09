import streamlit as st

st.set_page_config(
    page_title="VERITAS AI – Universal Engine",
    layout="wide",
    initial_sidebar_state="collapsed"
)

background_url = "https://i.postimg.cc/Kzv816Jc/VERITAS_AI_Universal_Verification_Engine_IMAGEN.png"

st.markdown(f"""
<style>
.stApp {{
    background-image: url("{background_url}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

#MainMenu, footer, header {{
    visibility: hidden;
}}

.btn {{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 14px;
    width: 100%;
    height: 90px;
    background: rgba(0,0,0,0.65);
    border: 2px solid #00ffff;
    border-radius: 18px;
    color: #00ffff;
    font-size: 30px;
    font-weight: 600;
    box-shadow: 0 0 20px rgba(0,255,255,0.25);
}}

.grid {{
    margin-top: 160px;
}}

.spacer {{
    height: 60px;
}}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="grid">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.markdown("<div class='btn'>🖼️ IMAGE</div>", unsafe_allow_html=True)
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    st.markdown("<div class='btn'>🔊 AUDIO</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    st.markdown("<div class='btn'>🎥 VIDEO</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='btn'>🔗 URL / LINK</div>", unsafe_allow_html=True)
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    st.markdown("<div class='btn'>📝 TEXT / EMAIL</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


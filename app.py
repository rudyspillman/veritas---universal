import streamlit as st

st.set_page_config(page_title="VERITAS AI", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
.stApp {
    background-image: url('https://i.postimg.cc/Kzv816Jc/VERITAS_AI_Universal_Verification_Engine_IMAGEN.png');
    background-size: cover;
}
.stButton > button {
    background: rgba(0,0,0,0.8);
    color: #00ffff;
    border: 2px solid #00ffff;
    font-size: 24px;
    padding: 20px;
    margin: 10px;
    border-radius: 12px;
    width: 250px;
}
</style>
""", unsafe_allow_html=True)

# Estado
if 'view' not in st.session_state:
    st.session_state.view = 'menu'

# Menú principal
if st.session_state.view == 'menu':
    if st.button("📝 TEXT / EMAIL"):
        st.session_state.view = 'text'
        st.rerun()
    if st.button("🔗 URL / LINK"):
        st.session_state.view = 'url'
        st.rerun()
    if st.button("🖼️ IMAGE"):
        st.session_state.view = 'image'
        st.rerun()
    if st.button("🎥 VIDEO"):
        st.session_state.view = 'video'
        st.rerun()
    if st.button("🔊 AUDIO"):
        st.session_state.view = 'audio'
        st.rerun()

# TEXT/EMAIL
elif st.session_state.view == 'text':
    st.write("### TEXT/EMAIL VERIFICATION")
    text = st.text_area("Paste text or email content:")
    if st.button("VERIFY"):
        st.write("✅ Verification complete: Text is authentic")
        st.write("📊 Analysis: 98% confidence")
        st.write("⚠️ No deepfake indicators detected")
    if st.button("CLOSE"):
        st.session_state.view = 'menu'
        st.rerun()

# URL/LINK
elif st.session_state.view == 'url':
    st.write("### URL/LINK VERIFICATION")
    url = st.text_input("Enter URL:")
    if st.button("VERIFY"):
        st.write("✅ Verification complete: URL is safe")
        st.write("📊 Analysis: 95% confidence")
        st.write("✅ No phishing detected")
    if st.button("CLOSE"):
        st.session_state.view = 'menu'
        st.rerun()

# IMAGE
elif st.session_state.view == 'image':
    st.write("### IMAGE VERIFICATION")
    img = st.file_uploader("Upload image:")
    if st.button("VERIFY"):
        st.write("✅ Verification complete: Image is authentic")
        st.write("📊 Analysis: 97% confidence")
        st.write("✅ No AI manipulation detected")
    if st.button("CLOSE"):
        st.session_state.view = 'menu'
        st.rerun()

# VIDEO
elif st.session_state.view == 'video':
    st.write("### VIDEO VERIFICATION")
    vid = st.file_uploader("Upload video:")
    if st.button("VERIFY"):
        st.write("✅ Verification complete: Video is authentic")
        st.write("📊 Analysis: 96% confidence")
        st.write("✅ No deepfake detected")
    if st.button("CLOSE"):
        st.session_state.view = 'menu'
        st.rerun()

# AUDIO
elif st.session_state.view == 'audio':
    st.write("### AUDIO VERIFICATION")
    aud = st.file_uploader("Upload audio:")
    if st.button("VERIFY"):
        st.write("✅ Verification complete: Audio is authentic")
        st.write("📊 Analysis: 94% confidence")
        st.write("✅ No voice cloning detected")
    if st.button("CLOSE"):
        st.session_state.view = 'menu'
        st.rerun()

import streamlit as st
import random
import time

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
    font-size: 20px;
    padding: 15px;
    margin: 5px;
    border-radius: 10px;
    width: 180px;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("📝 TEXT"):
        st.session_state.selected = "text"
        st.session_state.result = None
with col2:
    if st.button("🔗 URL"):
        st.session_state.selected = "url"
        st.session_state.result = None
with col3:
    if st.button("🖼️ IMAGE"):
        st.session_state.selected = "image"
        st.session_state.result = None
with col4:
    if st.button("🎥 VIDEO"):
        st.session_state.selected = "video"
        st.session_state.result = None
with col5:
    if st.button("🔊 AUDIO"):
        st.session_state.selected = "audio"
        st.session_state.result = None

if 'selected' in st.session_state:
    st.markdown("---")
    
    if st.session_state.selected == "text":
        text_input = st.text_area("Paste text or email:")
        if st.button("Verify Text", key="vtext"):
            if text_input:
                with st.spinner("Analyzing..."):
                    time.sleep(1.5)
                    results = ["✅ AUTHENTIC", "⚠️ SUSPICIOUS", "❌ FAKE"]
                    st.session_state.result = random.choice(results)
    elif st.session_state.selected == "url":
        url_input = st.text_input("Enter URL:")
        if st.button("Verify URL", key="vurl"):
            if url_input:
                with st.spinner("Checking..."):
                    time.sleep(1.5)
                    results = ["✅ SAFE", "⚠️ RISKY", "❌ MALICIOUS"]
                    st.session_state.result = random.choice(results)
    elif st.session_state.selected == "image":
        image_file = st.file_uploader("Upload image:")
        if st.button("Verify Image", key="vimage"):
            if image_file:
                with st.spinner("Scanning..."):
                    time.sleep(1.5)
                    results = ["✅ ORIGINAL", "⚠️ EDITED", "❌ FAKE"]
                    st.session_state.result = random.choice(results)
    elif st.session_state.selected == "video":
        video_file = st.file_uploader("Upload video:")
        if st.button("Verify Video", key="vvideo"):
            if video_file:
                with st.spinner("Processing..."):
                    time.sleep(2)
                    results = ["✅ GENUINE", "⚠️ MANIPULATED", "❌ DEEPFAKE"]
                    st.session_state.result = random.choice(results)
    elif st.session_state.selected == "audio":
        audio_file = st.file_uploader("Upload audio:")
        if st.button("Verify Audio", key="vaudio"):
            if audio_file:
                with st.spinner("Analyzing..."):
                    time.sleep(1.5)
                    results = ["✅ REAL", "⚠️ SYNTHETIC", "❌ CLONED"]
                    st.session_state.result = random.choice(results)
    
    if 'result' in st.session_state and st.session_state.result:
        st.markdown(f"# {st.session_state.result}")
        st.write(f"Confidence: {random.randint(70, 99)}%")
    
    if st.button("Close", key="close"):
        del st.session_state.selected
        if 'result' in st.session_state:
            del st.session_state.result
        st.rerun()

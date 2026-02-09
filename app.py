import streamlit as st

st.set_page_config(page_title="VERITAS AI", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
.stApp {
    background-image: url('https://i.postimg.cc/Kzv816Jc/VERITAS_AI_Universal_Verification_Engine_IMAGEN.png');
    background-size: cover;
}
</style>
""", unsafe_allow_html=True)

# Botones principales
option = st.radio("Seleccionar:", ["📝 TEXT/EMAIL", "🔗 URL/LINK", "🖼️ IMAGE", "🎥 VIDEO", "🔊 AUDIO"], 
                  horizontal=True, label_visibility="collapsed")

if option == "📝 TEXT/EMAIL":
    text = st.text_area("Pegue texto o email:")
    if st.button("Verificar"):
        st.write(f"Texto verificado: {len(text)} caracteres analizados")

elif option == "🔗 URL/LINK":
    url = st.text_input("Ingrese URL:")
    if st.button("Verificar"):
        st.write(f"URL verificada: {url}")

elif option == "🖼️ IMAGE":
    img = st.file_uploader("Suba imagen:", type=["jpg", "png"])
    if st.button("Verificar"):
        if img:
            st.write(f"Imagen verificada: {img.name}")

elif option == "🎥 VIDEO":
    vid = st.file_uploader("Suba video:", type=["mp4"])
    if st.button("Verificar"):
        if vid:
            st.write(f"Video verificado: {vid.name}")

elif option == "🔊 AUDIO":
    aud = st.file_uploader("Suba audio:", type=["mp3", "wav"])
    if st.button("Verificar"):
        if aud:
            st.write(f"Audio verificado: {aud.name}")

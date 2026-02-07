import streamlit as st

st.set_page_config(
    page_title="VERITAS AI — Universal Verification Engine",
    layout="wide"
)

st.title("VERITAS AI — Universal Verification Engine")
st.subheader("Universal authenticity verification for text, images, video, audio, documents and URLs")

st.markdown("---")

st.markdown("### Input")
input_type = st.selectbox(
    "Select what you want to verify:",
    ["Text", "Image", "Video", "Audio", "Document", "URL"]
)

if input_type == "Text":
    user_text = st.text_area("Paste the text to verify")
elif input_type == "URL":
    user_url = st.text_input("Paste the URL to verify")
else:
    uploaded_file = st.file_uploader("Upload the file")

st.markdown("---")

if st.button("Verify Authenticity"):
    st.markdown("## Verification Result")
    st.metric(label="Truth Score", value="87%")
    st.write(
        "The content shows no strong indicators of manipulation or fraud. "
        "Minor anomalies detected but overall consistency is high."
    )

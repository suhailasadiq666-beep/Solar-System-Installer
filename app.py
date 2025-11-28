import streamlit as st

DOWNLOAD_URL_ALPHA = "https://github.com/suhailasadiq666-beep/Solar-System-Installer/releases/download/nima/Solar.System.exe" 
DOWNLOAD_URL_BETA = "https://github.com/suhailasadiq666-beep/Solar-System-Installer/releases/download/nima/Solar.System.Installer.exe" 

st.set_page_config(page_title="Solar System Game Download")
st.title("Download Solar System")

if st.button("Install Solarsytem Alpha"):
    js = f"window.open('{DOWNLOAD_URL_ALPHA}')"
    html = f"<img src onerror=\"{js}\">"
    st.markdown(html, unsafe_allow_html=True)
if st.button("Install Solarsytem Beta"):
    js = f"window.open('{DOWNLOAD_URL_BETA}')"
    html = f"<img src onerror=\"{js}\">"
    st.markdown(html, unsafe_allow_html=True)

import streamlit as st
from PIL import Image
from utils import add_bg_with_overlay
import os

PROFILE_PIC = "PROFILE_PIC.jpg"
CV_FILE = "CV_AlfredMalinga.pdf"

st.set_page_config(page_title="About - Alfred Malinga", page_icon="👤", layout="wide")
add_bg_with_overlay("background_image.png", opacity=0.4)

col1, col2 = st.columns([1,3])
with col1:
    if os.path.exists(PROFILE_PIC):
        st.image(Image.open(PROFILE_PIC), width=160)
with col2:
    st.header("Alfred Sakhile Malinga")
    st.write("Computer Science graduate with experience across IT support, software development, and data analytics...")
    if os.path.exists(CV_FILE):
        with open(CV_FILE, "rb") as f:
            st.download_button("📄 Download CV", f.read(), file_name=CV_FILE, mime="application/pdf")

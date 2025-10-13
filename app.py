import streamlit as st
from utils import add_bg_with_overlay, inject_navbar

st.set_page_config(page_title="Alfred Malinga - CV", page_icon="📄", layout="wide")


add_bg_with_overlay("background_image.png", opacity=0.4)
inject_navbar(active="About")

st.title("Welcome to My CV App")
st.write("Use the navbar above to navigate through my profile.")

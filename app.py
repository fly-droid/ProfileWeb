import streamlit as st
from utils import add_bg_with_overlay

st.set_page_config(page_title="Alfred Malinga - CV", page_icon="📄", layout="wide")
add_bg_with_overlay("background_image.png", opacity=0.4)

st.title("Welcome to My CV App")
st.write("Use the sidebar to navigate through my profile: About, Skills, Experience, Projects, and Contact.")

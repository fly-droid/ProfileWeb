import streamlit as st
from utils import add_bg_with_overlay

st.set_page_config(page_title="Skills - Alfred Malinga", page_icon="🛠️", layout="wide")
add_bg_with_overlay("background_image.png", opacity=0.4)

st.header("🛠️ Skills")

skills = ["Python", "SQL", "R", "Pandas", "NumPy", "Docker", "AWS", "Azure", "PostgreSQL", "MongoDB"]
cols = st.columns(5)
for i, skill in enumerate(skills):
    with cols[i % 5]:
        st.markdown(f"✅ {skill}")

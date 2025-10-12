import streamlit as st
from utils import add_bg_with_overlay

st.set_page_config(page_title="Experience - Alfred Malinga", page_icon="💼", layout="wide")
add_bg_with_overlay("background_image.png", opacity=0.4)

st.header("💼 Experience")

st.subheader("System Developer Trainee — Mindworx Consulting (2023 – Present)")
st.write("Assisted in backend development and CRM customization...")

st.subheader("Software Developer Intern — UNITAP (PTY) LTD (2022 – 2023)")
st.write("Contributed to e-commerce platform development using Python and SQL...")

st.subheader("Data Analyst — Dry Dock Liquor (2021 – 2022)")
st.write("Designed Power BI dashboards to track sales and inventory trends...")

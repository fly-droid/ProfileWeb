import streamlit as st, base64, os

def add_bg_with_overlay(image_file, opacity=0.4):
    if not os.path.exists(image_file):
        return
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,{opacity}), rgba(0,0,0,{opacity})),
                        url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .block-container {{ padding-top: 60px !important; }}
        </style>
        """,
        unsafe_allow_html=True
    )

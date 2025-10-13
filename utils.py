import streamlit as st
import base64, os


def add_bg_with_overlay(image_file, opacity=0.4):
    """Adds a background image with dark overlay."""
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
        .block-container {{ padding-top: 80px !important; }}
        </style>
        """,
        unsafe_allow_html=True
    )

def inject_navbar(active="About"):
    """Injects a GitHub-style top navbar with active link highlighting."""
    hide_st_style = """
            <style>
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    
    pages = ["About", "Skills", "Experience", "Projects", "Contact"]
    icons = {
        "About": "fa-user",
        "Skills": "fa-code",
        "Experience": "fa-briefcase",
        "Projects": "fa-rocket",
        "Contact": "fa-envelope"
    }

    links = ""
    for page in pages:
        cls = "active" if page == active else ""
        links += f'<a href="/{page}" class="{cls}"><i class="fas {icons[page]}"></i> {page}</a>'

    st.markdown(f"""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
    .navbar {{
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: rgba(26,26,26,0.9);
        padding: 12px;
        position: fixed;
        top: 0; left: 0; width: 100%;
        z-index: 9999;
        box-shadow: 0 4px 8px rgba(0,0,0,0.4);
    }}
    .navbar a {{
        color: #e0e0e0;
        text-decoration: none;
        padding: 10px 18px;
        font-weight: 500;
        transition: background 0.3s, color 0.3s;
        border-radius: 6px;
        margin: 0 6px;
    }}
    .navbar a:hover {{
        background: #14ffec;
        color: #1a1a1a;
    }}
    .navbar a.active {{
        background: #0d7377;
        color: #fff;
    }}
    </style>
    <div class="navbar">{links}</div>
    """, unsafe_allow_html=True)

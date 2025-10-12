import streamlit as st
from utils import add_bg_with_overlay

st.set_page_config(page_title="Contact - Alfred Malinga", page_icon="📧", layout="wide")
add_bg_with_overlay("background_image.png", opacity=0.4)

st.header("📧 Get In Touch")

contact_form = f"""
<form action="https://formsubmit.co/{'alfredmalinga629@gmail.com'}" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

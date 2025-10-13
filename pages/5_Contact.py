import streamlit as st
from utils import add_bg_with_overlay, inject_navbar

st.set_page_config(page_title="Contact - Alfred Malinga", page_icon="📧", layout="wide")

# Apply background and navbar
add_bg_with_overlay("background_image.png", opacity=0.4)
inject_navbar(active="Contact")

st.header("📧 Get In Touch")

contact_html = """
<style>
.contact-card {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 12px;
  padding: 30px;
  max-width: 640px;
  margin: 30px auto;
  box-shadow: 0 4px 12px rgba(0,0,0,0.4);
}
.contact-card h3 {
  color: #14ffec;
  margin-bottom: 15px;
  text-align: center;
}
.contact-card form {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.contact-card input, .contact-card textarea {
  width: 100%;
  padding: 12px;
  border-radius: 6px;
  border: 1px solid #333;
  background: #111;
  color: #eee;
  font-size: 14px;
}
.contact-card button {
  background-color: #0d7377;
  color: white;
  padding: 12px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
  transition: background-color 0.3s ease, color 0.3s ease;
}
.contact-card button:hover {
  background-color: #14ffec;
  color: #1a1a1a;
}
.contact-links {
  display: flex; gap: 14px; justify-content: center; margin-top: 12px;
}
.contact-links a {
  color: #e0e0e0; font-size: 20px; text-decoration: none;
}
.contact-links a:hover { color: #14ffec; }
</style>

<div class="contact-card">
  <h3>Send me a message</h3>
  <form action="https://formsubmit.co/alfredmalinga629@gmail.com" method="POST">
      <input type="hidden" name="_captcha" value="false">
      <input type="text" name="name" placeholder="Your name" required>
      <input type="email" name="email" placeholder="Your email" required>
      <textarea name="message" rows="5" placeholder="Your message here" required></textarea>
      <button type="submit">Send</button>
  </form>
  <div class="contact-links">
    <a href="mailto:alfredmalinga629@gmail.com" title="Email"><i class="fas fa-envelope"></i></a>
    <a href="https://www.linkedin.com/in/alfredsakhilemalinga" target="_blank" title="LinkedIn"><i class="fab fa-linkedin"></i></a>
    <a href="https://github.com/alfredsakhilemalinga" target="_blank" title="GitHub"><i class="fab fa-github"></i></a>
  </div>
</div>
"""
st.markdown(contact_html, unsafe_allow_html=True)

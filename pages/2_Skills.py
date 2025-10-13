import streamlit as st
from utils import add_bg_with_overlay, inject_navbar

st.set_page_config(page_title="Skills - Alfred Malinga", page_icon="🛠️", layout="wide")
add_bg_with_overlay("background_image.png", opacity=0.4)
inject_navbar(active="Skills")

st.header("🛠️ Skills")

skills_html = """
<style>
.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 20px;
  margin-top: 20px;
}
.skill-card {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 12px;
  padding: 20px 10px;
  text-align: center;
  transition: transform 0.2s ease, background 0.2s ease;
}
.skill-card:hover { transform: translateY(-6px); background: rgba(20,255,236,0.12); }
.skill-icon { height: 40px; margin-bottom: 10px; }
.skill-label { font-size: 14px; font-weight: 600; color: #fff; }
</style>

<div class="skills-grid">
  <div class="skill-card"><img class="skill-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"/><div class="skill-label">Python</div></div>
  <div class="skill-card"><img class="skill-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg"/><div class="skill-label">SQL</div></div>
  <div class="skill-card"><img class="skill-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/r/r-original.svg"/><div class="skill-label">R</div></div>
  <div class="skill-card"><img class="skill-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg"/><div class="skill-label">Pandas</div></div>
  <div class="skill-card"><img class="skill-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg"/><div class="skill-label">NumPy</div></div>
  <div class="skill-card"><img class="skill-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg"/><div class="skill-label">Docker</div></div>
  <div class="skill-card"><img class="skill-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original.svg"/><div class="skill-label">AWS</div></div>
  <div class="skill-card"><img class="skill-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/azure/azure-original.svg"/><div class="skill-label">Azure</div></div>
  <div class="skill-card"><img class="skill-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg"/><div class="skill-label">PostgreSQL</div></div>
  <div class="skill-card"><img class="skill-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg"/><div class="skill-label">MongoDB</div></div>
</div>
"""
st.markdown(skills_html, unsafe_allow_html=True)

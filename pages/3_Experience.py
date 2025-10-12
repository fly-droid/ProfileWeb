import streamlit as st
from utils import add_bg_with_overlay

st.set_page_config(page_title="Experience - Alfred Malinga", page_icon="💼", layout="wide")
add_bg_with_overlay("background_image.png", opacity=0.4)

st.header("💼 Experience")

experience_html = """
<style>
.experience-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-top: 20px;
}
.experience-card {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 12px;
  padding: 20px;
  transition: transform 0.2s ease, background 0.2s ease;
}
.experience-card:hover {
  transform: translateY(-4px);
  background: rgba(20,255,236,0.08);
}
.exp-role { font-size: 18px; font-weight: 700; color: #14ffec; margin-bottom: 4px; }
.exp-company { font-size: 15px; font-weight: 600; color: #fff; margin-bottom: 6px; }
.exp-dates { font-size: 13px; font-style: italic; color: #ccc; margin-bottom: 10px; }
.exp-desc { font-size: 14px; line-height: 1.5; color: #e0e0e0; }
</style>

<div class="experience-container">
  <div class="experience-card">
    <div class="exp-role">System Developer Trainee</div>
    <div class="exp-company">Mindworx Consulting</div>
    <div class="exp-dates">2023 – Present</div>
    <div class="exp-desc">Assisted in backend development and CRM customization...</div>
  </div>
  <div class="experience-card">
    <div class="exp-role">Software Developer Intern</div>
    <div class="exp-company">UNITAP (PTY) LTD</div>
    <div class="exp-dates">2022 – 2023</div>
    <div class="exp-desc">Contributed to e-commerce platform development using Python and SQL...</div>
  </div>
  <div class="experience-card">
    <div class="exp-role">Data Analyst</div>
    <div class="exp-company">Dry Dock Liquor</div>
    <div class="exp-dates">2021 – 2022</div>
    <div class="exp-desc">Designed Power BI dashboards to track sales and inventory trends...</div>
  </div>
</div>
"""
st.markdown(experience_html, unsafe_allow_html=True)

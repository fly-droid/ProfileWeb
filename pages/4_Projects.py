import streamlit as st
from utils import add_bg_with_overlay, inject_navbar

st.set_page_config(page_title="Projects - Alfred Malinga", page_icon="🚀", layout="wide")
add_bg_with_overlay("background_image.png", opacity=0.4)
inject_navbar(active="Projects")

st.header("🚀 Projects")

projects_html = """
<style>
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  margin-top: 20px;
}
.project-card {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  height: 200px;
  color: white;
  box-shadow: 0 4px 10px rgba(0,0,0,0.4);
  transition: transform 0.3s ease;
  text-decoration: none;
}
.project-card:hover { transform: translateY(-6px); }
.project-bg {
  position: absolute; top: 0; left: 0; width: 100%; height: 100%;
  background-size: cover; background-position: center; filter: brightness(0.6);
}
.project-content {
  position: relative; z-index: 2; padding: 20px;
}
.project-title { font-size: 18px; font-weight: 700; margin-bottom: 6px; color: #14ffec; }
.project-desc { font-size: 14px; line-height: 1.4; color: #f0f0f0; }
</style>

<div class="projects-grid">
  <a class="project-card" href="https://github.com/alfredsakhilemalinga/ecommerce-predictor" target="_blank">
    <div class="project-bg" style="background-image: url('https://images.unsplash.com/photo-1523275335684-37898b6baf30');"></div>
    <div class="project-content">
      <div class="project-title">E-commerce Sales Predictor</div>
      <div class="project-desc">End-to-end predictive model for sales forecasting using Python, XGBoost, Streamlit, and PostgreSQL.</div>
    </div>
  </a>
  <a class="project-card" href="https://github.com/alfredsakhilemalinga/customer-segmentation" target="_blank">
    <div class="project-bg" style="background-image: url('https://images.unsplash.com/photo-1556740749-887f6717d7e4');"></div>
    <div class="project-content">
      <div class="project-title">Customer Segmentation</div>
      <div class="project-desc">Automated clustering of customers using R and K-Means, visualized with Tableau dashboards.</div>
    </div>
  </a>
  <a class="project-card" href="https://github.com/alfredsakhilemalinga/quality-control-ai" target="_blank">
    <div class="project-bg" style="background-image: url('https://images.unsplash.com/photo-1581090700227-4c4f50b1d1f2');"></div>
    <div class="project-content">
      <div class="project-title">Image Recognition for Quality Control</div>
      <div class="project-desc">Deep learning model using PyTorch and transfer learning to detect defects in manufacturing.</div>
    </div>
  </a>
</div>
"""
st.markdown(projects_html, unsafe_allow_html=True)

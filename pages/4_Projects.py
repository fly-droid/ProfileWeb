import streamlit as st
from utils import add_bg_with_overlay

st.set_page_config(page_title="Projects - Alfred Malinga", page_icon="🚀", layout="wide")
add_bg_with_overlay("background_image.png", opacity=0.4)

st.header("🚀 Projects")

st.markdown("### [E-commerce Sales Predictor](https://github.com/alfredsakhilemalinga/ecommerce-predictor)")
st.write("End-to-end predictive model for sales forecasting using Python, XGBoost, Streamlit, and PostgreSQL.")

st.markdown("### [Customer Segmentation](https://github.com/alfredsakhilemalinga/customer-segmentation)")
st.write("Automated clustering of customers using R and K-Means, visualized with Tableau dashboards.")

st.markdown("### [Image Recognition for Quality Control](https://github.com/alfredsakhilemalinga/quality-control-ai)")
st.write("Deep learning model using PyTorch and transfer learning to detect defects in manufacturing.")

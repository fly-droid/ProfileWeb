import streamlit as st
from streamlit_option_menu import option_menu
from utils import add_bg_with_overlay
from PIL import Image
import os

# 1. Page Config (Run once for the whole app)
st.set_page_config(page_title="Alfred Malinga - CV",
                   page_icon="📄", layout="wide")

# 2. Background
add_bg_with_overlay("background_image.png", opacity=0.4)

# 3. CSS Media Queries for Responsive Swap (Top on Desktop, Side on Mobile)
st.markdown("""
    <style>
    /* Remove default top padding */
    .block-container {
        padding-top: 0rem !important;
    }

    /* --- DESKTOP VIEW (Larger than 768px) --- */
    @media screen and (min-width: 769px) {
        /* Hide the Streamlit Sidebar and Hamburger button */
        [data-testid="stSidebar"] { display: none !important; }
        [data-testid="collapsedControl"] { display: none !important; }
        /* Hide default header spacing */
        [data-testid="stHeader"] { display: none !important; }
    }

    /* --- MOBILE VIEW (768px or smaller) --- */
    @media screen and (max-width: 768px) {
        /* Hide the top navbar iframe so it doesn't duplicate */
        .block-container iframe {
            display: none !important;
        }
        /* Show the default Streamlit header so the hamburger icon is visible */
        [data-testid="stHeader"] {
            display: block !important;
            background: transparent !important;
        }
        /* Add slight padding so content isn't hidden behind the hamburger icon */
        .block-container {
            padding-top: 3rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# 4. State Management (To keep both menus in sync)
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "About"

# 5. Define content functions


def show_about():
    col1, col2 = st.columns([1, 3])
    with col1:
        if os.path.exists("PROFILE_PIC.png"):
            st.image(Image.open("PROFILE_PIC.png"), width=160)
    with col2:
        st.header("Alfred Sakhile Malinga")
        st.write(
            "Computer Science graduate with experience across IT support, software development, and data analytics...")
        if os.path.exists("CV_AlfredMalinga.pdf"):
            with open("CV_AlfredMalinga.pdf", "rb") as f:
                st.download_button("📄 Download CV", f.read(
                ), file_name="CV_AlfredMalinga.pdf", mime="application/pdf")


def show_skills():
    st.header("🛠️ Skills")
    skills_html = """
    <style>
    .skills-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 20px; margin-top: 20px; }
    .skill-card { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.15); border-radius: 12px; padding: 20px 10px; text-align: center; transition: transform 0.2s ease, background 0.2s ease; }
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


def show_experience():
    st.header("💼 Experience")
    experience_html = """
    <style>
    .experience-container { display: flex; flex-direction: column; gap: 20px; margin-top: 20px; }
    .experience-card { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.15); border-radius: 12px; padding: 20px; transition: transform 0.2s ease, background 0.2s ease; }
    .experience-card:hover { transform: translateY(-4px); background: rgba(20,255,236,0.08); }
    .exp-role { font-size: 18px; font-weight: 700; color: #14ffec; margin-bottom: 4px; }
    .exp-company { font-size: 15px; font-weight: 600; color: #fff; margin-bottom: 6px; }
    .exp-dates { font-size: 13px; font-style: italic; color: #ccc; margin-bottom: 10px; }
    .exp-desc { font-size: 14px; line-height: 1.5; color: #e0e0e0; }
    </style>
    <div class="experience-container">
      <div class="experience-card">
        <div class="exp-role">System Developer Trainee</div>
        <div class="exp-company">Mindworx Consulting</div>
        <div class="exp-desc">Assisted in backend development and CRM customization, improving system efficiency and client workflows.</div>
      </div>
      <div class="experience-card">
        <div class="exp-role">Software Developer Intern</div>
        <div class="exp-company">UNITAP (PTY) LTD</div>
        <div class="exp-desc">Contributed to e-commerce platform development using Python and SQL, focusing on payment integration and data pipelines.</div>
      </div>
      <div class="experience-card">
        <div class="exp-role">Data Analyst</div>
        <div class="exp-company">Dry Dock Liquor</div>
        <div class="exp-desc">Designed Power BI dashboards to track sales and inventory trends, enabling data-driven decision-making.</div>
      </div>
    </div>
    """
    st.markdown(experience_html, unsafe_allow_html=True)


def show_projects():
    st.header("🚀 Projects")
    projects_html = """
    <style>
    .projects-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 20px; }
    .project-card { position: relative; border-radius: 12px; overflow: hidden; height: 200px; color: white; box-shadow: 0 4px 10px rgba(0,0,0,0.4); transition: transform 0.3s ease; text-decoration: none; }
    .project-card:hover { transform: translateY(-6px); }
    .project-bg { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-size: cover; background-position: center; filter: brightness(0.6); }
    .project-content { position: relative; z-index: 2; padding: 20px; }
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


def show_contact():
    st.header("📧 Get In Touch")
    contact_html = """
    <style>
    .contact-card { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.15); border-radius: 12px; padding: 30px; max-width: 640px; margin: 30px auto; box-shadow: 0 4px 12px rgba(0,0,0,0.4); }
    .contact-card h3 { color: #14ffec; margin-bottom: 15px; text-align: center; }
    .contact-card form { display: flex; flex-direction: column; gap: 12px; }
    .contact-card input, .contact-card textarea { width: 100%; padding: 12px; border-radius: 6px; border: 1px solid #333; background: #111; color: #eee; font-size: 14px; }
    .contact-card button { background-color: #0d7377; color: white; padding: 12px; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; transition: background-color 0.3s ease, color 0.3s ease; }
    .contact-card button:hover { background-color: #14ffec; color: #1a1a1a; }
    .contact-links { display: flex; gap: 14px; justify-content: center; margin-top: 12px; }
    .contact-links a { color: #e0e0e0; font-size: 20px; text-decoration: none; }
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


# 6. Render TOP MENU (Visible ONLY on Desktop)
top_selected = option_menu(
    menu_title=None,
    options=["About", "Skills", "Experience", "Projects", "Contact"],
    icons=["person", "code-slash", "briefcase", "rocket", "envelope"],
    default_index=["About", "Skills", "Experience", "Projects",
                   "Contact"].index(st.session_state.active_tab),
    orientation="horizontal",
    key="top_menu_key",
    styles={
        "container": {"padding": "10px 0px", "margin": "0px", "max-width": "100%", "background-color": "rgba(26,26,26,0.95)", "border-radius": "0px", "box-shadow": "0 4px 8px rgba(0,0,0,0.4)"},
        "icon": {"color": "#e0e0e0", "font-size": "18px"},
        "nav-link": {"color": "#e0e0e0", "font-size": "15px", "text-align": "center", "margin": "0px 5px", "--hover-color": "#14ffec"},
        "nav-link-selected": {"background-color": "#0d7377", "color": "white"},
    }
)

# 7. Render SIDE MENU (Visible ONLY on Mobile)
with st.sidebar:
    side_selected = option_menu(
        menu_title="Main Menu",
        options=["About", "Skills", "Experience", "Projects", "Contact"],
        icons=["person", "code-slash", "briefcase", "rocket", "envelope"],
        default_index=["About", "Skills", "Experience", "Projects",
                       "Contact"].index(st.session_state.active_tab),
        orientation="vertical",
        key="side_menu_key",
        styles={
            "container": {"padding": "5px", "background-color": "transparent"},
            "icon": {"color": "#14ffec", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px 0px", "--hover-color": "rgba(20,255,236,0.1)"},
            "nav-link-selected": {"background-color": "#0d7377", "color": "white"},
        }
    )

# 8. Sync Logic (Check which menu the user clicked and update state)
if top_selected != st.session_state.active_tab:
    st.session_state.active_tab = top_selected
    st.rerun()
elif side_selected != st.session_state.active_tab:
    st.session_state.active_tab = side_selected
    st.rerun()

# 9. Route to the correct view instantly
current_page = st.session_state.active_tab

if current_page == "About":
    show_about()
elif current_page == "Skills":
    show_skills()
elif current_page == "Experience":
    show_experience()
elif current_page == "Projects":
    show_projects()
elif current_page == "Contact":
    show_contact()

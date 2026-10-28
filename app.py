import streamlit as st
import pandas as pd
from datetime import datetime

# ---------- PAGE CONFIGURATION ----------
st.set_page_config(
    page_title="Mary Rose Pacina | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- CUSTOM CSS (Fattah Theme + Minimal Tech Grid) ----------
st.markdown("""
<style>
    /* Pitch black background with subtle dot grid */
    .stApp {
        background-color: #000000;
        background-image: radial-gradient(#27272a 1px, transparent 1px);
        background-size: 32px 32px;
    }
    
    /* Hide default Streamlit headers and footers */
    header[data-testid="stHeader"] {background: transparent;}
    footer {visibility: hidden;}
    
    /* Typography Overrides */
    h1, h2, h3 { color: #f4f4f5 !important; font-weight: 700 !important; }
    p, li { color: #a1a1aa !important; }
    
    /* Minimalist Navigation Bar */
    .nav {
        display: flex; gap: 32px; justify-content: center; 
        padding: 20px 0 40px 0; border-bottom: 1px solid #27272a;
        margin-bottom: 40px;
    }
    .nav a { color: #a1a1aa !important; text-decoration: none; font-weight: 500; font-size: 0.95rem; transition: 0.2s;}
    .nav a:hover { color: #f4f4f5 !important; }
    
    /* Hero Section Text Gradient */
    .hero {
        font-size: 3.8rem; font-weight: 800; line-height: 1.1; margin-bottom: 16px;
        background: linear-gradient(90deg, #ffffff, #71717a);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }

    /* Minimal Card Styling */
    .portfolio-card {
        background-color: #0d0d12;
        border: 1px solid #1e1e2a;
        border-radius: 20px;
        padding: 28px;
        margin-bottom: 24px;
    }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 20px;
    }

    /* Tab Label Styling */
    button[data-baseweb="tab"] p,
    button[data-baseweb="tab"] {
        font-size: 300rem !important;
        font-weight: 600 !important;
    }

    /* Grid layout for tech icons */
    .tech-grid {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 20px 16px;
        align-items: center;
        justify-items: center;
    }

    @media (max-width: 768px) {
        .tech-grid { grid-template-columns: repeat(3, 1fr); }
    }

    /* Icon styling with hover effect and white monochrome filter */
    .tech-item {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 60px;
        height: 60px;
        background: #14141b;
        border: 1px solid #272736;
        border-radius: 14px;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .tech-item:hover {
        transform: translateY(-4px);
        border-color: #a78bfa;
    }

    .tech-icon {
        width: 30px;
        height: 30px;
        object-fit: contain;
        filter: brightness(0) invert(1);
        opacity: 0.85;
    }
</style>

<div class="nav">
    <a href="#about" target="_self">About</a>
    <a href="#autobiography" target="_self">Autobiography</a>
    <a href="#skills" target="_self">Skills</a>
    <a href="#projects" target="_self">Projects</a>
    <a href="#contact" target="_self">Contact</a>
</div>
""", unsafe_allow_html=True)

# ---------- SESSION STATE FOR INTERACTIVITY ----------
if "likes" not in st.session_state:
    st.session_state.likes = 0
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- HERO SECTION ----------
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
c1, c2 = st.columns([2, 1], gap="large")

with c1:
    st.markdown('<div class="hero">Hi, I\'m Mary Rose.</div>', unsafe_allow_html=True)
    st.markdown("**BS Computer Science · 3rd Year · Cebu Institute of Technology – University**")
    st.write(
        "I'm a Cebu-based Computer Science student specializing in full-stack web engineering, "
        "applied AI, object-oriented architecture, and IoT systems. From analyzing machine learning "
        "voice classification models and developing Django healthcare backends to building C# desktop tools "
        "and DOST-awarded IoT buoys, I design software that delivers real-world impact."
    )
    
    if st.button("👍 Like my work"):
        st.session_state.likes += 1
        st.toast("Thanks for the support!", icon="✨")
    st.caption(f"{st.session_state.likes} people liked this portfolio.")

with c2:
    st.image("picture1.jpeg", caption="Mary Rose T. Pacina") 

st.divider()

# ---------- AUTOBIOGRAPHY (5 TABS INCLUDING RESEARCHES) ----------
st.markdown('<div id="autobiography"></div>', unsafe_allow_html=True)
st.header("Autobiography")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Background", "Education", "Leadership & Awards", "Milestones", "Researches"])

with tab1:
    st.write(
        "I grew up on Bantayan Island, Cebu, where I graduated as Elementary Batch Valedictorian "
        "and completed STEM at Bantayan Science High School with Highest Honors. "
        "Currently based in San Isidro, Talisay City while studying at CIT-U, my passion lies in using technology "
        "to solve local community challenges—ranging from sari-sari store inventory tracking to marine sanctuary security."
    )

with tab2:
    st.markdown("**2024 – Present**")
    st.markdown("**Cebu Institute of Technology – University (CIT-U)**\n*Bachelor of Science in Computer Science (Expected 2028)*")
    st.write("Coursework: Applied AI, OOP, Data Structures & Algorithms, Design & Analysis of Algorithms, Information Management.")
    st.markdown("**May 2024**")
    st.markdown("**Bantayan Science High School**\n*STEM Strand · Graduated With Highest Honors*")

with tab3:
    st.markdown("**Key Recognitions:**")
    st.write("• **7th DOST Imake.wemake Competition (2024):** Top 20 Finalist & C&E Adaptive Learning Solutions (CEALS) Arduino Science Kreators Awardee.")
    st.write("• **Regional Science & Technology Fair (2023):** 4th Placer (Tuklas-Physical Science Category).")
    st.write("• **Division Festival of Talents (2023):** 1st Placer STEMazing & Regional Finalist.")
    st.markdown("**Leadership Roles:**")
    st.write("• **CIT-U Technologian Leaders Academy (TLA):** Season 13 Delegate (2024–2025).")
    st.write("• **BSHS Supreme Secondary Learner Government:** President (2023–2024).")
    st.write("• **Bantayan Municipality VAWC:** Student Youth Representative (2023–2024).")

with tab4:
    year = st.select_slider(
        "Slide through my recent milestones",
        options=["2023", "2024", "2025", "2026"],
        value="2026"
    )
    if year == "2023":
        st.success("**2023:** Awarded 1st place in Division STEMazing competition and led the Science Club as President.")
    elif year == "2024":
        st.success("**2024:** Named Top 20 Finalist & CEALS Awardee at DOST Imake.wemake for Project Bassa (C++/IoT Buoy).")
    elif year == "2025":
        st.success("**2025:** Engineered SariSariSmart, a Java & MySQL POS and inventory management system capstone.")
    elif year == "2026":
        st.success("**2026:** Conducted Applied AI voice classification research and developed ALAGA (Django).")

with tab5:
    # Summary Card for Research
    with st.container(border=True):
        st.subheader("Can A Voice Reveal Parkinson’s? Classifying & Clustering Speech Measurements")
        st.caption("**Course:** CS365-F2 (Applied AI) | **Authors:** Chloe Julia Geonzon, Iren Nathaleigh Guinita, Mary Rose Pacina")
        st.write(
            "An applied AI research study analyzing 22 acoustic voice features across 32 subjects (195 recordings) "
            "to evaluate whether machine learning classification and unsupervised K-Means clustering can detect "
            "Parkinson's Disease without voice-data leakage."
        )
        st.markdown("**Methodology:** Logistic Regression, Decision Tree, Random Forest, SVM (RBF), PCA, K-Means Clustering")
        
        # Native Expander for Deep Dive Metrics & Charts
        with st.expander("📊 View Detailed Research Metrics & Charts"):
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Voice Recordings", "195", "6 per person")
            m2.metric("Speakers Studied", "32", "25% Healthy / 75% PD")
            m3.metric("Voice Features", "22", "Pitch, Jitter, Shimmer, PPE")
            m4.metric("Best Specificity", "0.470", "Logistic Regression")

            st.write("---")
            
            # Interactive Chart Toggle
            metric_view = st.radio(
                "Select Metric to Visualize:",
                options=["Balanced Accuracy", "Accuracy", "Recall (PD Sensitivity)", "Specificity (Healthy Detection)"],
                horizontal=True,
                key="research_tab_radio"
            )

            # Dataset from research presentation
            model_results = pd.DataFrame({
                "Model": ["Always-PD Baseline", "Logistic Regression", "Decision Tree", "Random Forest", "SVM (RBF)"],
                "Accuracy": [0.756, 0.702, 0.694, 0.726, 0.673],
                "Balanced Accuracy": [0.500, 0.617, 0.590, 0.592, 0.591],
                "Recall (PD Sensitivity)": [1.000, 0.763, 0.797, 0.848, 0.738],
                "Specificity (Healthy Detection)": [0.000, 0.470, 0.380, 0.380, 0.440]
            })

            r_col1, r_col2 = st.columns([1.2, 0.8], gap="large")

            with r_col1:
                st.subheader(f"Model Comparison: {metric_view}")
                chart_data = model_results.set_index("Model")[[metric_view]]
                st.bar_chart(chart_data, color="#8b5cf6")

            with r_col2:
                st.subheader("Model Performance Table")
                st.dataframe(
                    model_results,
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "Accuracy": st.column_config.NumberColumn(format="%.3f"),
                        "Balanced Accuracy": st.column_config.NumberColumn(format="%.3f"),
                        "Recall (PD Sensitivity)": st.column_config.NumberColumn(format="%.3f"),
                        "Specificity (Healthy Detection)": st.column_config.NumberColumn(format="%.3f")
                    }
                )
                st.info(
                    "**Key Finding:** Subject-wise CV prevents voice leakage. While Random Forest achieves high recall (0.848), "
                    "Logistic Regression achieves the highest balanced accuracy (0.617) and specificity (0.470)."
                )

st.divider()

# ---------- TECHNICAL SKILLS ----------
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="portfolio-card">
    <div class="card-title">Technical Arsenal</div>
    <div class="tech-grid">
        <div class="tech-item" title="Python"><img class="tech-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"/></div>
        <div class="tech-item" title="Django"><img class="tech-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg"/></div>
        <div class="tech-item" title="C#"><img class="tech-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg"/></div>
        <div class="tech-item" title="Java"><img class="tech-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg"/></div>
        <div class="tech-item" title="C++"><img class="tech-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg"/></div>
        <div class="tech-item" title="C"><img class="tech-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg"/></div>
        <div class="tech-item" title="PostgreSQL"><img class="tech-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg"/></div>
        <div class="tech-item" title="MySQL"><img class="tech-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg"/></div>
        <div class="tech-item" title="Arduino / IoT"><img class="tech-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/arduino/arduino-original.svg"/></div>
        <div class="tech-item" title="JavaScript"><img class="tech-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"/></div>
        <div class="tech-item" title="HTML5"><img class="tech-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"/></div>
        <div class="tech-item" title="CSS3"><img class="tech-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"/></div>
    </div>
</div>
""", unsafe_allow_html=True)


st.divider()

# ---------- FEATURED PROJECTS ----------
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.header("Featured Projects")

projects = [
    {
        "title": "ALAGA (Senior Citizen Health Platform)",
        "role": "Full-Stack Developer",
        "tools": "Python, Django",
        "desc": "A community healthcare web application designed for managing senior citizen health records and geospatial monitoring across local barangays."
    },
    {
        "title": "Sir Serato Simulator",
        "role": "Lead Game Developer",
        "tools": "Java, JavaFX, FXGL, JDBC, MySQL",
        "desc": "Multi-threaded arcade classroom management game proctoring quizzes in real time, featuring full CRUD leaderboard integration."
    },
    {
        "title": "Project Bassa: IoT Security Buoy",
        "role": "IoT & Embedded Developer",
        "tools": "C++, Arduino, Water Quality Sensors, GPS",
        "desc": "Real-time marine sanctuary monitoring buoy detecting illegal fishing activities. Recognized as a 7th DOST Imake.wemake Top 20 Finalist."
    },
    {
        "title": "SariSariSmart POS",
        "role": "Java / Database Developer",
        "tools": "Java, MySQL",
        "desc": "Point of Sale and inventory system modernizing traditional sari-sari store notebook accounting with automated sales tracking and analytics."
    }
]

p_col1, p_col2 = st.columns(2)
for i, proj in enumerate(projects):
    col = p_col1 if i % 2 == 0 else p_col2
    with col.container(border=True):
        st.subheader(proj["title"])
        st.caption(f"**Role:** {proj['role']} | **Stack:** {proj['tools']}")
        st.write(proj["desc"])
        st.button("View Details", key=f"btn_{i}")

st.divider()

# ---------- CONTACT FORM ----------
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.header("Get In Touch")

k1, k2 = st.columns([1, 2], gap="large")
with k1:
    st.write("📍 San Isidro, Talisay City, Cebu, 6000")
    st.write("📧 mrypacina@gmail.com")
    st.write("📱 09309692418")
    st.link_button("GitHub Profile", "https://github.com/Mary-Rose01")

with k2:
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        topic = st.selectbox("Reason for contact", ["Collaboration", "Job Opportunity", "Feedback", "Just saying hi!"])
        message = st.text_area("Message")
        
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            if name and message:
                st.session_state.messages.append({"Name": name, "Topic": topic, "Time": datetime.now().strftime("%H:%M")})
                st.success(f"Thanks, {name}! Your message regarding {topic} has been received.")
                st.balloons()
            else:
                st.error("Please fill out your name and message.")

# Footer
st.caption("© 2026 Mary Rose T. Pacina · CSIT 349 · Section F2")
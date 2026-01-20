


import streamlit as st

# ================= CONFIG =================
st.set_page_config(page_title="Pranshu Gautam | Portfolio", layout="centered", initial_sidebar_state="collapsed")

# ================= CUSTOM CSS =================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Source+Sans+Pro:wght@300;400;600;700&display=swap');

    .stApp {
        background: linear-gradient(180deg, #0f1117 0%, #1a1d29 100%);
        font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3, h4 {
        font-family: 'Inter', sans-serif;
        color: #e8e9ed;
    }

    h1 {
        font-size: 2.75rem !important;
        font-weight: 700;
        color: #ffffff;
        text-align: center;
    }

    h2 {
        font-size: 1.5rem !important;
        font-weight: 600;
        color: #d1d5db;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        padding-bottom: 12px;
        margin-top: 40px;
    }

    /* Card Styling */
    .pro-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 24px;
        margin: 16px 0;
    }

    .pro-card:hover {
        background: rgba(255, 255, 255, 0.05);
        border-color: rgba(255, 255, 255, 0.12);
    }

    .pro-card h3 {
        color: #f3f4f6;
        font-size: 1.15rem;
        font-weight: 600;
        margin: 0 0 4px 0;
    }

    .pro-card .subtitle {
        color: #a5b4fc;
        font-weight: 500;
        font-size: 0.95rem;
    }

    .pro-card .date {
        color: rgba(255, 255, 255, 0.5);
        font-size: 0.85rem;
    }

    .pro-card p {
        color: rgba(255, 255, 255, 0.75);
        line-height: 1.7;
        margin: 12px 0 0 0;
    }

    .pro-card ul {
        color: rgba(255, 255, 255, 0.75);
        margin: 12px 0 0 0;
        padding-left: 20px;
    }

    .pro-card li {
        margin: 6px 0;
        line-height: 1.6;
    }

    /* Stats Box */
    .stat-box {
        background: rgba(99, 102, 241, 0.08);
        border: 1px solid rgba(99, 102, 241, 0.15);
        border-radius: 12px;
        padding: 20px 16px;
        text-align: center;
    }

    .stat-number {
        font-family: 'Inter', sans-serif;
        font-size: 2rem;
        color: #a5b4fc;
        font-weight: 700;
    }

    .stat-label {
        color: rgba(255, 255, 255, 0.6);
        font-size: 0.9rem;
        margin-top: 6px;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        justify-content: center;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        padding: 8px;
        border: 1px solid rgba(255, 255, 255, 0.06);
    }

    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 8px;
        color: rgba(255, 255, 255, 0.6);
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        padding: 10px 20px;
    }

    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255, 255, 255, 0.05);
        color: rgba(255, 255, 255, 0.9);
    }

    .stTabs [aria-selected="true"] {
        background: rgba(99, 102, 241, 0.2) !important;
        color: #c7d2fe !important;
    }

    /* Badge */
    .badge {
        display: inline-block;
        background: rgba(99, 102, 241, 0.1);
        border: 1px solid rgba(99, 102, 241, 0.2);
        color: #a5b4fc;
        padding: 4px 10px;
        border-radius: 6px;
        margin: 3px;
        font-family: 'Inter', sans-serif;
        font-size: 0.75rem;
        font-weight: 500;
    }

    .badges {
        margin: 10px 0;
    }

    /* Contact Links */
    .contact-links {
        text-align: center;
        margin: 24px 0 32px 0;
    }

    .contact-link {
        display: inline-block;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        padding: 12px 20px;
        margin: 6px;
        color: rgba(255, 255, 255, 0.8);
        text-decoration: none;
        font-family: 'Inter', sans-serif;
        font-size: 0.9rem;
    }

    .contact-link:hover {
        background: rgba(99, 102, 241, 0.15);
        border-color: rgba(99, 102, 241, 0.3);
        color: #c7d2fe;
    }

    .center-text {
        text-align: center;
    }

    /* Progress Bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #6366f1 0%, #8b5cf6 100%);
    }

    .stProgress > div > div {
        background: rgba(255, 255, 255, 0.1);
    }

    p, li {
        color: rgba(255, 255, 255, 0.75);
    }

    hr {
        border: none;
        height: 1px;
        background: rgba(255, 255, 255, 0.08);
        margin: 24px 0;
    }

    a {
        color: #a5b4fc;
        text-decoration: none;
    }

    a:hover {
        color: #c7d2fe;
    }
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("<h1>Pranshu Gautam</h1>", unsafe_allow_html=True)
st.markdown("""
<p class='center-text' style='font-size: 1.1rem; color: rgba(255,255,255,0.6); margin-top: -10px;'>
    Software Engineer · Automation Specialist · Problem Solver
</p>
""", unsafe_allow_html=True)

st.markdown("""
<div class='contact-links'>
    <a href='mailto:pranshugautam8699@gmail.com' class='contact-link'>Email</a>
    <a href='https://www.linkedin.com/in/pranshu-gautam' target='_blank' class='contact-link'>LinkedIn</a>
    <a href='https://github.com/PRAN5HU' target='_blank' class='contact-link'>GitHub</a>
</div>
""", unsafe_allow_html=True)

# ================= TABS =================
tab1, tab2, tab3, tab4, tab5 = st.tabs(["About", "Experience", "Projects", "Skills", "Achievements"])

# ================= ABOUT =================
with tab1:
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>4×</div>
            <div class='stat-label'>Scholarships</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>7</div>
            <div class='stat-label'>Patents</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>3×</div>
            <div class='stat-label'> Excellence Awards</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>8.30</div>
            <div class='stat-label'>CGPA</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## About Me")
    st.markdown("""
    I'm a final-year engineering student at **Manipal University Jaipur** passionate about building 
    efficient, automated solutions. With hands-on experience at **Dell Technologies** and **BITS Pilani**, 
    I specialize in backend development, database optimization, and creating tools that reduce manual effort significantly.

    Currently seeking full-time opportunities in software engineering where I can contribute to impactful projects.
    """)

    st.markdown("## Education")
    st.markdown("""
    <div class='pro-card'>
        <h3>Manipal University Jaipur</h3>
        <span class='subtitle'>B.Tech in Computer and Communication Engineering</span><br>
        <span class='date'>2022 – 2026 · CGPA: 8.30 / 10</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Leadership")

    st.markdown("""
    <div class='pro-card'>
        <h3>Student Placement Coordinator</h3>
        <span class='subtitle'>Manipal University Karnal</span> · <span class='date'>Jan 2025 – Present</span>
        <ul>
            <li>Coordinate between placement cell, recruiters, and alumni</li>
            <li>Manage placement drives and company interactions</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='pro-card'>
        <h3>Technical Secretary</h3>
        <span class='subtitle'>Turing Sapiens Chapter</span> · <span class='date'>Jun 2024 – Jun 2025</span>
        <ul>
            <li>Organized <strong>10+ hackathons</strong> and coding competitions</li>
            <li>Led <strong>15+ volunteers</strong> and increased participation by <strong>50%</strong></li>
            <li>Conducted technical workshops and guest lectures</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ================= EXPERIENCE =================
with tab2:
    st.markdown("## Professional Experience")

    st.markdown("""
    <div class='pro-card'>
        <h3>Dell Technologies</h3>
        <span class='subtitle'>Undergraduate Intern</span> · <span class='date'>May 2025 – Jul 2025 · Bangalore</span>
        <ul>
            <li>Enhanced Oracle APEX dashboards for internal tooling projects</li>
            <li>Automated Upload Diagnostics Tool, reducing manual effort by <strong>95%</strong></li>
            <li>Conducted backend testing and optimized Oracle DB workflows</li>
            <li>Improved system efficiency and user experience across teams</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='pro-card'>
        <h3>BITS Pilani</h3>
        <span class='subtitle'>Summer Research Intern</span> · <span class='date'>Jun 2024 – Jul 2024 · Pilani</span>
        <ul>
            <li>Built smart solar microgrid system using scraped weather data</li>
            <li>Developed automation scripts for preprocessing sensor data</li>
            <li>Improved real-time forecasting accuracy and energy optimization</li>
            <li>Integrated web scraping with IoT systems</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ================= PROJECTS =================
with tab3:
    st.markdown("## Featured Projects")

    st.markdown("""
    <div class='pro-card'>
        <h3>RealTimeCSVMonitor</h3>
        <div class='badges'>
            <span class='badge'>MATLAB</span>
            <span class='badge'>Python</span>
            <span class='badge'>Real-time Analytics</span>
        </div>
        <p>Live CSV data monitoring system with MATLAB to track file changes in real-time. 
        Features timestamp formatting and dynamic visualization for streaming insights. 
        Python script fetches web data and updates CSV files for seamless automation workflows.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='pro-card'>
        <h3>IMD Weather Data Scraper</h3>
        <div class='badges'>
            <span class='badge'>Python</span>
            <span class='badge'>BeautifulSoup</span>
            <span class='badge'>Web Scraping</span>
        </div>
        <p>Automated scraper for India Meteorological Department weather data. 
        Stores structured data into CSV for downstream analysis, enabling local weather 
        data ingestion without paid APIs. Ideal for weather prediction projects.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='pro-card'>
        <h3>PresentifyX</h3>
        <span class='date'>Image to PPTX & Document Summarizer</span>
        <div class='badges'>
            <span class='badge'>Python</span>
            <span class='badge'>PyQt5</span>
            <span class='badge'>AI</span>
            <span class='badge'>Desktop App</span>
        </div>
        <p>Desktop application that converts images into fully editable PowerPoint files. 
        Features AI-based document summarization, modern GUI with configurable pipeline, 
        and standalone executable distribution via PyInstaller.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='pro-card'>
        <h3>Instagram Follower Tracking System</h3>
        <div class='badges'>
            <span class='badge'>Python</span>
            <span class='badge'>Selenium</span>
            <span class='badge'>Automation</span>
        </div>
        <p>Automated follower/unfollower tracking with high accuracy using Selenium web automation. 
        Generates analytics reports for account changes and provides insights into growth patterns.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='pro-card'>
        <h3>Autonomous Wall-Following Robot</h3>
        <div class='badges'>
            <span class='badge'>Arduino</span>
            <span class='badge'>C++</span>
            <span class='badge'>Embedded Systems</span>
        </div>
        <p>Robotics project featuring stepper motor control with ultrasonic sensors for obstacle detection. 
        Implements configurable wall-following strategies with LCD display and audio feedback. 
        Modular firmware design with documented schematics.</p>
    </div>
    """, unsafe_allow_html=True)

# ================= SKILLS =================
with tab4:
    st.markdown("## Technical Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='pro-card'>
            <h3>Languages</h3>
            <div class='badges'>
                <span class='badge'>C</span>
                <span class='badge'>C++</span>
                <span class='badge'>Java</span>
                <span class='badge'>Python</span>
                <span class='badge'>SQL</span>
                <span class='badge'>PL/SQL</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='pro-card'>
            <h3>Tools & Technologies</h3>
            <div class='badges'>
                <span class='badge'>Oracle APEX</span>
                <span class='badge'>Oracle DB</span>
                <span class='badge'>MySQL</span>
                <span class='badge'>Selenium</span>
                <span class='badge'>Arduino</span>
                <span class='badge'>MATLAB</span>
                <span class='badge'>Git</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='pro-card'>
            <h3>Soft Skills</h3>
            <div class='badges'>
                <span class='badge'>Problem Solving</span>
                <span class='badge'>Agile</span>
                <span class='badge'>Leadership</span>
                <span class='badge'>Communication</span>
                <span class='badge'>Project Management</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='pro-card'>
            <h3>Domains</h3>
            <div class='badges'>
                <span class='badge'>Backend Development</span>
                <span class='badge'>Database Design</span>
                <span class='badge'>Web Scraping</span>
                <span class='badge'>Automation</span>
                <span class='badge'>IoT Systems</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ================= ACHIEVEMENTS =================
with tab5:
    st.markdown("## Achievements")

    st.markdown("""
    <div class='pro-card'>
        <h3>Hackathons</h3>
        <ul>
            <li><strong>Winner</strong> — Autobots2.0)</li>
            <li><strong>Winner</strong> — Algorithm Faceoff (Dell Technologies)</li>
            <li><strong>Winner</strong> — Randomize Hackathon (MUJ)</li>
            <li><strong>Top 3</strong> — Turing Hacks (MUJ)</li>
            <li><strong>Top 3</strong> — Bobble AI Hackathon</li>
            <li><strong>Top 10</strong> — MUJHackX2.0 International Hackathon</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='pro-card'>
        <h3>Academic Recognition</h3>
        <ul>
            <li><strong>4× Scholarship Recipient</strong> — 20% Scholarship</li>
            <li><strong>7× Patent Applications</strong> — Innovation in Technology</li>
            <li><strong>3× Student Excellence Awards</strong> — Outstanding Performance</li>
            <li><strong>8.30 CGPA</strong> — Consistent Academic Achievement</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>5+</div>
            <div class='stat-label'>Hackathons Won</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>200+</div>
            <div class='stat-label'>Students Mentored</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='stat-box'>
            <div class='stat-number'>10+</div>
            <div class='stat-label'>Events Organized</div>
        </div>
        """, unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("---")
st.markdown("""
<p class='center-text' style='color: rgba(255, 255, 255, 0.4); font-size: 0.85rem;'>
    © 2026 Pranshu Gautam · Karnal, India
</p>
""", unsafe_allow_html=True)








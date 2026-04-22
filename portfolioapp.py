import streamlit as st

# 1. Page configuration for a professional AI dashboard
st.set_page_config(
    page_title="Zohaib Hussain | AI & CS Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for a sleek Dark Mode & Neon Accents
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    [data-testid="stSidebar"] {
        background-color: #161B22;
        border-right: 1px solid #3B82F6;
    }
    .stMetric {
        background-color: #1F2937;
        border: 1px solid #3B82F6;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(59, 130, 246, 0.2);
    }
    h1, h2, h3 {
        color: #3B82F6 !important;
        font-family: 'Inter', sans-serif;
    }
    .project-card {
        background-color: #1F2937;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        border-left: 5px solid #3B82F6;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar - Profile & Contact details [cite: 2, 3, 5, 6]
with st.sidebar:
    st.markdown("# Mohd Zohaib Hussain")
    st.write("📍 Dubai, UAE")
    st.write("🚗 Valid UAE Driving License") [cite: 3]
    st.markdown("---")
    st.subheader("Connect")
    st.write("📧 ZOHAIBHUSSAIN4321@GMAIL.COM") [cite: 6]
    st.write("📱 +971 56 972 9983") [cite: 5]
    
    st.markdown("---")
    st.subheader("Technical Toolkit") [cite: 64, 65, 67]
    st.write("**Languages:** Python (Advanced), SQL, C++, Java") [cite: 64]
    st.write("**AI/ML:** TensorFlow, Scikit-Learn, CNNs, SHAP") [cite: 65]
    st.write("**Tools:** Docker, Git/GitHub, Streamlit, Tableau") [cite: 67, 55]

# 4. Hero Section & Career High-Impact Results [cite: 24, 29, 37, 55]
st.title("Industrial AI & Computer Science Professional")
st.write("Transforming complex business needs into scalable, data-driven technical solutions.") [cite: 24]

st.header("🚀 Performance Metrics")
m1, m2, m3 = st.columns(3)
with m1:
    st.metric(label="Safety Incidents", value="-35%", delta="Impact at InnoBayt") [cite: 29]
with m2:
    st.metric(label="Reporting Efficiency", value="+70%", delta="Impact at Najah Media") [cite: 55]
with m3:
    st.metric(label="Model Accuracy", value="90%", delta="FinTech AI Performance") [cite: 37]

st.markdown("---")

# 5. Technical Project Showcase with Demos [cite: 35, 41, 47]
st.header("🛠️ Detailed Project Showcase")

# --- Project 1: FinTech AI ---
with st.expander("📊 FinTech AI: Deriv-AI-Market-Sentinel", expanded=True):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Bitcoin Volatility Prediction")
        st.write("""
        Developed an end-to-end ML pipeline utilizing the **CCXT API** for real-time market data[cite: 36]. 
        Integrated **SHAP** for model explainability to ensure transparent decision-making[cite: 38].
        """)
        st.write("**Impact:** Achieved ~90% accuracy in predicting volatility[cite: 37].")
        st.code("Stack: Python, Scikit-Learn, Streamlit, CCXT API") [cite: 36]
    with col2:
        st.info("**Interactive Demo: Risk Logic**")
        v_index = st.slider("Select Volatility Index", 0.0, 1.0, 0.4)
        status = "🔴 HIGH RISK" if v_index > 0.7 else "🟢 STABLE"
        st.subheader(f"Status: {status}")

# --- Project 2: Deep Learning ---
with st.expander("🎙️ Deep Learning: Speech Emotion Recognition"):
    st.subheader("Audio Sentiment Classification")
    st.write("""
    Designed a **CNN-based model** to classify human emotions from raw audio files[cite: 50]. 
    Performed **MFCC feature extraction** on audio data to achieve high-accuracy sentiment detection[cite: 51].
    """)
    st.write("**Application:** Designed for integration into AI Customer Service bots[cite: 52].")
    st.code("Stack: Python, Librosa, TensorFlow/Keras (CNN)") [cite: 49]

# --- Project 3: Risk Analytics ---
with st.expander("🛡️ Risk Analytics: Fraud Detection Model"):
    st.subheader("Secure Financial Assessment")
    st.write("""
    Engineered a **Random Forest** classification model to assess creditworthiness and identify fraudulent transactions[cite: 42]. 
    Optimized the model specifically to **minimize false negatives**, ensuring high-security standards for financial risk[cite: 44, 46].
    """)
    st.code("Stack: Python, Pandas, Scikit-Learn") [cite: 41]

st.markdown("---")

# 6. Detailed Professional Experience [cite: 27, 31, 53, 59]
st.header("💼 Professional Journey")

# InnoBayt
st.subheader("Jr. Product Manager Trainee | InnoBayt") [cite: 27]
st.write("""
- Managed the lifecycle of an **IoT-based Safety System** for 500+ site laborers[cite: 28].
- Built **Automated Flagging Logic** that reduced heat-related safety incidents by 35%[cite: 29].
- Managed **3D Reality Capture** solutions, improving clash detection accuracy by 22%[cite: 30].
""")

# Najah Media
st.subheader("Business Analyst | Najah Media") [cite: 53]
st.write("""
- Analyzed cross-platform data for 12+ clients to increase **ROAS**[cite: 54].
- Automated **70% of reporting** using Tableau and Excel dashboards[cite: 55].
- Performed **A/B testing** on ad creatives, driving a 1.5% increase in CTR[cite: 57, 58].
""")

# AllMilez
st.subheader("Operations Analyst | AllMilez") [cite: 31]
st.write("""
- Identified operational bottlenecks and implemented targeted workflow solutions[cite: 32].
- Leveraged analytics to support the implementation of **streamlined business processes**[cite: 33].
""")

# INK IT Solutions
st.subheader("SAP BTP Intern | INK IT Solutions") [cite: 59]
st.write("""
- Streamlined workflows to reduce manual processing time[cite: 61].
- Translated business needs into technical specifications for feature implementation[cite: 62].
""")

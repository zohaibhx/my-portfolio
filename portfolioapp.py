import streamlit as st

# 1. Page Configuration & Professional Styling
st.set_page_config(page_title="Zohaib Hussain | AI Portfolio", page_icon="🤖", layout="wide")

# Custom CSS for Black Background & Neon Accents
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    [data-testid="stSidebar"] {
        background-color: #161B22;
    }
    .stMetric {
        background-color: #1F2937;
        border: 1px solid #3B82F6;
        padding: 15px;
        border-radius: 10px;
    }
    h1, h2, h3 {
        color: #3B82F6 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar - Professional Identity
st.sidebar.title("Mohd Zohaib Hussain") [cite: 2]
st.sidebar.write("📍 Dubai, UAE") [cite: 27]
st.sidebar.write("📧 ZOHAIBHUSSAIN4321@GMAIL.COM") [cite: 6]
st.sidebar.write("📱 +971 56 972 9983") [cite: 5]
st.sidebar.markdown("---")
st.sidebar.subheader("Technical Toolkit")
st.sidebar.write("**Languages:** Python (Advanced), SQL, C++, Java") [cite: 64]
st.sidebar.write("**AI/ML:** TensorFlow, Scikit-Learn, CNNs, SHAP") [cite: 65]
st.sidebar.write("**Tools:** Docker, Git, Tableau, Excel, SAP BTP") [cite: 55, 59, 67]
st.sidebar.markdown("---")
st.sidebar.write("🚗 Valid UAE Driving License") [cite: 3]

# 3. Hero Section
st.title("Industrial AI & Computer Science")
st.write("Specializing in transforming business needs into scalable technical products[cite: 24].")

# 4. Key Performance Metrics
st.header("🚀 High-Impact Results")
m1, m2, m3 = st.columns(3)
with m1:
    st.metric(label="Safety Incidents", value="-35%", delta="Improved Safety") [cite: 29]
with m2:
    st.metric(label="Reporting Speed", value="+70%", delta="Efficiency Gain") [cite: 55]
with m3:
    st.metric(label="Model Accuracy", value="90%", delta="Market Prediction") [cite: 37]

st.markdown("---")

# 5. Project Demos (Detailed Sections)
st.header("🛠️ Technical Project Showcase")

# --- Project 1: FinTech AI ---
with st.expander("📊 FinTech AI: Deriv-AI-Market-Sentinel"):
    st.subheader("Predicting Bitcoin Volatility")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        Developed an end-to-end ML pipeline utilizing the CCXT API for real-time data[cite: 35, 36]. 
        Integrated **SHAP** for model explainability to ensure transparent decision-making[cite: 38].
        """)
        st.write("**Impact:** Achieved 90% accuracy in volatility forecasting[cite: 37].")
    with col2:
        st.info("**Try the Logic:**")
        test_val = st.slider("Select Volatility Index", 0.0, 1.0, 0.5)
        st.write(f"Predicted Market Risk: {'🔴 HIGH' if test_val > 0.7 else '🟢 STABLE'}")

# --- Project 2: Deep Learning ---
with st.expander("🎙️ Deep Learning: Speech Emotion Recognition"):
    st.subheader("Audio Sentiment Classification")
    st.write("""
    Designed a CNN-based system to classify human emotions from raw audio files[cite: 48, 50]. 
    Used **Librosa** for MFCC feature extraction to detect sentiment for AI customer service bots[cite: 49, 51, 52].
    """)
    st.code("Stack: Python, TensorFlow, Keras, Librosa") [cite: 49]

# --- Project 3: Risk Analytics ---
with st.expander("🛡️ Risk Analytics: Fraud Detection Model"):
    st.subheader("Secure Financial Assessment")
    st.write("""
    Engineered a Random Forest classification model to assess creditworthiness and identify fraud[cite: 39, 41, 42].
    Optimized to minimize **false negatives**, ensuring high-security standards[cite: 43, 44].
    """)
    st.code("Stack: Python, Pandas, Scikit-Learn") [cite: 41]

st.markdown("---")

# 6. Detailed Experience
st.header("💼 Professional Journey")

st.subheader("Jr. Product Manager Trainee | InnoBayt") [cite: 26, 27]
st.write("""
- Managed IoT Worker Welfare system for **500+ laborers** tracking heart rate and heat stress[cite: 28].
- Implemented **Automated Flagging Logic** reducing heat-related incidents by 35%[cite: 29].
- Improved construction accuracy by 22% using **3D Reality Capture**[cite: 30].
""")

st.subheader("Business Analyst | Najah Media") [cite: 53]
st.write("""
- Managed ad portfolios for **12+ clients**, increasing ROAS through budget reallocation[cite: 54].
- Automated **70% of monthly reporting** via Tableau and Excel dashboards[cite: 55].
- Drove a 1.5% increase in CTR through A/B testing and funnel analysis[cite: 56, 57, 58].
""")

st.subheader("Operations Analyst | AllMilez") [cite: 31]
st.write("""
- Identified bottlenecks in day-to-day processes to enhance operational productivity[cite: 32].
- Leveraged analytics to implement streamlined business processes[cite: 33].
""")

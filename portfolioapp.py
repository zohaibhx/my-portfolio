import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Zohaib Hussain | AI Portfolio", 
    page_icon="🤖", 
    layout="wide"
)

# 2. Sleek Dark Theme & Neon Blue Styling
st.markdown("""
    <style>
    /* 1. Main Background and Global Text */
    .stApp { 
        background-color: #0E1117; 
    }
    
    /* 2. Force ALL text elements to White */
    .stApp, .stApp p, .stApp span, .stApp label, .stApp li {
        color: #FFFFFF !important;
    }

    /* 3. Sidebar Specific - This fixes your screenshot issue */
    [data-testid="stSidebar"] { 
        background-color: #161B22; 
        border-right: 1px solid #3B82F6; 
    }
    
    /* Targets every text element inside the sidebar specifically */
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span, 
    [data-testid="stSidebar"] div,
    [data-testid="stSidebar"] label {
        color: #FFFFFF !important;
    }

    /* 4. Headers - Keeping your cool blue color */
    h1, h2, h3 { 
        color: #3B82F6 !important; 
    }

    /* 5. Metrics & Boxes */
    .stMetric { 
        background-color: #1F2937; 
        border: 1px solid #3B82F6; 
        padding: 20px; 
        border-radius: 12px; 
    }
    
    /* Ensure metric labels/values are white */
    [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {
        color: #FFFFFF !important;
    }

    /* 6. Expander Content */
    .streamlit-expanderContent {
        color: #FFFFFF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar - Profile & Core Skills
with st.sidebar:
    st.title("Zohaib Hussain")
    st.write("📍 Dubai, UAE")
    st.write("📧 ZOHAIBHUSSAIN4321@GMAIL.COM")
    st.write("📱 +971 56 972 9983")
    st.write("🚗 Valid UAE Driving License")
    st.markdown("---")
    st.subheader("Technical Toolkit")
    st.write("**Languages:** Python, SQL, C++, Java")
    st.write("**AI/ML:** TensorFlow, Scikit-Learn, CNNs, SHAP")
    st.write("**Tools:** Docker, Git, Tableau, Streamlit")

# 4. Hero Section & High-Impact Results
st.title("Industrial AI & Computer Science")
st.write("Transforming complex business data into scalable, user-centric technical solutions.")

st.header("🚀 High-Impact Metrics")
m1, m2, m3 = st.columns(3)
with m1: st.metric("Safety Incidents", "-35%", delta="At InnoBayt")
with m2: st.metric("Reporting Automation", "70%", delta="Efficiency Gain")
with m3: st.metric("Model Accuracy", "90%", delta="Market Prediction")

st.markdown("---")

# 5. Interactive Project Showcase
st.header("🛠️ Detailed Projects & Demos")

# Project 1: FinTech AI
with st.expander("📊 FinTech AI: Deriv-AI-Market-Sentinel", expanded=True):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Bitcoin Volatility Prediction")
        st.write("Built an end-to-end ML pipeline utilizing the CCXT API for real-time market data. Integrated SHAP for model explainability.")
        st.write("**Impact:** ~90% accuracy in predicting market volatility.")
        st.code("Stack: Python, Scikit-Learn, CCXT API, Streamlit")
    with col2:
        st.info("**Interactive Risk Logic**")
        v_idx = st.slider("Market Volatility Input", 0.0, 1.0, 0.4)
        risk = "🔴 HIGH" if v_idx > 0.7 else "🟢 STABLE"
        st.subheader(f"Risk Status: {risk}")

# Project 2: Deep Learning
with st.expander("🎙️ Deep Learning: Speech Emotion Recognition"):
    st.subheader("Audio Sentiment Classification")
    st.write("Designed a CNN-based model to classify human emotions from raw audio files. Used Librosa for MFCC feature extraction.")
    st.write("**Use Case:** Applicable for AI-driven customer service automation.")
    st.code("Stack: Python, Librosa, TensorFlow/Keras (CNN)")

# Project 3: Risk Analytics
with st.expander("🛡️ Risk Analytics: Fraud Detection"):
    st.subheader("Creditworthiness Assessment")
    st.write("Engineered a Random Forest model to identify fraudulent transactions, optimized specifically to minimize false negatives.")
    st.code("Stack: Python, Pandas, Scikit-Learn")

st.markdown("---")

# 6. Full Experience History
st.header("💼 Professional Journey")

st.subheader("Jr. Product Manager Trainee | InnoBayt")
st.write("""
- Managed IoT safety systems for 500+ laborers, tracking biometrics like heart rate and heat stress[cite: 28].
- Built logic that reduced heat-related incidents by 35% via predictive health alerts[cite: 29].
- Improved construction accuracy by 22% using 3D Reality Capture solutions[cite: 30].
""")

st.subheader("Business Analyst | Najah Media")
st.write("""
- Automated 70% of reporting using Tableau and Excel for 12+ client portfolios[cite: 55].
- Analyzed cross-platform data to reallocate budgets and increase overall ROAS[cite: 54].
- Performed A/B testing on ad creatives to drive a 1.5% increase in Click-Through Rate[cite: 57, 58].
""")

st.subheader("Operations Analyst | AllMilez")
st.write("- Identified bottlenecks in daily operations and implemented targeted workflow improvements[cite: 32, 33].")

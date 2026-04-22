import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Zohaib Hussain | AI Portfolio", 
    page_icon="🤖", 
    layout="wide"
)

# 2. Sleek Dark Theme & Force White Text
st.markdown("""
    <style>
    /* Force background to black and all text to white */
    .stApp, .stApp p, .stApp span, .stApp label, .stApp div {
        background-color: #0E1117;
        color: #FFFFFF !important;
    }
    /* Sidebar specific styling */
    [data-testid="stSidebar"], [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        background-color: #161B22 !important;
        color: #FFFFFF !important;
        border-right: 1px solid #3B82F6;
    }
    /* Metric boxes with glowing blue borders */
    .stMetric {
        background-color: #1F2937 !important;
        border: 1px solid #3B82F6 !important;
        padding: 20px;
        border-radius: 12px;
    }
    /* Glowing Blue Headers */
    h1, h2, h3 {
        color: #3B82F6 !important;
    }
    /* Fix for expanders to keep text white */
    .streamlit-expanderHeader {
        background-color: #161B22 !important;
        color: #FFFFFF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar - Profile & Core Skills
with st.sidebar:
    st.markdown("## Mohd Zohaib Hussain")
    st.write("📍 Dubai, UAE [cite: 9, 27]")
    st.write("📧 ZOHAIBHUSSAIN4321@GMAIL.COM [cite: 6]")
    st.write("📱 +971 56 972 9983 [cite: 5]")
    st.write("🚗 Valid UAE Driving License [cite: 3]")
    st.markdown("---")
    st.subheader("Technical Toolkit")
    st.write("**Languages:** Python, SQL, C++, Java [cite: 64]")
    st.write("**AI/ML:** TensorFlow, Scikit-Learn, CNNs, SHAP [cite: 65]")
    st.write("**Tools:** Docker, Git, PowerBI, Streamlit ")

# 4. Hero Section
st.title("Industrial AI & Computer Science")
st.write("Final-year Computer Science student at BITS Pilani Dubai with experience in Product Management, AI, and Data Analytics. [cite: 23]")

st.header("🚀 High-Impact Metrics")
m1, m2, m3 = st.columns(3)
with m1: 
    st.metric("Safety Incidents", "-35%", delta="At InnoBayt")
    st.caption("Reduced via predictive health alerts. [cite: 29]")
with m2: 
    st.metric("Reporting Automation", "70%", delta="Efficiency Gain")
    st.caption("Automated reporting for 12+ clients. [cite: 55]")
with m3: 
    st.metric("Model Accuracy", "90%", delta="Market Prediction")
    st.caption("Bitcoin volatility forecasting accuracy. [cite: 37]")

st.markdown("---")

# 5. Interactive Project Showcase
st.header("🛠️ Detailed Projects & Demos")

with st.expander("📊 FinTech AI: Deriv-AI-Market-Sentinel", expanded=True):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Bitcoin Volatility Prediction")
        st.write("Developed an end-to-end ML pipeline utilizing the CCXT API for real-time market data. [cite: 35, 36]")
        st.write("Integrated **SHAP** for model explainability and deployed a live dashboard for monitoring. [cite: 38]")
        st.code("Stack: Python, Scikit-Learn, CCXT API, Streamlit [cite: 36]")
    with col2:
        st.info("**Interactive Risk Logic**")
        v_idx = st.slider("Market Volatility Input", 0.0, 1.0, 0.4)
        risk = "🔴 HIGH" if v_idx > 0.7 else "🟢 STABLE"
        st.subheader(f"Risk Status: {risk}")

with st.expander("🎙️ Deep Learning: Speech Emotion Recognition"):
    st.subheader("Audio Sentiment Classification")
    st.write("Designed and trained a CNN-based model to classify human emotions from raw audio files. [cite: 48, 50]")
    st.write("Performed MFCC feature extraction for sentiment detection applicable for AI customer service bots. [cite: 51, 52]")
    st.code("Stack: Python, Librosa, TensorFlow/Keras (CNN) [cite: 49]")

with st.expander("🛡️ Risk Analytics: Fraud Detection"):
    st.subheader("Creditworthiness Assessment")
    st.write("Engineered a classification model to assess creditworthiness and identify fraudulent transactions. [cite: 41, 42]")
    st.write("Optimized the model to minimize false negatives for financial risk assessment. [cite: 43, 44, 46]")
    st.code("Stack: Python, Pandas, Scikit-Learn [cite: 41]")

st.markdown("---")

# 6. Experience History
st.header("💼 Professional Journey")

st.subheader("Jr. Product Manager Trainee | InnoBayt [cite: 26, 27]")
st.write("* Supported the end-to-end product lifecycle for an IoT-based Worker Welfare & Safety System for 500+ site laborers. ")
st.write("* Developed Automated Flagging Logic reducing safety incidents by 35%. ")
st.write("* Managed delivery of a 3D Reality Capture solution, improving clash detection accuracy by 22%. ")

st.subheader("Business Analyst | Najah Media ")
st.write("* Analyzed cross-platform data for 12+ SMMA clients to increase ROAS. ")
st.write("* Developed performance dashboards using Tableau and Excel, automating 70% of reporting. ")
st.write("* Conducted deep-dive funnel analysis and A/B testing to drive a 1.5% increase in CTR. ")

st.subheader("Operations Analyst | AllMilez ")
st.write("* Identified operational bottlenecks and implemented targeted workflow solutions. ")
st.write("* Leveraged analytics to track performance and support streamlined business processes. ")

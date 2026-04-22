import streamlit as st

# Page configuration for a professional look
st.set_page_config(page_title="Zohaib Hussain | Portfolio", page_icon="🚀", layout="wide")

# Custom CSS for a cleaner look
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar - Profile & Contact
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100) # Placeholder profile icon
st.sidebar.title("Mohd Zohaib Hussain") [cite: 2]
st.sidebar.write("📍 Dubai, UAE") [cite: 27]
st.sidebar.write("🚗 UAE Driving License Holder") [cite: 3]
st.sidebar.markdown("---")
st.sidebar.header("Contact")
st.sidebar.write("📧 zohaibhussain4321@gmail.com") [cite: 6]
st.sidebar.write("📱 +971 56 972 9983") [cite: 5]

st.sidebar.header("Technical Toolkit")
st.sidebar.write("**Languages:** Python, SQL, C++, Java") [cite: 64]
st.sidebar.write("**AI/ML:** TensorFlow, Scikit-Learn, CNNs") [cite: 65]
st.sidebar.write("**Tools:** Docker, Git, Tableau, Excel") [cite: 55, 67]

# Main Content
st.title("Computer Science & AI Professional")
st.write("Specializing in building data-driven solutions and automating complex technical lifecycles.") [cite: 23, 24]

# Section 1: Measurable Impact (Recruiters love metrics)
st.header("📈 Career Highlights")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Safety Incident Reduction", value="35%", delta="-35% vs baseline")
    st.caption("Developed predictive health alerts for 500+ site laborers.") [cite: 28, 29]

with col2:
    st.metric(label="Reporting Automation", value="70%", delta="Efficiency Gain")
    st.caption("Automated cross-platform reporting for 12+ client portfolios.") [cite: 54, 55]

with col3:
    st.metric(label="Market Prediction Accuracy", value="90%", delta="FinTech AI")
    st.caption("Achieved high-precision Bitcoin volatility forecasting.") [cite: 37]

st.markdown("---")

# Section 2: Technical Projects
st.header("🛠️ Key Projects")

# Project 1: FinTech AI
with st.expander("📊 FinTech AI: Market Sentinel"):
    st.write("Developed an end-to-end ML pipeline predicting Bitcoin volatility.") [cite: 35, 37]
    st.write("**Impact:** Integrated SHAP for model explainability and deployed a live dashboard for real-time risk monitoring.") [cite: 38]
    st.code("Stack: Python, Scikit-Learn, CCXT API, Streamlit") [cite: 36]

# Project 2: Deep Learning
with st.expander("🎙️ Deep Learning: Speech Emotion Recognition"):
    st.write("CNN-based model designed to classify human emotions from raw audio files.") [cite: 48, 50]
    st.write("**Impact:** Performed MFCC feature extraction for sentiment detection applicable to AI customer service.") [cite: 51, 52]
    st.code("Stack: Python, Librosa, TensorFlow/Keras (CNN)") [cite: 49]

# Project 3: Risk Analytics
with st.expander("🛡️ Risk Analytics: Fraud Detection Model"):
    st.write("Engineered a classification model to assess creditworthiness and identify fraudulent transactions.") [cite: 39, 42]
    st.write("**Impact:** Optimized model to minimize false negatives, ensuring high-security financial risk standards.") [cite: 43, 44]
    st.code("Stack: Python, Pandas, Scikit-Learn (Random Forest)") [cite: 41]

st.markdown("---")

# Section 3: Professional Experience (Brief)
st.header("💼 Professional Experience")
st.write("**Jr. Product Manager Trainee** | InnoBayt, Dubai") [cite: 27]
st.write("Managing end-to-end product lifecycles for IoT-based safety systems and 3D reality capture solutions.") [cite: 28, 30]

st.write("**Business Analyst** | Najah Media") [cite: 53]
st.write("Analyzed cross-platform data for a portfolio of 12+ clients to increase ROAS.") [cite: 54]

st.write("**Operations Analyst** | AllMilez") [cite: 31]
st.write("Identified operational bottlenecks and implemented workflow solutions to improve efficiency.") [cite: 32]

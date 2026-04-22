import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Zohaib Hussain | Portfolio", page_icon="🚀", layout="wide")

# 2. Sidebar - Bio & Contact
st.sidebar.title("Mohd Zohaib Hussain")
st.sidebar.write("📍 Dubai, UAE")
st.sidebar.write("📧 zohaibhussain4321@gmail.com")
st.sidebar.write("📱 +971 56 972 9983")
st.sidebar.markdown("---")
st.sidebar.subheader("Technical Toolkit")
st.sidebar.write("**Languages:** Python, SQL, C++, Java")
st.sidebar.write("**AI/ML:** TensorFlow, Scikit-Learn, CNNs")
st.sidebar.write("**Tools:** Docker, Git, Tableau, Excel")

# 3. Main Header
st.title("Computer Science & AI Professional")
st.write("Building data-driven solutions and automating technical lifecycles.")

# 4. Key Metrics (Recruiter-friendly)
st.header("📈 Career Highlights")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Safety Incident Reduction", value="35%")
    st.caption("Developed predictive health alerts for 500+ site laborers.")
with col2:
    st.metric(label="Reporting Automation", value="70%")
    st.caption("Automated performance dashboards for marketing portfolios.")

st.markdown("---")

# 5. Technical Projects
st.header("🛠️ Key Projects")

with st.expander("📊 FinTech AI: Market Sentinel"):
    st.write("Predicts Bitcoin volatility with 90% accuracy.")
    st.code("Stack: Python, Scikit-Learn, CCXT API")

with st.expander("🛡️ Risk Analytics: Fraud Detection"):
    st.write("Engineered a model to assess creditworthiness and identify fraud.")
    st.code("Stack: Python, Pandas, Scikit-Learn")

with st.expander("🎙️ Deep Learning: Emotion Recognition"):
    st.write("CNN-based model to classify emotions from raw audio files.")
    st.code("Stack: Python, TensorFlow, Keras")

st.markdown("---")

# 6. Experience Summary
st.header("💼 Experience")
st.write("**Jr. Product Manager Trainee** | InnoBayt, Dubai")
st.write("**Business Analyst** | Najah Media")

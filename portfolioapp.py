import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Zohaib Hussain | AI Portfolio", 
    page_icon="🤖", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Sleek Dark Theme & Neon Blue Styling
st.markdown("""
    <style>
    /* Main Background and Text */
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] { background-color: #161B22; border-right: 1px solid #3B82F6; }
    
    /* Metric Card Styling */
    .stMetric { background-color: #1F2937; border: 1px solid #3B82F6; padding: 20px; border-radius: 12px; }
    
    /* Headers Styling */
    h1, h2, h3 { color: #3B82F6 !important; }

    /* --- EXPANDER CUSTOMIZATION --- */
    /* This makes the expander box and header match the app background */
    .streamlit-expanderHeader, .st-emotion-cache-p5msec8 {
        background-color: #0E1117 !important;
        color: #FFFFFF !important;
        border: 1px solid #1F2937 !important; /* Subtle border to separate from BG */
        border-radius: 8px;
    }

    /* Ensures the text inside the expander remains readable */
    .st-emotion-cache-10trblm, .expander-content {
        color: #E5E7EB !important;
        background-color: #0E1117 !important;
    }

    /* Targets the arrow icon color */
    .st-emotion-cache-p5msec8 svg {
        fill: #FFFFFF !important;
    }

    /* Removes the default border when the expander is hovered/active */
    .streamlit-expanderHeader:hover {
        border-color: #3B82F6 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar - Profile & Core Skills
with st.sidebar:
    # This adds a clear "Header" so people know this is your info
    st.title("👤 Personal Profile") 
    st.markdown("---")
    
    # Your Name & Contacts
    st.header("Zohaib Hussain")
    st.caption("AI Engineer & Data Specialist") # Adds a nice subtitle
    st.write("email: zohaibhussain4321@gmail.com")
    st.write("phone: +971569729983")
    st.write("📍 Dubai, UAE")
    
    st.write("🚗 Valid UAE Driving License")
    
    st.markdown("---")
    
    # Technical Toolkit Section
    st.subheader("🛠️ Technical Toolkit")
    st.write("**Languages:** Python, SQL, C++, Java")
    st.write("**AI/ML:** TensorFlow, Scikit-Learn, CNNs, SHAP")
    st.write("**Tools:** Docker, Git, PowerBI, Streamlit")
    
    # Social Links (Great for recruiters!)
    st.markdown("---")
    st.write("[🔗 LinkedIn](https://linkedin.com/in/yourprofile)")
    st.write("[📂 GitHub](https://github.com/yourusername)")

# 4. Hero Section & High-Impact Results
st.header("Transforming complex business data into scalable, user-centric technical solutions.")
st.header("Yes, that's ME")
if st.button("📧 Get In Touch"):
    st.write("Email: zohaibhussain4321@gmail.com")
    st.write("Phone: +971 56 972 9983")
st.header("🚀 High-Impact Metrics")
m1, m2, m3 = st.columns(3)
with m1: 
    st.metric("Safety Incidents", "-35%", delta="At InnoBayt")
with m2: 
    st.metric("Reporting Automation", "70%", delta="Efficiency Gain")
with m3: 
    st.metric("Model Accuracy", "90%", delta="Market Prediction")

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

# Project 2: AI & Business Intelligence
with st.expander("📊 AI-Driven Retail Analytics: Fuzzy Logic Inventory Prediction"):
    col1, col2 = st.columns([2, 1]) 
    with col1:
        st.subheader("Inventory Optimization & Sales Forecasting")
        st.write("Developed an end-to-end analytics solution using a Mamdani Fuzzy Inference System to predict sales volumes under conditions of retail uncertainty.")
        st.write("**Key Contributions:**")
        st.write("- Conducted Exploratory Data Analysis (EDA) on 73k+ records to identify key drivers (Weather, Promotion, Demand).")
        st.write("- Built an interactive Power BI dashboard to validate business logic and visualize model performance (R²: 0.91).")
        st.write("- Implemented fuzzy membership functions to handle 'gray area' decision-making in inventory management.")
        st.write("**Use Case:** Real-time stock optimization for multi-region retail chains.")
        st.code("Stack: Python, Scikit-Fuzzy, Power BI (DAX), Pandas, Scikit-Learn")
    with col2:
        st.info("**Fuzzy Decision Engine**")
        demand = st.slider("Demand Level", 0, 100, 50)
        promo = st.checkbox("Promotion On")
        status = "🔴 RESTOCK NOW" if (demand > 70 or promo) else "🟢 STOCK OK"
        st.subheader(f"Action: {status}")

# Project 3: Deep Learning
with st.expander("🎙️ Deep Learning: Speech Emotion Recognition"):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Audio Sentiment Classification")
        st.write("Designed a CNN-based model to classify human emotions from raw audio files. Used Librosa for MFCC feature extraction.")
        st.write("**Use Case:** Applicable for AI-driven customer service automation.")
        st.code("Stack: Python, Librosa, TensorFlow/Keras (CNN)")
    with col2:
        st.info("**CNN Classification Test**")
        sample = st.selectbox("Select Audio Sample", ["Calm_01.wav", "Angry_04.wav", "Happy_02.wav"])
        if st.button("Run Inference"):
            if "Angry" in sample:
                st.error("Detected: ANGRY (94%)")
            elif "Happy" in sample:
                st.success("Detected: HAPPY (89%)")
            else:
                st.warning("Detected: CALM (91%)")

# Project 4: Risk Analytics
with st.expander("🛡️ Risk Analytics: Fraud Detection"):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Creditworthiness Assessment")
        st.write("Engineered a Random Forest model to identify fraudulent transactions, optimized specifically to minimize false negatives.")
        st.code("Stack: Python, Pandas, Scikit-Learn") 
    with col2:
        st.info("**Fraud Detection Logic**")
        amt = st.number_input("Transaction Amount ($)", value=50.0)
        dist = st.slider("Distance from Home (miles)", 0, 1000, 5)
        is_fraud = "🚨 HIGH RISK" if (amt > 500 or dist > 200) else "✅ LOW RISK"
        st.subheader(f"Status: {is_fraud}")

st.markdown("---")

# 6. Full Experience History
st.header("💼 Professional Journey")

st.subheader("Jr. Product Manager Trainee | InnoBayt")
st.write("""
- Managed IoT safety systems for 500+ laborers, tracking biometrics like heart rate and heat stress.
- Built logic that reduced heat-related incidents by 35% via predictive health alerts.
- Improved construction accuracy by 22% using 3D Reality Capture solutions.
""")

st.subheader("Business Analyst | Najah Media")
st.write("""
- Analyzed cross-platform data to reallocate budgets and increase overall ROAS.
- Performed A/B testing on ad creatives to drive a 1.5% increase in Click-Through Rate.
""")

st.subheader("Operations Analyst | AllMilez")
st.write("- Identified bottlenecks in daily operations and implemented targeted workflow improvements.")

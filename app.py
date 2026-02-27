import streamlit as st
import pickle
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* 🌸 App Background */
.main {
    background: linear-gradient(135deg, #FFF7CD, #FDC3A1);
    animation: fadeIn 1s ease-in;
}

/* ✨ Fade Animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

/* 🏠 Title */
.title {
    font-size: 44px;
    font-weight: 900;
    color: #F57799;
    text-align: center;
    text-shadow: 2px 2px 10px rgba(245,119,153,0.4);
    animation: float 3s ease-in-out infinite;
}

/* 💫 Floating Title */
@keyframes float {
    0% {transform: translateY(0);}
    50% {transform: translateY(-6px);}
    100% {transform: translateY(0);}
}

/* 📝 Subtitle */
.subtext {
    font-size: 18px;
    color: #FB9B8F;
    text-align: center;
    margin-bottom: 20px;
}

/* 📦 Card Styling */
.stSubheader, .stNumberInput, .stSelectbox, .stSlider {
    background: rgba(253, 195, 161, 0.65);
    padding: 16px;
    border-radius: 16px;
    box-shadow: 0 10px 25px rgba(251, 155, 143, 0.35);
    animation: slideUp 0.9s ease;
}

/* 🚀 Slide Animation */
@keyframes slideUp {
    from {opacity: 0; transform: translateY(25px);}
    to {opacity: 1; transform: translateY(0);}
}

/* 🔘 Predict Button */
.stButton > button {
    background: linear-gradient(135deg, #F57799, #FB9B8F);
    color: white;
    font-size: 20px;
    font-weight: bold;
    border-radius: 20px;
    height: 3.3em;
    width: 100%;
    border: none;
    transition: all 0.35s ease;
}

/* ✨ Button Hover */
.stButton > button:hover {
    transform: scale(1.08);
    box-shadow: 0 0 30px rgba(245,119,153,0.7);
    background: linear-gradient(135deg, #FB9B8F, #F57799);
}

/* 💰 Result Box */
.stSuccess {
    background: rgba(255, 247, 205, 0.9);
    color: #F57799;
    border-radius: 18px;
    padding: 20px;
    font-size: 24px;
    font-weight: bold;
    box-shadow: 0 0 35px rgba(245,119,153,0.4);
    animation: pop 0.8s ease;
}

/* 🎉 Pop Animation */
@keyframes pop {
    0% {transform: scale(0.9); opacity: 0;}
    100% {transform: scale(1); opacity: 1;}
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<p class="title">🏠 Smart House Price Predictor 💖</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtext">✨ Cute • Smart • AI-Powered Real Estate Prediction ✨</p>',
    unsafe_allow_html=True
)

st.write("")

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("best_model.pkl", "rb"))

# ---------------- LAYOUT ----------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Property Details")
    area = st.number_input("📐 Area (sqft)", 500, 10000, 1500)
    bedrooms = st.number_input("🛏 Bedrooms", 1, 10, 3)
    bathrooms = st.number_input("🛁 Bathrooms", 1, 10, 2)
    floors = st.number_input("🏢 Floors", 1, 5, 1)

with col2:
    st.subheader("🏘 Extra Features")
    age = st.number_input("⏳ House Age (Years)", 0, 100, 5)
    garage = st.selectbox("🚗 Garage Available?", ["No", "Yes"])
    location_score = st.slider("📍 Location Score (1–10)", 1, 10, 5)

garage_value = 1 if garage == "Yes" else 0

st.write("")
st.write("")

# ---------------- PREDICTION ----------------
if st.button("🚀 Predict House Price"):
    input_data = np.array([[area, bedrooms, bathrooms, floors, age, garage_value, location_score]])
    prediction = model.predict(input_data)

    st.markdown("---")
    st.success(f"💰 Estimated House Price: ₹ {prediction[0]:,.2f}")
    st.balloons()
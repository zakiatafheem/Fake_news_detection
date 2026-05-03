import streamlit as st
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("📰 Fake News Detection (NLP)")

text = st.text_area("Enter News Article")

if st.button("Predict"):

    if text.strip() == "":
        st.warning("Please enter text")
    else:
        prediction = model.predict([text])[0]

        if prediction == 1:
            st.success("✅ REAL NEWS")
        else:
            st.error("🚨 FAKE NEWS")
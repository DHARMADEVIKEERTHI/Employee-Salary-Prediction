import streamlit as st
import joblib
import numpy as np

st.title("💼 Salary Prediction App")
st.divider()

st.write("Enter your experience and job rating to predict salary")

# ✅ Provide a label to both number_input calls
years = st.number_input("Years of Experience", value=1, step=1, min_value=0)
jobrate = st.number_input("Job Rating (0–10)", value=3.5, step=0.1, min_value=0.0)

# Input vector
x = [years, jobrate]

# Load model
model = joblib.load("Linearmodel.pkl")

st.divider()

# Predict button
predict = st.button("Predict Salary")

st.divider()

if predict:
    st.balloons()
    x = np.array([x])
    prediction = model.predict(x)[0]
    st.success(f"💰 Predicted Salary: ₹{prediction:,.2f}")
else:
    st.info("Please press the button above to make a prediction.")

# app.py

import streamlit as st

st.title("Student Score Predictor")
st.header("Enter Student Details")
st.subheader("Prediction Section")
st.write("This app predicts student score.")

name = st.text_input("Enter Name")
print(name)

hours = st.number_input("Study Hours")
hours = st.number_input(
    "Study Hours",
    min_value=0,
    max_value=24,
    value=1
)
print(hours)

hours = st.slider(
    "Study Hours",
    0,
    12
)

gender = st.selectbox(
    "Gender",
    ["Male","Female"]
)

education = st.radio(
    "Education",
    ["UG","PG"]
)

if st.button("Predict"):
    st.write("Prediction Started")

# st.write(score)
st.success("Loan Approved")
st.error("Loan Rejected")
st.warning("Low Credit Score")


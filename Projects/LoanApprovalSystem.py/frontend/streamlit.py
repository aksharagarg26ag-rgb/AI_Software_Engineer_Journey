import streamlit as st
import requests

st.title("Loan Approval System")
st.header("Predicting Loan Approved OR Not!")

st.subheader("Enter Applicant Details: ")

income= st.number_input("Enter Income: ", min_value=0, max_value=150000)
age = st.number_input("Enter Age: " ,min_value=18, max_value=60)
credit_score = st.number_input("Enter CreditScore: ", min_value=300, max_value=800)
employment_years = st.number_input("Enter EmploymentYear: ", min_value=0, max_value=20)

if st.button("Predict "):
    # JSON Data to send to FastAPI
    data = {
        "income": income,
        "age": age,
        "credit_score": credit_score,
        "employment_years": employment_years
    }

    try:

        # Send POST request to FastAPI
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        # Check if request successful
        if response.status_code == 200:

            result = response.json()

            approved = result["approved"]
            probability = result["probability"]

            if approved:
                st.success("✅ Loan Approved")
            else:
                st.error("❌ Loan Rejected")

            st.write(f"### Approval Probability : {probability:.2%}")

        else:
            st.error(f"Server Error : {response.status_code}")

    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to FastAPI Server.")
        st.info("Start FastAPI first using:")
        st.code("uvicorn app:app --reload")

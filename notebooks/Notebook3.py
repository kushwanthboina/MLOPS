import streamlit as st
import requests

# Title and description
st.title("Banking Term Deposit Prediction")
st.write("Enter client details to predict whether they will subscribe to a term deposit.")

# Input fields for each feature

# Numeric Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
balance = st.number_input("Balance (euros)", value=0.0)
day = st.number_input("Day of Last Contact", min_value=1, max_value=31, value=15)
duration = st.number_input("Duration (seconds)", min_value=0, value=0)
campaign = st.number_input("Number of Contacts in Campaign", min_value=1, value=1)
pdays = st.number_input("Days Since Last Contact", value=-1)
previous = st.number_input("Number of Previous Contacts", value=0)

# Categorical Inputs
job = st.selectbox("Job", options=[
    "admin.", "unknown", "unemployed", "management", "housemaid",
    "entrepreneur", "student", "blue-collar", "self-employed",
    "retired", "technician", "services"
])
marital = st.selectbox("Marital", options=["married", "divorced", "single"])
education = st.selectbox("Education", options=["unknown", "secondary", "primary", "tertiary"])
default = st.selectbox("Credit in Default", options=["yes", "no"])
housing = st.selectbox("Housing Loan", options=["yes", "no"])
loan = st.selectbox("Personal Loan", options=["yes", "no"])
contact = st.selectbox("Contact", options=["unknown", "telephone", "cellular"])
month = st.selectbox("Month of Last Contact", options=[
    "jan", "feb", "mar", "apr", "may", "jun",
    "jul", "aug", "sep", "oct", "nov", "dec"
])
poutcome = st.selectbox("Outcome of Previous Campaign", options=[
    "unknown", "other", "failure", "success"
])

# Prepare data for API call
data = {
    "age": age,
    "job": job,
    "marital": marital,
    "education": education,
    "default": default,
    "balance": balance,
    "housing": housing,
    "loan": loan,
    "contact": contact,
    "day": day,
    "month": month,
    "duration": duration,
    "campaign": campaign,
    "pdays": pdays,
    "previous": previous,
    "poutcome": poutcome
}

# Button to trigger prediction
if st.button("Predict"):
    # Endpoint URL (ensure FastAPI is running at this URL)
    url = "http://127.0.0.1:8000/predict"

    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            result = response.json()
            prediction = result.get("prediction", "No prediction returned")
            st.success(f"Prediction: {prediction}")
        else:
            st.error(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

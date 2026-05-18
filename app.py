import streamlit as st
import pickle
import numpy as np


# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


st.set_page_config(page_title="Customer Churn Prediction")

st.title("Customer Churn Prediction")
st.write("Predict whether a telecom customer will churn or not")


st.sidebar.header("Customer Details")


gender = st.sidebar.selectbox("Gender", ["Female", "Male"])
senior = st.sidebar.selectbox("Senior Citizen", [0, 1])
partner = st.sidebar.selectbox("Partner", ["No", "Yes"])
dependents = st.sidebar.selectbox("Dependents", ["No", "Yes"])

tenure = st.sidebar.number_input(
    "Tenure (Months)",
    min_value=0,
    max_value=100,
    value=12
)

phone_service = st.sidebar.selectbox(
    "Phone Service",
    ["No", "Yes"]
)

paperless = st.sidebar.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)

monthly_charges = st.sidebar.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=50.0
)

total_charges = st.sidebar.number_input(
    "Total Charges",
    min_value=0.0,
    value=500.0
)


# Encoding
gender = 1 if gender == "Male" else 0
partner = 1 if partner == "Yes" else 0
dependents = 1 if dependents == "Yes" else 0
phone_service = 1 if phone_service == "Yes" else 0
paperless = 1 if paperless == "Yes" else 0


# Dummy values for remaining columns
# Must match training feature count
input_data = np.array([[
    gender,
    senior,
    partner,
    dependents,
    tenure,
    phone_service,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    monthly_charges,
    total_charges,
    paperless
]])


if st.button("Predict"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Customer is likely to churn")
    else:
        st.success("Customer is not likely to churn")
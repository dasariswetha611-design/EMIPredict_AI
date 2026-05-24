import streamlit as st
import pandas as pd
import joblib

class_model = joblib.load("models/best_classification_model.pkl")
reg_model = joblib.load("models/best_regression_model.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")
input_columns = joblib.load("models/input_columns.pkl")

st.title("EMIPredict AI")
st.write("Intelligent Financial Risk Assessment Platform")

age = st.number_input("Age", 25, 60, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
marital_status = st.selectbox("Marital Status", ["Single", "Married"])
education = st.selectbox("Education", ["High School", "Graduate", "Post Graduate", "Professional"])

monthly_salary = st.number_input("Monthly Salary", 15000, 200000, 50000)
employment_type = st.selectbox("Employment Type", ["Private", "Government", "Self-employed"])
years_of_employment = st.number_input("Years of Employment", 0.0, 40.0, 5.0)
company_type = st.selectbox("Company Type", ["Startup", "Small", "Medium", "Large", "MNC"])

house_type = st.selectbox("House Type", ["Rented", "Own", "Family"])
monthly_rent = st.number_input("Monthly Rent", 0, 100000, 10000)
family_size = st.number_input("Family Size", 1, 10, 4)
dependents = st.number_input("Dependents", 0, 8, 2)

school_fees = st.number_input("School Fees", 0, 100000, 5000)
college_fees = st.number_input("College Fees", 0, 100000, 0)
travel_expenses = st.number_input("Travel Expenses", 0, 50000, 5000)
groceries_utilities = st.number_input("Groceries and Utilities", 0, 100000, 15000)
other_monthly_expenses = st.number_input("Other Monthly Expenses", 0, 100000, 5000)

existing_loans = st.selectbox("Existing Loans", ["Yes", "No"])
current_emi_amount = st.number_input("Current EMI Amount", 0, 100000, 5000)
credit_score = st.number_input("Credit Score", 300, 850, 700)
bank_balance = st.number_input("Bank Balance", 0, 1000000, 100000)
emergency_fund = st.number_input("Emergency Fund", 0, 1000000, 50000)

emi_scenario = st.selectbox(
    "EMI Scenario",
    [
        "E-commerce Shopping EMI",
        "Home Appliances EMI",
        "Vehicle EMI",
        "Personal Loan EMI",
        "Education EMI"
    ]
)

requested_amount = st.number_input("Requested Amount", 10000, 1500000, 100000)
requested_tenure = st.number_input("Requested Tenure", 3, 84, 12)

data = {
    "age": age,
    "gender": gender,
    "marital_status": marital_status,
    "education": education,
    "monthly_salary": monthly_salary,
    "employment_type": employment_type,
    "years_of_employment": years_of_employment,
    "company_type": company_type,
    "house_type": house_type,
    "monthly_rent": monthly_rent,
    "family_size": family_size,
    "dependents": dependents,
    "school_fees": school_fees,
    "college_fees": college_fees,
    "travel_expenses": travel_expenses,
    "groceries_utilities": groceries_utilities,
    "other_monthly_expenses": other_monthly_expenses,
    "existing_loans": existing_loans,
    "current_emi_amount": current_emi_amount,
    "credit_score": credit_score,
    "bank_balance": bank_balance,
    "emergency_fund": emergency_fund,
    "emi_scenario": emi_scenario,
    "requested_amount": requested_amount,
    "requested_tenure": requested_tenure
}

input_df = pd.DataFrame([data])

input_df["total_expenses"] = (
    input_df["monthly_rent"] +
    input_df["school_fees"] +
    input_df["college_fees"] +
    input_df["travel_expenses"] +
    input_df["groceries_utilities"] +
    input_df["other_monthly_expenses"] +
    input_df["current_emi_amount"]
)

input_df["expense_to_income_ratio"] = input_df["total_expenses"] / input_df["monthly_salary"]
input_df["emi_to_income_ratio"] = input_df["current_emi_amount"] / input_df["monthly_salary"]
input_df["balance_to_income_ratio"] = input_df["bank_balance"] / input_df["monthly_salary"]
input_df["emergency_fund_ratio"] = input_df["emergency_fund"] / input_df["monthly_salary"]

for col in input_columns:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[input_columns]

if st.button("Predict EMI Risk"):
    class_pred = class_model.predict(input_df)
    eligibility = label_encoder.inverse_transform(class_pred)[0]

    max_emi = reg_model.predict(input_df)[0]

    st.success(f"EMI Eligibility: {eligibility}")
    st.info(f"Maximum Safe Monthly EMI: ₹{max_emi:,.2f}")
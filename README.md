# EMIPredict AI

EMIPredict AI is an intelligent financial risk assessment platform that predicts EMI eligibility and maximum safe EMI amount.

## Problem Statement
Many customers struggle to pay EMI due to poor financial planning. This project uses machine learning to assess EMI risk and provide safer loan decisions.

## Dataset
The dataset contains 400,000 financial records with demographic, income, expense, credit, and loan-related features.

## Machine Learning Tasks
1. Classification: Predict EMI eligibility
2. Regression: Predict maximum safe monthly EMI

## Models Used
### Classification
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier

### Regression
- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

## Best Classification Accuracy
96.42%

## Application
The project includes a Streamlit web app where users enter financial details and get:
- EMI Eligibility
- Maximum Safe Monthly EMI

## How to Run
```bash
streamlit run app.py
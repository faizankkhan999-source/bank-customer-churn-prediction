import streamlit as st

st.set_page_config(
    page_title="Bank Customer Churn Dashboard",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Predictive Modeling and Risk Scoring for Bank Customer Churn")

st.header("Project Overview")
st.write("""
This project predicts customer churn using machine learning techniques
and helps identify customers at risk of leaving the bank.
""")

st.metric("Best Average F1-Score", "0.854")

st.header("Features Used")
st.write("""
- Credit Score
- Age
- Tenure
- Balance
- Number of Products
- Has Credit Card
- Active Member Status
- Estimated Salary
- Geography
- Gender
""")

st.header("Risk Categories")
st.write("""
🟢 Low Risk
🟡 Medium Risk
🔴 High Risk
""")

st.header("Recommendations")
st.write("""
- Target high-risk customers with retention campaigns.
- Improve customer engagement.
- Provide personalized banking services.
- Monitor churn risk regularly.
""")

st.success("Bank Customer Churn Prediction Dashboard")

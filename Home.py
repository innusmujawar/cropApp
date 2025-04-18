import streamlit as st
from components.db import load_data
from components.charts import crop_expense_chart

st.title("📊 Dashboard")

data = load_data()
total_income = sum(crop["income"] for crop in data["crops"])
total_expense = sum(exp["amount"] for exp in data["expenses"])

col1, col2 = st.columns(2)
col1.metric("Total Income", f"₹ {total_income:,.2f}")
col2.metric("Total Expenses", f"₹ {total_expense:,.2f}")

st.divider()
crop_expense_chart()

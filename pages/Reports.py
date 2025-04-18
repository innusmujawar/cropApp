import streamlit as st
import pandas as pd
from components.db import load_data

st.set_page_config(page_title="Reports", layout="wide")
st.title("📁 Reports")

# Load data
data = load_data()
crops = data["crops"]
expenses = data["expenses"]

# Crop dropdown
crop_names = [c["name"] for c in crops]
selected_crop = st.selectbox("🌾 Select a Crop to Export Report", crop_names)

# Filter crop and its expenses
crop_data = next((c for c in crops if c["name"] == selected_crop), None)
crop_expenses = [e for e in expenses if e["crop"] == selected_crop]

if crop_data:
    income = crop_data.get("income", 0)
    total_expense = sum(e["amount"] for e in crop_expenses)
    profit_or_loss_value = income - total_expense

    # Build dynamic table row
    summary_data = {
        "Crop": selected_crop,
        "Income (₹)": income,
        "Total Expenses (₹)": total_expense,
    }

    if profit_or_loss_value >= 0:
        summary_data["Profit (₹)"] = profit_or_loss_value
    else:
        summary_data["Loss (₹)"] = abs(profit_or_loss_value)

    df_report = pd.DataFrame([summary_data])

    # Display summary table
    st.subheader("📄 Crop Financial Summary")
    st.dataframe(df_report, use_container_width=True)

    # Convert to CSV and export
    csv = df_report.to_csv(index=False)
    st.download_button(
        label="⬇️ Export Summary Report as CSV",
        data=csv,
        file_name=f"{selected_crop}_summary.csv",
        mime="text/csv"
    )
else:
    st.warning("No crop data found.")

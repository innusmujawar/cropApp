import streamlit as st
import datetime
from components.db import load_data, save_data

def expense_form():
    db = load_data()
    # st.subheader("💸 Add Expense to Crop")

    crop_names = [c["name"] for c in db["crops"]]
    if not crop_names:
        st.warning("No crops found. Please create a crop first.")
        return

    crop = st.selectbox("Select Crop", crop_names)
    head = st.selectbox("Expense Head", db["expense_heads"])
    amount = st.number_input("Amount", step=10.0)
    expense_date = st.date_input("Expense Date", value=datetime.date.today())

    if st.button("Add Expense"):
        db["expenses"].append({
            "crop": crop,
            "head": head,
            "amount": amount,
            "date": str(expense_date)
        })
        save_data(db)
        st.success("Expense added successfully.")

def expense_head_form():
    db = load_data()
    # st.subheader("🧾 Add New Expense Head")
    new_head = st.text_input("Expense Head Name")
    if st.button("Add Head"):
        if new_head not in db["expense_heads"]:
            db["expense_heads"].append(new_head)
            save_data(db)
            st.success("New head added.")

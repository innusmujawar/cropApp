import streamlit as st
from datetime import date
from components.db import load_data, save_data

st.set_page_config(page_title="Create Crop", layout="wide")
st.title("🌱 Create New Crop")

# Load data
data = load_data()
crops = data["crops"]

with st.form("create_crop_form"):
    name = st.text_input("Crop Name")
    area = st.number_input("Area (in acres)", min_value=0.0)
    start_date = st.date_input("Start Date", value=date.today())
    end_date = st.date_input("End Date (optional)", value=None)
    income = st.number_input("Expected Income (₹)", min_value=0.0, value=0.0)

    submitted = st.form_submit_button("➕ Add Crop")

    if submitted:
        if not name:
            st.warning("Crop name is required.")
        else:
            new_crop = {
                "name": name,
                "area": area,
                "start_date": str(start_date),
                "end_date": str(end_date) if end_date else "",
                "income": income
            }
            crops.append(new_crop)
            save_data(data)
            st.success(f"✅ Crop '{name}' created successfully!")

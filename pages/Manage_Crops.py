import streamlit as st
from components.db import load_data, save_data

st.set_page_config(page_title="Manage Crop", layout="wide")
st.title("🌾 Manage Crop")

# Load data
data = load_data()
crops = data["crops"]

# If no crops exist
if not crops:
    st.info("No crops available to manage.")
    st.stop()

# Dropdown to choose crop
crop_names = [c["name"] for c in crops]
selected_crop_name = st.selectbox("Select a crop to manage", crop_names)

# Find the selected crop data
selected_crop = next((c for c in crops if c["name"] == selected_crop_name), None)

if selected_crop:
    st.subheader("✏️ Edit Crop Details")

    with st.form("edit_crop_form"):
        name = st.text_input("Crop Name", selected_crop["name"])
        area = st.number_input("Area (in acres)", min_value=0.0, value=float(selected_crop.get("area", 0.0)))
        start_date = st.date_input("Start Date", selected_crop.get("start_date"))
        end_date = st.date_input("End Date", selected_crop.get("end_date")) if selected_crop.get("end_date") else None
        income = st.number_input("Income (₹)", min_value=0.0, value=float(selected_crop.get("income", 0.0)))

        submit_btn, delete_btn = st.columns(2)
        submitted = submit_btn.form_submit_button("💾 Save Changes")
        delete = delete_btn.form_submit_button("🗑️ Delete Crop")

        if submitted:
            # Update crop in data
            selected_crop.update({
                "name": name,
                "area": area,
                "start_date": str(start_date),
                "end_date": str(end_date) if end_date else "",  # Only update if end date is provided
                "income": income
            })
            save_data(data)
            st.success("Crop details updated successfully.")

        if delete:
            data["crops"] = [c for c in crops if c["name"] != selected_crop_name]
            save_data(data)
            st.success(f"Crop '{selected_crop_name}' deleted successfully.")
            st.experimental_user()

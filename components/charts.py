import streamlit as st
import pandas as pd
import altair as alt
from components.db import load_data

def crop_expense_chart():
    db = load_data()
    if not db["expenses"]:
        st.info("No expenses to display.")
        return

    df = pd.DataFrame(db["expenses"])
    chart = alt.Chart(df).mark_bar().encode(
        x="crop",
        y="amount",
        color="head",
        tooltip=["crop", "head", "amount"]
    ).properties(width=700, height=400, title="Crop Expenses by Type")

    st.altair_chart(chart, use_container_width=True)

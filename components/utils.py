import pandas as pd
import io
from components.db import load_data

def generate_crop_report_csv():
    data = load_data()
    crops = data["crops"]
    expenses = data["expenses"]

    # Sum expenses by crop name
    crop_expense_map = {}
    for exp in expenses:
        crop_expense_map.setdefault(exp["crop"], 0)
        crop_expense_map[exp["crop"]] += exp["amount"]

    # Build report rows
    report_data = []
    for crop in crops:
        total_expenses = crop_expense_map.get(crop["name"], 0)
        income = crop.get("income", 0)
        profit = income - total_expenses
        report_data.append({
            "Crop Name": crop["name"],
            "Area (acres)": crop["area"],
            "Start Date": crop.get("start_date", ""),
            "Income (₹)": income,
            "Total Expenses (₹)": total_expenses,
            "Profit (₹)": profit
        })

    # Convert to CSV
    df = pd.DataFrame(report_data)
    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    return buffer.getvalue()

import streamlit as st
import pandas as pd
import joblib

from report_generator import generate_pdf_report
from visualizations import plot_sales_by_category

# Load model
model = joblib.load(r"C:\Users\Laptop\Desktop\walmart_data_anlytic project\scripts\scripts\xgb_sales_model.pkl")

st.set_page_config(page_title="🛒 Walmart Sales Dashboard", layout="wide")
st.title("🛒 Walmart Sales Prediction and Analytics")

uploaded_file = st.file_uploader("📤 Upload transaction CSV", type=["csv"])

if uploaded_file:
    input_df = pd.read_csv(uploaded_file)

    # Preprocessing
    input_df['date'] = pd.to_datetime(input_df['date'], dayfirst=True)
    input_df['day'] = input_df['date'].dt.day
    input_df['month'] = input_df['date'].dt.month
    input_df['hour'] = pd.to_datetime(input_df['time']).dt.hour

    # Prediction
    try:
        predictions = model.predict(input_df)
        input_df["Predicted Total"] = predictions
        st.success("✅ Predictions generated successfully.")
    except Exception as e:
        st.error(f"❌ Error in prediction: {e}")

    # Display result table
    st.subheader("📄 Prediction Results")
    st.dataframe(input_df)

    # Show plot
    st.subheader("📊 Total Sales by Category")
    fig = plot_sales_by_category(input_df)
    st.plotly_chart(fig, use_container_width=True)

    # Download report
    if st.button("📥 Download PDF Report"):
        report_path = generate_pdf_report(input_df)
        with open(report_path, "rb") as f:
            st.download_button("Download Report", f, file_name="walmart_sales_report.pdf")

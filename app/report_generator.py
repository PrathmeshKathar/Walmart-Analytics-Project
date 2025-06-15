def generate_pdf_report(df):
    from fpdf import FPDF
    import os

    # Clean up column names
    df.columns = df.columns.str.strip()

    print("Available columns:", df.columns)  # Debugging

    pdf = FPDF()
    pdf.add_page()

    font_path = os.path.join(os.path.dirname(__file__), "fonts", "DejaVuSans.ttf")
    pdf.add_font('DejaVu', '', font_path, uni=True)
    pdf.set_font('DejaVu', '', 12)

    pdf.cell(200, 10, txt="Sales Report 📊", ln=True)

    for index, row in df.iterrows():
        line = f"Product: {row['product_name']} | Sales: ₹{row['total_sales']}"
        pdf.cell(200, 10, txt=line, ln=True)

    output_file = "sales_report.pdf"
    pdf.output(output_file)
    return output_file

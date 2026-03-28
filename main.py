from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Helvetica", style="B", size=24)
    pdf.set_text_color(100,254,200)
    pdf.cell(w=0, h=12, text=row["Topic"], align = "L")
    pdf.line(10, 21, 200, 21)

    for y_location in range(31, 290, 11):
        pdf.line(10, y_location, 200, y_location)

    pdf.ln(275)
    pdf.set_font(family="Helvetica", style="I", size=8)
    pdf.set_text_color(100,100,254)
    pdf.cell(w=0, h=10, text=row["Topic"], align="R")

    for page in range(row["Pages"] - 1):
        pdf.add_page()

        for y_location in range(5, 295, 10):
            pdf.line(10, y_location, 200, y_location)

        pdf.ln(275)
        pdf.set_font(family="Helvetica", style="I", size=8)
        pdf.set_text_color(100, 100, 254)
        pdf.cell(w=0, h=10, text=row["Topic"], align="R")

pdf.output("output.pdf")
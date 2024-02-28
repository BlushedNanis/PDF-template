from fpdf import FPDF
from pandas import read_csv


df = read_csv('topics.csv')

pdf = FPDF()

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 16, row['Topic'],0, 1,'L')
    pdf.line(10, 21, 200, 21)
    for i in range(row['Pages'] - 1):
        pdf.add_page()
    


pdf.output('output.pdf')
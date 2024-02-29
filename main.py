from fpdf import FPDF
from pandas import read_csv


df = read_csv('topics.csv')

pdf = FPDF()
pdf.set_auto_page_break(False)

for index, row in df.iterrows():
    pdf.add_page()
    #Set the topic title
    pdf.set_font('Arial', 'B', 16)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 16, row['Topic'],0, 1,'L')
    pdf.line(10, 21, 200, 21)
    #Set inner lines in page
    for y in range(31, 291, 10):
        pdf.line(10, y, 200, y)
    #Set the footer
    pdf.ln(255)
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(0, 10, row['Topic'],0, 0,'R')
    for i in range(row['Pages'] - 1):
        pdf.add_page()
        #Set inner lines in page
        for y in range(21, 291, 10):
            pdf.line(10, y, 200, y)
        #Set the footer
        pdf.ln(270)
        pdf.set_font('Arial', 'B', 10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, 10, row['Topic'],0, 0,'R')
    
pdf.output('output.pdf')
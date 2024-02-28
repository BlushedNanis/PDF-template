from fpdf import FPDF
from pandas import read_csv




pdf = FPDF()


pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 16, 'hello there!',0, 1,'L')

    


pdf.output('output.pdf')
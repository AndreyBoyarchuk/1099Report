from fpdf import FPDF

pdf = FPDF()

# set default alias: {nb} that will be replaced with total page count
pdf.alias_nb_pages()

# Add a Unicode font (uses UTF-8)


for i in range(5):
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Hello World! {nb}')
    pdf.set_font('Times', '', 14)
    pdf.cell(40, 10, 'Hello World! unicode {nb}')

fn = 'nb_pages.pdf'
pdf.output(fn, 'F')

import os

try:
    os.startfile(fn)
except:
    os.system("xdg-open \"%s\"" % fn)
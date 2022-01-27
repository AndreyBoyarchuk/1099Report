import pandas as pd
from fpdf import FPDF
filename = './alley.csv'
df = pd.read_csv(filename)


class PdfReport(FPDF):
    def __init__(self, filename):
        FPDF.__init__(self) #initializes parent class
        self.filename = filename

    def generate(self, first_name,last_name, address_lane,city,zip_code, amount):

        pdf.add_page()
        pdf.set_font(family="Times", size=12, style='B')
        pdf.cell(w=0, h=40, txt="Report Header", border=1, align="C", ln=1)
        pdf.cell(w=0, h=20, txt="Year: 2021 ", border=1,ln=1)
        pdf.cell(w=40, h=20, txt=first_name, border=1)
        pdf.cell(w=0, h=20, txt=last_name, border=1, ln=1)
        pdf.cell(w=0, h=20, txt=address_lane, border=1, ln=1)
        pdf.cell(w=40, h=20, txt=city, border=1 )
        pdf.cell(w=0, h=20, txt=str(zip_code), border=1, ln=1)
        pdf.cell(w=0, h=20, txt=str(amount), border=1, ln=1)

pdf = PdfReport(filename)
pdf.alias_nb_pages()

for ind in df.index:
    pdf.generate(df['first_name'][ind], df['last_name'][ind], df['address_lane'][ind], df['city'][ind], df['zip_code'][ind],df['amount'][ind])

pdf.output('PDF_TEST.pdf','F')


#for ind in df.index:



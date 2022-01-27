import webbrowser
import os
from fpdf import FPDF
from filestack import Client


class PdfReport:
    def __init__(self,filename):
        self.filename=filename
    def generate(self, flatmate1, flatmate2, bill ):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("static/pic.jpg", w=30, h=30)
        pdf.set_font(family="Times", size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatemates Bill", border=1, align="C", ln=1)
        pdf.cell(w=100, h=40, txt="Period: ", border=1)
        pdf.cell(w=0, h=40, txt=bill.period, border=1, ln=1)

        pdf.cell(w=100, h=40, txt="Period: ", border=1)
        pdf.cell(w=0, h=40, txt=bill.period, border=1, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=0, h=40, txt=str(round(flatmate1.pays(bill,flatmate2),2)), border=1, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=0, h=40, txt=str(round(flatmate2.pays(bill, flatmate1), 2)), border=1)

        #Change directory to files
        os.chdir("filesout")
        pdf.output(self.filename)
        webbrowser.open(self.filename)

class FileSharer:

    def __init__(self, filepath, api_key="AoZRHtiSATGSGZnvjiuJPz"):
        self.filepath=filepath
        self.api_key=api_key
    def share(self):
        client= Client(self.api_key)
        new_filelink=client.upload(filepath=self.filepath)
        return new_filelink.url
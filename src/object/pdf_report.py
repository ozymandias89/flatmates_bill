import webbrowser
import os

from fpdf import FPDF
from filestack import Client


class PdfReport:
    """
    PdfReport
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmate Bill", border=0, align="C", ln=1)

        # Insert Period labels and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate1.pays(bill=bill, flatmate2=flatmate2), 2)),
                 border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=str(round(flatmate2.pays(bill=bill, flatmate2=flatmate1), 2)),
                 border=0, ln=1)

        os.chdir("files")

        pdf.output(self.filename)

        webbrowser.open(self.filename)


class FileShare:
    """
    FileShare
    """

    def __init__(self, filepath, api_key="A7oIKpsZgQVKz72Q0V9Drz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)

        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url

from object.bill import Bill
from object.flatmate import Flatmate
from src.object.pdf_report import PdfReport, FileShare

amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the period? E.g. December 2022: ")

name1 = input("What is your name?")
days_in_hourse1 = int(input(f"How many days did {name1} stay in the house during the bill period?"))

name2 = input("What is the name of the other flatmate?")
days_in_hourse2 = int(input(f"How many days did {name2} stay in the house during the bill period?"))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_hourse1)
flatmate2 = Flatmate(name2, days_in_hourse2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)

file_share = FileShare(filepath=pdf_report.filename)
print(file_share.share())

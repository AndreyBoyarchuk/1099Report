from flat import Bill, Flatmate
from reports import PdfReport

billamount=float(input("Hey User, Enter the bill amount"))
period=input("What is the bill period? e.g December 2020")

name1= input("What is your name?")
day_in_the_house= int(input(f"How many days did {name1} stay in the house"))
name2= input("Who is your roomate?")
day_in_the_house2= int(input(f"How many days your roomate stayed {name1} stay in the house"))


the_bill = Bill(amount=billamount, period=period)
john= Flatmate(name=name1, days_in_house=day_in_the_house)
marry= Flatmate(name=name2, days_in_house=day_in_the_house2)

print(john.pays(bill=the_bill,flatemate2=marry))
print(marry.pays(the_bill,john))

pdf_report= PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john,flatmate2=marry,bill=the_bill)
print (str(billamount)+" Here you go!")


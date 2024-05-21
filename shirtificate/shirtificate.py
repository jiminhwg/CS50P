from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()

#header
pdf.add_page()
pdf.set_font("helvetica", "B", 50) #https://pyfpdf.github.io/fpdf2/Tutorial.html
pdf.cell(0, 30, 'CS50 Shirtificate', align='C') #https://pyfpdf.github.io/fpdf2/Tutorial.html

#footer
pdf.image("shirtificate.png", 0, 60) #https://pyfpdf.github.io/fpdf2/Images.html
pdf.set_text_color(255, 255, 255)
pdf.set_font("helvetica", size=30) #https://pyfpdf.github.io/fpdf2/TextStyling.html
pdf.text(70, 148, name+" took CS50")

pdf.output("shirtificate.pdf")
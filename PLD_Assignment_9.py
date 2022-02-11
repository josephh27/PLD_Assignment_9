import json

with open("PLD_Assignment_9.json") as f:
    data = json.load(f)

# with open(r"C:\Users\Core i5 HB\OneDrive\Pictures\School Photos\Applicant Photo.jpg") as file:
    
# for person in data["Person"]:
#     print(person["Phone"])


from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("pdf_background2.png", 0, 0, 218)
        self.ln(0)

# Layout("P", "L")
# Unit ("mm", "cm", "in")
# format ("A3", "A4" (default), "A5", "Letter", "Legal", (100, 150))
pdf = PDF("P", "mm", "Letter")



# Set auto page break
pdf.set_auto_page_break(auto = True)
# Add a page
pdf.add_page() 

# Specify font
# fonts ("times", "courier", "helvetica", "symbol", "zpfdingbats")
# "B" (bold), "U" (underline), "I" (italics), "" (regular), combination (i.e., ("BU"))
pdf.set_font("helvetica", "", 16)

# Add text
# w = width
# h = height
#

pdf.image("Applicant Photo.jpg", 170, 10, 40)
count = 0
for attribute, detail in data["Person"].items():
    count += 1
    detail = str(detail)

    if attribute:
        if count == 1 or count == 2:
            pdf.set_font("helvetica", "B", 13)         
            pdf.multi_cell(155, 10, attribute, ln = 1, border = "B", align = "L")   
        else:
            pdf.set_font("helvetica", "B", 13)         
            pdf.multi_cell(0, 10, attribute, ln = 1, border = "B", align = "L")      
    if detail:    
        pdf.set_font("helvetica", "", 13)
        if count == 8:
            pdf.cell(10, 0)
            detail = detail.replace("'", "").replace("[", "").replace("]", "").replace(",", "").replace("%", "\n")
            print(detail)
            pdf.multi_cell(0, 8, detail, border = 0, ln = 0, align = "L")
        else:
            pdf.cell(10, 0)
            pdf.multi_cell(0, 10, detail, ln = 1, border = 0, align = "L")   
        
if __name__ == "__main__":
    pdf.output("PLD_Assignment_9.pdf") 


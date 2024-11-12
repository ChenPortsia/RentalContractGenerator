from fpdf import FPDF

def text_to_pdf(text, output_path):
  pdf = FPDF()
  pdf.add_page()
  pdf.set_font("Arial", size=12)
  
  for line in text.split('\n'):
    pdf.cell(200, 10, txt=line, ln=True, align='L')
  
  pdf.output(output_path)
from pypdf import PdfReader

pdf_path = "resumes/resume.pdf"

reader =  PdfReader(pdf_path)

text = ""

for page in reader.pages:
    text += page.extract_text()

print(text)
import PyPDF2

def extract_text_from_pdf(file_path):
    text = ''
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)


        for page in pdf_reader.pages:
            text += page.extract_text()
        
    return text
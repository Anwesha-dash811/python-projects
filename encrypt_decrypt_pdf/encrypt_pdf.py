from PyPDF2 import PdfFileWriter,PdfFileReader
output = PdfFileWriter() 
file = PdfFileReader("assignment bootstrap.pdf") 
for i in range(file.numPages ): 
    page = file.getPage(i) 
    output.addPage(page) 
password = "123"
output.encrypt(password) 
with open("encrypted_file.pdf", "wb") as f: 
    output.write(f)
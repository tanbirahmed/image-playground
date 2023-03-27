import PyPDF2

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))

    #you can count the pages
    #you can rotate the pages
    #we can merge PDFs also

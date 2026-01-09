import sys
from pypdf import PdfWriter

def pdf_merger():
    files = sys.argv[1:]
    print(files)
    writer = PdfWriter()
    try:
        for file in files:
            writer.append(file)

        writer.write('./processed_pdfs/combined.pdf')
    except FileNotFoundError:
        print('Cannot find the PDF(s)')

if __name__ == '__main__':
    pdf_merger()
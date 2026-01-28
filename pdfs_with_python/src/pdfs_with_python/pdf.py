import sys
from pypdf import PdfWriter, PdfReader

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


def remove_pdf_watermark():
    files = sys.argv[1]
    reader = PdfReader(files)
    writer = PdfWriter()
    try:
        writer.append(reader)
        writer.remove_images()
        writer.write('./processed_pdfs/removed.pdf')
    except FileNotFoundError:
        print('Cannot find the PDF(s)')


def add_pdf_watermark():
    orig_files = sys.argv[1]
    writer = PdfWriter(clone_from='./processed_pdfs/combined.pdf')
    try:
        imgs = PdfReader(orig_files).pages[0]

        for page in writer.pages:
            page.merge_page(imgs, over=False)

        writer.write('./processed_pdfs/added.pdf')
    except FileNotFoundError:
        print('Cannot find the PDF(s)')

if __name__ == '__main__':
    # pdf_merger()
    # remove_pdf_watermark()
    add_pdf_watermark()
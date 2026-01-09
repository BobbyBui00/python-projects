from pypdf import PdfReader, PdfWriter

## rb in this case is read binary
with open('./pdfs/dummy.pdf', 'rb') as file:
    reader = PdfReader(file)
    print(reader.get_num_pages())
    print(reader.get_page(0))
    page = reader.get_page(0)
    page.rotate(180)
    writer = PdfWriter()
    writer.add_page(page)
    with open('./processed_pdfs/titled.pdf', 'wb') as new_file:
        writer.write(new_file)
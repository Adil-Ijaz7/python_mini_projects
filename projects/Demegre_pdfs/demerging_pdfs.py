import PyPDF2

merged_pdf = open('{path of file that you want to demerge}', mode='rb')


pdf = PyPDF2.PdfFileReader(merged_pdf)

(u, ctr, x) = tuple([0]*3)
for i in range(1, pdf.numPages+1):

    if u >= pdf.numPages:
        print("Successfully done!")
        exit(0)
    name = input("Enter the name of the pdf: ")
    ctr = int(input(f"Enter the number of pages for {name}: "))
    u += ctr
    if u > pdf.numPages:
        print('Limit exceeded! ')
        break

    base_path = '/Users/darpan/Desktop/{}.pdf'
    path = base_path.format(name)
    f = open(path, mode='wb')
    pdf_writer = PyPDF2.PdfFileWriter()

    for j in range(x, x+ctr):
        page = pdf.getPage(j)
        pdf_writer.addPage(page)

    x += ctr

    pdf_writer.write(f)
    f.close()


merged_pdf.close()
print("Successfully done!")

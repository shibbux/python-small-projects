# importing required modules
from pypdf import PdfMerger


def PDFmerge(pdfs, output):
	# creating pdf file merger object
	pdfMerger = PdfMerger()

	# appending pdfs one by one
	for pdf in pdfs:
		pdfMerger.append(pdf)

		# writing combined pdf to output pdf file
		with open(output, 'wb') as f:
			pdfMerger.write(f)


def main():
	# pdf files to merge
	pdfs = ['pdf 1.pdf', 'pdf2.pdf']

	# output pdf file name
	output = 'pdf3.pdf'

	# calling pdf merge function
	PDFmerge(pdfs=pdfs, output=output)


if __name__ == "__main__":
	# calling the main function
	main()

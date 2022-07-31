import textract
import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
# returns text from a .doc, .docx and .pdf file
# @param pathToFile: path directory to file to be read
def converter(pathToFile):
	text = ""
	if pathToFile.endswith(".doc") or pathToFile.endswith(".docx"):
		text = str(textract.process(pathToFile)).lower()
	elif pathToFile.endswith(".pdf"):
		text = str(convert_pdf_to_txt(pathToFile)).lower()
	return text


# extract text from pdf
# @param pathToFile: path directory to pdf file to be read
def convert_pdf_to_txt(path):
  rsrcmgr = PDFResourceManager()
  retstr = StringIO()
  codec = 'utf-8'
  laparams = LAParams()
  device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
  fp = open(path, 'rb')
  interpreter = PDFPageInterpreter(rsrcmgr, device)
  password = ""
  maxpages = 0
  caching = True
  pagenos=set()

  for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
      interpreter.process_page(page)

  text = retstr.getvalue()

  fp.close()
  device.close()
  retstr.close()
  return text

#driver test code
# dr = "/media/amey/LocalDisk0/_projects/cv-reader/documents/resume.docx"
# text = converter(dr)
# print(text)
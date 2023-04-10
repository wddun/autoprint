import os
import glob
import subprocess
import PyPDF2

# define the directory where the PDF files are located
directory = '/path/to/directory'

# get a list of all the PDF files in the directory
pdf_files = glob.glob(os.path.join(directory, '*.pdf'))

# loop through each PDF file in the directory
for pdf_file in pdf_files:
    # get the base filename without the extension
    filename = os.path.splitext(os.path.basename(pdf_file))[0]
    
    # check if the filename matches the desired name
    if filename == 'desired_name':
        # open the PDF file in read-binary mode
        with open(pdf_file, 'rb') as f:
            # create a PdfFileReader object to read the PDF file
            pdf_reader = PyPDF2.PdfFileReader(f)
            
            # get the number of pages in the PDF file
            num_pages = pdf_reader.getNumPages()
            
            # print the PDF file using the default system PDF viewer
            subprocess.call(['lp', '-d', 'printer_name', '-n', str(num_pages), pdf_file])

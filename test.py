import os
import glob

directory = "C:\\Users\\wddun\\Desktop\\autoprint"
pdf_files = glob.glob(os.path.join(directory, '*.pdf'))
print(pdf_files)

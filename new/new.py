from flask import Flask, render_template, send_file, redirect
import os
import win32print
import win32api

app = Flask(__name__)

# Define the directory to scan for PDFs
pdf_directory = "C:\\Users\\wddun\\Desktop\\autoprint\\autoprint\\new\\pdfs"

# Define a function to get all subdirectories in the PDF directory
def get_subdirectories(directory):
    return [f.name for f in os.scandir(directory) if f.is_dir()]

# Define a function to get all PDF files in a directory
def get_pdf_files(directory):
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

# Define the index page
@app.route('/')
def index():
    subdirectories = get_subdirectories(pdf_directory)
    return render_template('index.html', subdirectories=subdirectories)

# Define the page for a specific subdirectory
@app.route('/<subdirectory>')
def subdirectory(subdirectory):
    pdf_files = get_pdf_files(os.path.join(pdf_directory, subdirectory))
    return render_template('subdirectory.html', subdirectory=subdirectory, pdf_files=pdf_files)

# Define a function to handle printing a PDF file
def print_pdf(pdf_file):
    # Print the PDF file on the server machine's default printer
    win32api.ShellExecute(
        0,
        "print",
        pdf_file,
        '/d:"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )

# Define the route to print a PDF file
@app.route('/print-pdf/<path:pdf_file>')
def print_pdf_route(pdf_file):
    print_pdf(pdf_file)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

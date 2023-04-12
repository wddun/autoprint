import os
from flask import Flask, request, render_template

app = Flask(__name__)

pdfs_dir = 'pdfs'

# Function to generate HTML menu for a list of PDF files
def generate_menu(pdfs):
    menu = '<html><head><title>PDF Files</title></head><body><h1>PDF Files</h1><p>Click on a file name to print it:</p><ul>'
    for pdf in pdfs:
        menu += '<li><a href="' + pdf + '">' + pdf + '</a></li>'
    menu += '</ul></body></html>'
    return menu

# Route for root URL
@app.route('/')
def root():
    subdirs = [d for d in os.listdir(pdfs_dir) if os.path.isdir(os.path.join(pdfs_dir, d))]
    return render_template('main_menu.html', subdirs=subdirs)

# Route for subdirectory URLs
@app.route('/<subdir>/')
def subdir(subdir):
    pdf_dir = os.path.join(pdfs_dir, subdir)
    if not os.path.exists(pdf_dir):
        return 'Error: directory not found'
    pdfs = [f for f in os.listdir(pdf_dir) if os.path.isfile(os.path.join(pdf_dir, f)) and f.endswith('.pdf')]
    menu_html = generate_menu(pdfs)
    with open(os.path.join(pdf_dir, 'index.html'), 'w') as f:
        f.write(menu_html)
    return render_template('sub_menu.html', subdir=subdir, pdfs=pdfs)

# Route for printing PDF files
@app.route('/print')
def print_pdf():
    file = request.args.get('file', '')
    if not file.endswith('.pdf'):
        return 'Error: invalid file format'
    filepath = os.path.join(pdfs_dir, request.args.get('subdir', ''), file)
    os.startfile(filepath, 'print')
    return 'Printing ' + file

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template, send_file, redirect
import os
import win32print
import win32api

app = Flask(__name__)

# Define routes for the two pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

# Define functions to handle button clicks and serve PDF files
@app.route('/pdf1')
def pdf1():
    # Print the PDF file on the server machine's default printer
    win32api.ShellExecute(
        0,
        "print",
        "C:\\Users\\wddun\\Desktop\\autoprint\\resume.pdf",
        '/d:"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )
    return redirect('/')

@app.route('/pdf2')
def pdf2():
    # Print the PDF file on the server machine's default printer
    win32api.ShellExecute(
        0,
        "print",
        "path/to/pdf2.pdf",
        '/d:"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )
    return redirect('/')

@app.route('/pdf3')
def pdf3():
    # Print the PDF file on the server machine's default printer
    win32api.ShellExecute(
        0,
        "print",
        "path/to/pdf3.pdf",
        '/d:"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )
    return redirect('/')

@app.route('/pdf4')
def pdf4():
    # Print the PDF file on the server machine's default printer
    win32api.ShellExecute(
        0,
        "print",
        "path/to/pdf4.pdf",
        '/d:"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)



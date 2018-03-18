from flask import Flask, request, redirect, url_for, send_from_directory, flash
from flask import render_template
from werkzeug.utils import secure_filename
import os
import boto3
import requests

UPLOAD_FOLDER = "static/uploads"  # change this to path
ALLOWED_EXTENSIONS = set(["pdf"])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    """Return boolean for whether or not file is allowable format."""

    extension = filename.split(".")[-1]

    return True if extension in ALLOWED_EXTENSIONS else False


@app.route("/upload-pdf", methods=["POST"])
def upload_pdf():
    """Accepts HTTP POST request containing PDF files - upload to S3 as PNG.

    Returns URL manifest for each page of doc as PNG"""

    if request.method == 'POST':

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))


if __name__ == "__main__":

    app.run(port=5000, host="0.0.0.0")

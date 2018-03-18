from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import boto3
import requests

UPLOAD_FOLDER = '/path/to/the/uploads'  # change this to path
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/upload-pdf", methods=["POST"])
def upload_pdf():
    """Accepts HTTP POST request containing PDF files - upload to S3 as PNG.

    Returns URL manifest for each page of doc as PNG"""

    pass


if __name__ == "__main__":

    app.run(port=5000, host="0.0.0.0")

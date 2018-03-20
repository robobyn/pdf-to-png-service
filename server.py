from flask import Flask, request, send_from_directory
from flask import jsonify
from werkzeug.utils import secure_filename
import os
from image_conversion import allowed_file, get_url_manifest
from wand.image import Image


UPLOAD_FOLDER = "static/uploads"


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.environ["SECRET_KEY"]


@app.route("/upload-pdf", methods=["POST"])
def upload_pdf():
    """Accepts HTTP POST request containing PDF files - convert to PNG.

    Returns URL manifest for each page of doc as PNG"""

    if request.method == 'POST':

        if 'file' not in request.files:
            return jsonify("No file submitted")

        file = request.files['file']
        filename = secure_filename(file.filename)

        if file and allowed_file(filename):

            file.save(filename)

            converted_img = Image(filename=str(filename)).convert("png")
            converted_img.save(filename=os.path.join(app.config['UPLOAD_FOLDER'],
                               "{}.png".format(filename[:-4])))
            os.remove(filename)

            return get_url_manifest(converted_img, filename)

        else:
            return jsonify("/upload-pdf route accepts only .pdf file format.")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Display uploaded file."""

    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":

    app.run(port=8000, host="0.0.0.0")

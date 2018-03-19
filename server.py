from flask import Flask, request, url_for, send_from_directory
from flask import jsonify
from werkzeug.utils import secure_filename
from wand.image import Image
import os

UPLOAD_FOLDER = "static/uploads"  # change this to path
ALLOWED_EXTENSIONS = set(["pdf"])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.environ["SECRET_KEY"]


def allowed_file(filename):
    """Return boolean for whether or not file is allowable format."""

    extension = filename.split(".")[-1]

    return True if extension in ALLOWED_EXTENSIONS else False


@app.route("/upload-pdf", methods=["POST"])
def upload_pdf():
    """Accepts HTTP POST request containing PDF files - convert to PNG.

    Returns URL manifest for each page of doc as PNG"""

    if request.method == 'POST':

        if 'file' not in request.files:
            return jsonify("No file submitted")

        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(filename)

            converted_img = Image(filename=str(filename)).convert("png")
            converted_img.save(filename=os.path.join(app.config['UPLOAD_FOLDER'],
                               "{}.png".format(filename[:-4])))

            url_manifest = []

            if len(converted_img.sequence) > 1:
                for i in range(len(converted_img.sequence)):

                    url = url_for('uploaded_file', filename="{}-{}.png".format(
                        filename[:-4], i))
                    url_manifest.append(url)

                return jsonify(url_manifest)

            else:
                url = url_for('uploaded_file', filename="{}.png".format(
                              filename[:-4]))
                return jsonify([url])

        else:
            return jsonify("/upload-pdf route accepts only .pdf file format.")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Display uploaded file."""

    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":

    app.run(port=8000, host="0.0.0.0")

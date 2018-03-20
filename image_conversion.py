import os
from flask import jsonify
from wand.image import Image
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(["pdf"])


def allowed_file(filename):
    """Return boolean for whether or not file is allowable format."""

    extension = filename.split(".")[-1]

    return True if extension in ALLOWED_EXTENSIONS else False


def convert_to_png(file, filename):
    """Return file converted from PDF to PNG."""

    file.save(filename)

    converted_img = Image(filename=str(filename)).convert("png")
    converted_img.save(filename="/static/uploads/{}.png".format(filename[:-4]))
    os.remove(filename)

    return converted_img


def get_url_manifest(converted_img, filename):
    """Return JSON object containing list of URLs for PNG images for converted_img.
    """

    url_manifest = []

    if len(converted_img.sequence) > 1:
        for i in range(len(converted_img.sequence)):

            url = "http://localhost:8000/uploads/{}-{}.png".format(
                filename[:-4], i)
            url_manifest.append(url)

    else:
        url_manifest.append("http://localhost:8000/uploads/{}.png".format(
            filename[:-4]))

    return jsonify(url_manifest)

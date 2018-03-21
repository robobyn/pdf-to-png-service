from flask import jsonify


def allowed_file(filename):
    """Return boolean for whether or not file is allowable format."""

    allowed_extensions = set(["pdf"])
    extension = filename.split(".")[-1]

    return True if extension in allowed_extensions else False


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

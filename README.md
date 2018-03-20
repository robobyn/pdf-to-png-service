# PDF to PNG

PDF to PNG is an HTTP service that:
* Accepts POST requests containing PDF files
* Returns a manifest formatted as a JSON object containing a list of URLs to PNG
images of the pages of the PDF
* Responds to GET requests for those URLs with the PNG image requested

### Prerequisites

Program written in Python 2.7 using Flask framework version 0.12.2.  This service
uses Wand version 0.4.4, a Python wrapper for ImageMagick, to convert PDF files to
PNG images.  You will need to install ImageMagick version 6 to run this service.
(Version 6 is compatible with 32-bit Python)  Using Mac OSX and homebrew, execute
the following commands:

```
$ brew install imagemagick@6
```

To work with PDF files, ImageMagick depends on GhostScript.

```
$ brew install ghostscript
```

Following these two installs, it is adviseable to use a virtual environment to
install the remaining requirements via pip.

If you don't have pip installed, go [here](https://pip.pypa.io/en/stable/installing/) for instructions.

If you don't have virtualenv, you can install this tool using pip.

To create and activate a virtual environment:

```
$ virtualenv env
$ source env/bin/activate
```

Install Flask and Wand using pip:

```
$ pip install -r requirements.txt
```

Flask requires a secret key to run this application.  Create an environmental
variable called ```SECRET_KEY```.  Use a string of your choosing as the key.

## Getting Started

Download files from Github

Start the server:
```
$ python server.py
```

Choose a PDF to convert and, using a new terminal tab, navigate to the directory
containing that PDF.

Execute the following cURL command from the command line in the directory
containing your PDF:

```
curl -F file=@<filename>.pdf http://localhost:8000/upload-pdf
```

This should return a list of URLs for the PNG images for each page of the PDF.
You will also notice that the uploads file in the pdf-to-png project now
contains the converted PNG images.

To retrieve PNG images, paste the URL for your desired image into a browser,
or cURL the URL into a terminal for a PNG blob.

## Running the tests

To run the tests, you will need to move test documents into the pdf-to-png
directory.  The tests require a single page PDF named test_singlepage.pdf,
a multi-page PDF named test_multipage.pdf, and a JPG named test_nonpdf.jpg.

Once the pdf-to-png contains the appropriate test files, execute this command:
```
python tests.py
```

If all routes are working, this command should return "OK".

## Built With

* [Flask](http://flask.pocoo.org/docs/0.12/) - The web framework used
* [ImageMagick](https://http://www.imagemagick.org/script/index.php) - For PDF
to PNG Image conversion
* [GhostScript](https://www.ghostscript.com/Documentation.html) - ImageMagick
dependency for PDF formatted files
* [Wand](https://developers.eatstreet.com/endpoint/search) - Python wrapper for
ImageMagick

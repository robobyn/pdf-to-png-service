from unittest import TestCase
from server import app
from io import FileIO


class FlaskTestsServer(TestCase):
    """Flask unit tests for server routes."""

    def setUp(self):
        """Set up test client before each test."""

        self.client = app.test_client()
        app.config["TESTING"] = True
        app.config["SECRET_KEY"] = "key"

    def test_no_file(self):
        """Test /upload-pdf route with no file submitted."""

        result = self.client.post("/upload-pdf")

        self.assertIn("No file submitted", result.data)

    def test_single_page_pdf(self):
        """Test /upload-pdf route for single page pdf."""

        data = {"file": FileIO("test_singlepage.pdf")}
        result = self.client.post("/upload-pdf",
                                  content_type="multipart/form-data",
                                  data=data)

        self.assertIn("/uploads/test_singlepage.png", result.data)

    def test_multipage_pdf(self):
        """Test /upload-pdf route for multi page pdf."""

        data = {"file": FileIO("test_multipage.pdf")}
        result = self.client.post("/upload-pdf",
                                  content_type="multipart/form-data",
                                  data=data)

        self.assertIn("/uploads/test_multipage-1.png", result.data)

    def test_wrong_file_type(self):
        """Test /upload-pdf route for non-pdf file upload."""

        data = {"file": FileIO("test_nonpdf.jpg")}
        result = self.client.post("/upload-pdf",
                                  content_type="multipart/form-data",
                                  data=data)

        self.assertIn("/upload-pdf route accepts only .pdf file format.",
                      result.data)


if __name__ == "__main__":
    import unittest

    unittest.main()

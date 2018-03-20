from unittest import TestCase
from server import app


class FlaskTestsServer(TestCase):
    """Flask unit tests for server routes."""

    def setUp(self):
        """Set up test client before each test."""

        self.client = app.test_client()
        app.config["TESTING"] = True
        app.config["SECRET_KEY"] = "key"

    def test_no_file(self):
        """Test /upload-pdf route for single page pdf."""

        result = self.client.post("/upload-pdf")

        self.assertIn("No file submitted", result.data)


if __name__ == "__main__":
    import unittest

    unittest.main()

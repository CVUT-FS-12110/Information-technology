import unittest
import requests
from settings import URL as BASE_URL

class TestSimpleMathServer(unittest.TestCase):

    def test_get_root(self):
        """GET / should return 200 and contain the HTML page."""
        r = requests.get(BASE_URL + "/")
        self.assertEqual(r.status_code, 200)
        self.assertIn("Simple Math Web Server", r.text)

    def test_post_factorial(self):
        """POST / with factorial should return 200 and contain expected result string."""
        payload = {
            "operation": "factorial",
            "number": "5"
        }
        r = requests.post(BASE_URL + "/", data=payload)
        self.assertEqual(r.status_code, 200)
        self.assertIn("Factorial of 5", r.text)

    def test_post_is_prime(self):
        """POST / with is_prime should return 200 and contain expected result string."""
        payload = {
            "operation": "is_prime",
            "number": "7"
        }
        r = requests.post(BASE_URL + "/", data=payload)
        self.assertEqual(r.status_code, 200)
        self.assertIn("Is 7 prime?", r.text)

    def test_post_invalid_input(self):
        """POST with non-numeric value should still return 200 and contain error message."""
        payload = {
            "operation": "factorial",
            "number": "abc"
        }
        r = requests.post(BASE_URL + "/", data=payload)
        self.assertEqual(r.status_code, 200)
        self.assertIn("Error", r.text)

if __name__ == "__main__":
    unittest.main(verbosity=2)

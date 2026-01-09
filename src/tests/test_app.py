import unittest
from app import app

class BasicTests(unittest.TestCase):

    def test_main_page(self):

        tester = app.test_client()
        response = tester.get('/', content_type='text/html')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'DevOps Project 2', response.data)

if __name__ == "__main__":
    unittest.main()
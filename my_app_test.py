# test_hello.py
from app import app
import unittest


class SimpleTest(unittest.TestCase):
    def test_hello(self):
        response = app.test_client().get('/')
        assert response.status_code == 200
        assert response.data == b'<p>Hello, World!</p>'


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch #Part 2
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('app.boto3.client')
    def test_hello(self, mock_boto):
        mock_lambda = mock_boto.return_value #Part 2
        mock_lambda.invoke.return_value = { #Part 2
            'Payload' : type('obj', (), {'read': lambda self: b'{"statusCode": 200, "body": "File uploaded to S3 successfully"}'})() #Part 2
        }
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello, World - I am app build using Flask library! Lambda response: File uploaded to S3 successfully", response.data.decode('utf-8'))

if __name__ == "__main__":
    unittest.main()
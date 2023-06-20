# Python Standard Library Imports
from unittest.mock import patch

# Other Third Party Imports
import requests
from requests import RequestException

# First Party Imports
from paymob.accept.connection import AcceptConnection
from paymob.data_classes import ResponseFeedBack
from paymob.response_codes import (
    HTTP_EXCEPTION,
    HTTP_EXCEPTION_MESSAGE,
    JSON_DECODE_EXCEPTION,
    JSON_DECODE_EXCEPTION_MESSAGE,
    REQUEST_EXCEPTION,
    REQUEST_EXCEPTION_MESSAGE,
    SUCCESS,
    SUCCESS_MESSAGE,
    UNHANDLED_EXCEPTION,
    UNHANDLED_EXCEPTION_MESSAGE,
)
from tests.factories import ResponseFactory
from tests.utils import AbstractTestCase


class TestAcceptConnection(AbstractTestCase):
    """Test AcceptConnection Class"""

    # =========== Start __init__ Tests =======
    # Test cases to verify the initialization process of the connection

    @patch.object(AcceptConnection, "_get_headers")
    @patch.object(AcceptConnection, "_get_auth_token")
    def test__init__success(self, mock_get_auth_token, mock_get_headers):
        """test __init__: Success"""
        mock_get_auth_token.return_value = "****"
        mock_get_headers.return_value = {}

        AcceptConnection()

        self.assertTrue(mock_get_auth_token.called)
        self.assertTrue(mock_get_headers.called)

    # ======= End __init__ Tests =======

    # ======= Start _get_headers Tests =======
    # Test cases to verify that request headers is successfully generated

    @patch.object(AcceptConnection, "_get_auth_token")
    def test_get_headers_success(self, mock_get_auth_token):
        """test _get_headers: success"""

        mock_get_auth_token.return_value = "****"

        connection = AcceptConnection()
        actual_headers = connection._get_headers()
        expected_headers = {
            "Content-Type": "application/json",
            "Authorization": f"{connection.auth_token}",
        }
        self.assertEqual(actual_headers, expected_headers)
        self.assertTrue(mock_get_auth_token.called)

    # ======= End _get_headers Tests =======

    # ======= Start _get_auth_token Tests ========
    # Test cases to verify the process of retreiving auth token

    @patch.object(AcceptConnection, "post")
    @patch.object(AcceptConnection, "_get_headers")
    def test_get_auth_token_code_is_not_success(self, mock_get_headers, mock_post):
        """test _get_auth_token: Code is not SUCCESS"""

        mock_get_headers.return_value = {}
        mock_post.return_value = HTTP_EXCEPTION, ResponseFeedBack(message=HTTP_EXCEPTION_MESSAGE)

        connection = AcceptConnection()
        auth_token = connection._get_auth_token()

        self.assertIsNone(auth_token)
        self.assertTrue(mock_get_headers.called)
        self.assertTrue(mock_post.called)

    @patch.object(AcceptConnection, "post")
    @patch.object(AcceptConnection, "_get_headers")
    def test_get_auth_token_success(self, mock_get_headers, mock_post):
        """test _get_auth_token: Code is SUCCESS"""

        expected_token = "*****"
        mock_get_headers.return_value = {}
        mock_post.return_value = SUCCESS, ResponseFeedBack(
            message=HTTP_EXCEPTION_MESSAGE,
            data={"token": expected_token},
        )

        connection = AcceptConnection()
        actual_auth_token = connection._get_auth_token()

        self.assertEqual(actual_auth_token, expected_token)
        self.assertTrue(mock_get_headers.called)
        self.assertTrue(mock_post.called)

    # ======= End _get_auth_token Tests ========

    # ======= Start get Tests ========
    # Test cases to verify the get wrapper catch the exceptions properly

    @patch.object(requests.Session, "get")
    @patch.object(AcceptConnection, "_get_headers")
    @patch.object(AcceptConnection, "_get_auth_token")
    def test_get_json_decode_exception(self, mock_get_auth_token, mock_get_headers, mock_get):
        """test get: json decode Exception"""

        mock_get_auth_token.return_value = "****"
        mock_get_headers.return_value = {}
        mock_get.return_value = ResponseFactory(json_data=None, status_code=400)

        connection = AcceptConnection()
        code, feedback = connection.get()

        self.assertEqual(code, JSON_DECODE_EXCEPTION)
        self.assertIsNone(feedback.data)
        self.assertIsInstance(feedback, ResponseFeedBack)
        self.assertEqual(feedback.message, JSON_DECODE_EXCEPTION_MESSAGE)
        self.assertEqual(feedback.status_code, 400)
        self.assertIsNotNone(feedback.exception_error)

        self.assertTrue(mock_get_auth_token.called)
        self.assertTrue(mock_get_headers.called)
        self.assertTrue(mock_get.called)

    @patch.object(requests.Session, "get")
    @patch.object(AcceptConnection, "_get_headers")
    @patch.object(AcceptConnection, "_get_auth_token")
    def test_get_http_exception(self, mock_get_auth_token, mock_get_headers, mock_get):
        """test get: HTTP Exception"""

        mock_get_auth_token.return_value = "****"
        mock_get_headers.return_value = {}
        mock_get.return_value = ResponseFactory(json_data={}, status_code=400)

        connection = AcceptConnection()
        code, feedback = connection.get()

        self.assertEqual(code, HTTP_EXCEPTION)
        self.assertEqual(feedback.data, {})
        self.assertIsInstance(feedback, ResponseFeedBack)
        self.assertEqual(feedback.message, HTTP_EXCEPTION_MESSAGE)
        self.assertEqual(feedback.status_code, 400)
        self.assertIsNotNone(feedback.exception_error)

        self.assertTrue(mock_get_auth_token.called)
        self.assertTrue(mock_get_headers.called)
        self.assertTrue(mock_get.called)

    @patch.object(requests.Session, "get")
    @patch.object(AcceptConnection, "_get_headers")
    @patch.object(AcceptConnection, "_get_auth_token")
    def test_get_request_exception(self, mock_get_auth_token, mock_get_headers, mock_get):
        """test get: Request Exception"""

        mock_get_auth_token.return_value = "****"
        mock_get_headers.return_value = {}
        mock_get.side_effect = RequestException("Boom!")

        connection = AcceptConnection()
        code, feedback = connection.get()

        self.assertEqual(code, REQUEST_EXCEPTION)
        self.assertIsNone(feedback.data)
        self.assertIsInstance(feedback, ResponseFeedBack)
        self.assertEqual(feedback.message, REQUEST_EXCEPTION_MESSAGE)
        self.assertIsNone(feedback.status_code)
        self.assertIsNotNone(feedback.exception_error)

        self.assertTrue(mock_get_auth_token.called)
        self.assertTrue(mock_get_headers.called)
        self.assertTrue(mock_get.called)

    @patch.object(requests.Session, "get")
    @patch.object(AcceptConnection, "_get_headers")
    @patch.object(AcceptConnection, "_get_auth_token")
    def test_get_unhandled_exception(self, mock_get_auth_token, mock_get_headers, mock_get):
        """test get: Unhandled Exception"""

        mock_get_auth_token.return_value = "****"
        mock_get_headers.return_value = {}
        mock_get.side_effect = Exception("Boom!")

        connection = AcceptConnection()
        code, feedback = connection.get()

        self.assertEqual(code, UNHANDLED_EXCEPTION)
        self.assertIsNone(feedback.data)
        self.assertIsInstance(feedback, ResponseFeedBack)
        self.assertEqual(feedback.message, UNHANDLED_EXCEPTION_MESSAGE)
        self.assertIsNone(feedback.status_code)
        self.assertIsNotNone(feedback.exception_error)

        self.assertTrue(mock_get_auth_token.called)
        self.assertTrue(mock_get_headers.called)
        self.assertTrue(mock_get.called)

    @patch.object(requests.Session, "get")
    @patch.object(AcceptConnection, "_get_headers")
    @patch.object(AcceptConnection, "_get_auth_token")
    def test_get_success(self, mock_get_auth_token, mock_get_headers, mock_get):
        """test get: Success"""

        mock_get_auth_token.return_value = "****"
        mock_get_headers.return_value = {}
        mock_get.return_value = ResponseFactory(json_data={}, status_code=200)

        connection = AcceptConnection()
        code, feedback = connection.get()

        self.assertEqual(code, SUCCESS)
        self.assertEqual(feedback.data, {})
        self.assertIsInstance(feedback, ResponseFeedBack)
        self.assertEqual(feedback.message, SUCCESS_MESSAGE)
        self.assertEqual(feedback.status_code, 200)
        self.assertIsNone(feedback.exception_error)

        self.assertTrue(mock_get_auth_token.called)
        self.assertTrue(mock_get_headers.called)
        self.assertTrue(mock_get.called)

    # ======= End get Tests ========

    # ======= Start get Tests ========
    # Test cases to verify the get wrapper catch the exceptions properly

    @patch.object(requests.Session, "post")
    @patch.object(AcceptConnection, "_get_headers")
    @patch.object(AcceptConnection, "_get_auth_token")
    def test_post_json_decode_exception(self, mock_get_auth_token, mock_get_headers, mock_post):
        """test post: json decode Exception"""

        mock_get_auth_token.return_value = "****"
        mock_get_headers.return_value = {}
        mock_post.return_value = ResponseFactory(json_data=None, status_code=400)

        connection = AcceptConnection()
        code, feedback = connection.post()

        self.assertEqual(code, JSON_DECODE_EXCEPTION)
        self.assertIsNone(feedback.data)
        self.assertIsInstance(feedback, ResponseFeedBack)
        self.assertEqual(feedback.message, JSON_DECODE_EXCEPTION_MESSAGE)
        self.assertEqual(feedback.status_code, 400)
        self.assertIsNotNone(feedback.exception_error)

        self.assertTrue(mock_get_auth_token.called)
        self.assertTrue(mock_get_headers.called)
        self.assertTrue(mock_post.called)

    @patch.object(requests.Session, "post")
    @patch.object(AcceptConnection, "_get_headers")
    @patch.object(AcceptConnection, "_get_auth_token")
    def test_post_json_http_exception(self, mock_get_auth_token, mock_get_headers, mock_post):
        """test get: HTTP Exception"""

        mock_get_auth_token.return_value = "****"
        mock_get_headers.return_value = {}
        mock_post.return_value = ResponseFactory(json_data={}, status_code=400)

        connection = AcceptConnection()
        code, feedback = connection.post()

        self.assertEqual(code, HTTP_EXCEPTION)
        self.assertEqual(feedback.data, {})
        self.assertIsInstance(feedback, ResponseFeedBack)
        self.assertEqual(feedback.message, HTTP_EXCEPTION_MESSAGE)

        self.assertEqual(feedback.status_code, 400)

        self.assertTrue(mock_get_auth_token.called)
        self.assertTrue(mock_get_headers.called)
        self.assertTrue(mock_post.called)

    @patch.object(requests.Session, "post")
    @patch.object(AcceptConnection, "_get_headers")
    @patch.object(AcceptConnection, "_get_auth_token")
    def test_post_request_exception(self, mock_get_auth_token, mock_get_headers, mock_post):
        """test post: Request Exception"""

        mock_get_auth_token.return_value = "****"
        mock_get_headers.return_value = {}
        mock_post.side_effect = RequestException("Boom!")

        connection = AcceptConnection()
        code, feedback = connection.post()

        self.assertEqual(code, REQUEST_EXCEPTION)
        self.assertIsNone(feedback.data)
        self.assertIsInstance(feedback, ResponseFeedBack)
        self.assertEqual(feedback.message, REQUEST_EXCEPTION_MESSAGE)
        self.assertIsNone(feedback.status_code)
        self.assertIsNotNone(feedback.exception_error)

        self.assertTrue(mock_get_auth_token.called)
        self.assertTrue(mock_get_headers.called)
        self.assertTrue(mock_post.called)

    @patch.object(requests.Session, "post")
    @patch.object(AcceptConnection, "_get_headers")
    @patch.object(AcceptConnection, "_get_auth_token")
    def test_post_unhandled_exception(self, mock_get_auth_token, mock_get_headers, mock_post):
        """test post: Unhandled Exception"""

        mock_get_auth_token.return_value = "****"
        mock_get_headers.return_value = {}
        mock_post.side_effect = Exception("Boom!")

        connection = AcceptConnection()
        code, feedback = connection.post()

        self.assertEqual(code, UNHANDLED_EXCEPTION)
        self.assertIsNone(feedback.data)
        self.assertIsInstance(feedback, ResponseFeedBack)
        self.assertEqual(feedback.message, UNHANDLED_EXCEPTION_MESSAGE)
        self.assertIsNone(feedback.status_code)
        self.assertIsNotNone(feedback.exception_error)

        self.assertTrue(mock_get_auth_token.called)
        self.assertTrue(mock_get_headers.called)
        self.assertTrue(mock_post.called)

    @patch.object(requests.Session, "post")
    @patch.object(AcceptConnection, "_get_headers")
    @patch.object(AcceptConnection, "_get_auth_token")
    def test_post_success(self, mock_get_auth_token, mock_get_headers, mock_post):
        """test post: Success"""

        mock_get_auth_token.return_value = "****"
        mock_get_headers.return_value = {}
        mock_post.return_value = ResponseFactory(json_data={}, status_code=200)

        connection = AcceptConnection()
        code, feedback = connection.post()

        self.assertEqual(code, SUCCESS)
        self.assertEqual(feedback.data, {})
        self.assertIsInstance(feedback, ResponseFeedBack)
        self.assertEqual(feedback.message, SUCCESS_MESSAGE)
        self.assertEqual(feedback.status_code, 200)
        self.assertIsNone(feedback.exception_error)

        self.assertTrue(mock_get_auth_token.called)
        self.assertTrue(mock_get_headers.called)
        self.assertTrue(mock_post.called)

    # ======= End post Tests ========

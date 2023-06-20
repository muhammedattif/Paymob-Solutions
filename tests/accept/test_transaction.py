# Python Standard Library Imports
from unittest.mock import patch

# First Party Imports
from paymob.accept.config import URLsConfig
from paymob.accept.connection import AcceptConnection
from paymob.accept.transaction import Transaction
from paymob.data_classes import ResponseFeedBack
from paymob.response_codes import HTTP_EXCEPTION, HTTP_EXCEPTION_MESSAGE, SUCCESS, SUCCESS_MESSAGE
from tests.utils import AbstractTestCase


class TestTransaction(AbstractTestCase):
    """Test Transaction Class"""

    # =========== Start refund Tests =======
    # Test cases to verify that Transaction refund process is working properly

    @patch.object(AcceptConnection, "post")
    def test_refund_code_is_not_success(self, mock_post):
        """test refund: Code is not Success"""
        mock_post.return_value = HTTP_EXCEPTION, ResponseFeedBack(message=HTTP_EXCEPTION_MESSAGE)

        transaction_data = {"id": 1}
        transaction = Transaction(connection=AcceptConnection, **transaction_data)
        amount_cents = 1000
        code, refund_transaction, feedback = transaction.refund(
            amount_cents=amount_cents,
        )
        self.assertEqual(code, HTTP_EXCEPTION)
        self.assertIsNone(refund_transaction)
        self.assertEqual(feedback.message, HTTP_EXCEPTION_MESSAGE)
        self.assertTrue(mock_post.called)

        request_body = {
            "transaction_id": transaction_data.get("id"),
            "amount_cents": amount_cents,
        }
        mock_post.assert_called_with(url=URLsConfig.REFUND_TRANSACTION, json=request_body)

    @patch.object(AcceptConnection, "post")
    def test_refund_success(self, mock_post):
        """test refund: Success"""
        refund_transaction_data = {"id": 2}
        mock_post.return_value = SUCCESS, ResponseFeedBack(
            message=SUCCESS_MESSAGE,
            data=refund_transaction_data,
        )

        transaction_data = {"id": 1}
        transaction = Transaction(connection=AcceptConnection, **transaction_data)
        amount_cents = 1000
        code, refund_transaction, feedback = transaction.refund(
            amount_cents=amount_cents,
        )
        self.assertEqual(code, SUCCESS)
        self.assertEqual(refund_transaction.id, refund_transaction_data.get("id"))
        self.assertEqual(feedback.data, refund_transaction_data)
        self.assertTrue(mock_post.called)

        request_body = {
            "transaction_id": transaction_data.get("id"),
            "amount_cents": amount_cents,
        }
        mock_post.assert_called_with(url=URLsConfig.REFUND_TRANSACTION, json=request_body)

    # ======= End refund Tests =======

    # =========== Start capture Tests =======
    # Test cases to verify that Transaction capture process is working properly

    @patch.object(AcceptConnection, "post")
    def test_capture_code_is_not_success(self, mock_post):
        """test capture: Code is not Success"""
        mock_post.return_value = HTTP_EXCEPTION, ResponseFeedBack(message=HTTP_EXCEPTION_MESSAGE)

        transaction_data = {"id": 1}
        transaction = Transaction(connection=AcceptConnection, **transaction_data)
        amount_cents = 1000
        code, refund_transaction, feedback = transaction.capture(
            amount_cents=amount_cents,
        )
        self.assertEqual(code, HTTP_EXCEPTION)
        self.assertIsNone(refund_transaction)
        self.assertEqual(feedback.message, HTTP_EXCEPTION_MESSAGE)
        self.assertTrue(mock_post.called)

        request_body = {
            "transaction_id": transaction_data.get("id"),
            "amount_cents": amount_cents,
        }
        mock_post.assert_called_with(url=URLsConfig.CAPTURE_TRANSACTION, json=request_body)

    @patch.object(AcceptConnection, "post")
    def test_capture_success(self, mock_post):
        """test capture: Success"""
        capture_transaction_data = {"id": 2}
        mock_post.return_value = SUCCESS, ResponseFeedBack(
            message=SUCCESS_MESSAGE,
            data=capture_transaction_data,
        )

        transaction_data = {"id": 1}
        transaction = Transaction(connection=AcceptConnection, **transaction_data)
        amount_cents = 1000
        code, capture_transaction, feedback = transaction.capture(
            amount_cents=amount_cents,
        )
        self.assertEqual(code, SUCCESS)
        self.assertEqual(capture_transaction.id, capture_transaction_data.get("id"))
        self.assertEqual(feedback.data, capture_transaction_data)
        self.assertTrue(mock_post.called)

        request_body = {
            "transaction_id": transaction_data.get("id"),
            "amount_cents": amount_cents,
        }
        mock_post.assert_called_with(url=URLsConfig.CAPTURE_TRANSACTION, json=request_body)

    # ======= End capture Tests =======

    # =========== Start capture Tests =======
    # Test cases to verify that Transaction capture process is working properly

    @patch.object(AcceptConnection, "post")
    def test_void_code_is_not_success(self, mock_post):
        """test void: Code is not Success"""
        mock_post.return_value = HTTP_EXCEPTION, ResponseFeedBack(message=HTTP_EXCEPTION_MESSAGE)

        transaction_data = {"id": 1}
        transaction = Transaction(connection=AcceptConnection, **transaction_data)
        code, void_transaction, feedback = transaction.void()
        self.assertEqual(code, HTTP_EXCEPTION)
        self.assertIsNone(void_transaction)
        self.assertEqual(feedback.message, HTTP_EXCEPTION_MESSAGE)
        self.assertTrue(mock_post.called)

        request_body = {
            "transaction_id": transaction_data.get("id"),
        }
        mock_post.assert_called_with(url=URLsConfig.VOID_TRANSACTION, json=request_body)

    @patch.object(AcceptConnection, "post")
    def test_void_success(self, mock_post):
        """test void: Success"""
        void_transaction_data = {"id": 2}
        mock_post.return_value = SUCCESS, ResponseFeedBack(
            message=SUCCESS_MESSAGE,
            data=void_transaction_data,
        )

        transaction_data = {"id": 1}
        transaction = Transaction(connection=AcceptConnection, **transaction_data)
        code, void_transaction, feedback = transaction.void()
        self.assertEqual(code, SUCCESS)
        self.assertEqual(void_transaction.id, void_transaction_data.get("id"))
        self.assertEqual(feedback.data, void_transaction_data)
        self.assertTrue(mock_post.called)

        request_body = {
            "transaction_id": transaction_data.get("id"),
        }
        mock_post.assert_called_with(url=URLsConfig.VOID_TRANSACTION, json=request_body)

    # ======= End void Tests =======

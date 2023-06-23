# Python Standard Library Imports
from unittest.mock import patch

# First Party Imports
from paymob.accept import AcceptAPIClient
from paymob.accept.config import URLsConfig
from paymob.accept.connection import AcceptConnection
from paymob.accept.constants import PaymentSubTypes
from paymob.data_classes import ResponseFeedBack
from paymob.response_codes import HTTP_EXCEPTION, HTTP_EXCEPTION_MESSAGE, SUCCESS, SUCCESS_MESSAGE
from tests.utils import AbstractTestCase


class TestAcceptClient(AbstractTestCase):
    """Test AcceptClient Class"""

    # =========== Start create_order Tests =======
    # Test cases to verify that order creation process is working properly

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_create_order_code_is_not_success(self, mock_accept_connection, mock_post):
        """test create_order: Code is not Success"""
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = HTTP_EXCEPTION, ResponseFeedBack(message=HTTP_EXCEPTION_MESSAGE)

        accept_api_client = AcceptAPIClient()
        merchant_order_id = "Test"
        amount_cents = "1000"
        currency = "EGP"
        code, order_instance, feedback = accept_api_client.create_order(
            merchant_order_id=merchant_order_id,
            amount_cents=amount_cents,
            currency=currency,
        )
        self.assertEqual(code, HTTP_EXCEPTION)
        self.assertIsNone(order_instance)
        self.assertEqual(feedback.message, HTTP_EXCEPTION_MESSAGE)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "merchant_order_id": merchant_order_id,
            "amount_cents": str(amount_cents),
            "currency": currency,
            "delivery_needed": False,
            "items": [],
            "shipping_data": {},
            "shipping_details": {},
        }
        mock_post.assert_called_with(url=URLsConfig.CREATE_ORDER, json=request_body)

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_create_order_success(self, mock_accept_connection, mock_post):
        """test create_order: Success"""
        order_data = {"id": 1}
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = SUCCESS, ResponseFeedBack(
            message=SUCCESS_MESSAGE,
            data=order_data,
        )

        accept_api_client = AcceptAPIClient()
        merchant_order_id = "Test"
        amount_cents = "1000"
        currency = "EGP"
        code, order_instance, feedback = accept_api_client.create_order(
            merchant_order_id=merchant_order_id,
            amount_cents=amount_cents,
            currency=currency,
        )
        self.assertEqual(code, SUCCESS)
        self.assertEqual(order_instance.id, order_data.get("id"))
        self.assertEqual(feedback.data, order_data)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "merchant_order_id": merchant_order_id,
            "amount_cents": str(amount_cents),
            "currency": currency,
            "delivery_needed": False,
            "items": [],
            "shipping_data": {},
            "shipping_details": {},
        }
        mock_post.assert_called_with(url=URLsConfig.CREATE_ORDER, json=request_body)

    # ======= End create_order Tests =======

    # =========== Start get_order Tests =======
    # Test cases to verify that order retreived successfully

    @patch.object(AcceptConnection, "get")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_get_order_code_is_not_success(self, mock_accept_connection, mock_get):
        """test get_order: Code is not Success"""
        mock_accept_connection.return_value = AcceptConnection
        mock_get.return_value = HTTP_EXCEPTION, ResponseFeedBack(message=HTTP_EXCEPTION_MESSAGE)

        accept_api_client = AcceptAPIClient()
        order_id = "1"
        code, order_instance, feedback = accept_api_client.get_order(
            order_id=order_id,
        )
        self.assertEqual(code, HTTP_EXCEPTION)
        self.assertIsNone(order_instance)
        self.assertEqual(feedback.message, HTTP_EXCEPTION_MESSAGE)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_get.called)

        mock_get.assert_called_with(url=URLsConfig.GET_ORDER.format(order_id=order_id))

    @patch.object(AcceptConnection, "get")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_get_order_success(self, mock_accept_connection, mock_get):
        """test get_order: Success"""
        order_id = "1"
        order_data = {"id": order_id}
        mock_accept_connection.return_value = AcceptConnection
        mock_get.return_value = SUCCESS, ResponseFeedBack(
            message=SUCCESS_MESSAGE,
            data=order_data,
        )

        accept_api_client = AcceptAPIClient()
        code, order_instance, feedback = accept_api_client.get_order(
            order_id=order_id,
        )
        self.assertEqual(code, SUCCESS)
        self.assertEqual(order_instance.id, order_data.get("id"))
        self.assertEqual(feedback.data, order_data)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_get.called)

        mock_get.assert_called_with(url=URLsConfig.GET_ORDER.format(order_id=order_id))

    # ======= End get_order Tests =======

    # =========== Start create_payment_key Tests =======
    # Test cases to verify that payment key created successfully

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_create_payment_key_code_is_not_success(self, mock_accept_connection, mock_post):
        """test create_payment_key: Code is not Success"""
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = HTTP_EXCEPTION, ResponseFeedBack(message=HTTP_EXCEPTION_MESSAGE)

        accept_api_client = AcceptAPIClient()
        order_id = 1
        amount_cents = "1000"
        currency = "EGP"
        billing_data = {}
        integration_id = 112233
        code, payment_key, feedback = accept_api_client.create_payment_key(
            order_id=order_id,
            amount_cents=amount_cents,
            currency=currency,
            billing_data=billing_data,
            integration_id=integration_id,
        )
        self.assertEqual(code, HTTP_EXCEPTION)
        self.assertIsNone(payment_key)
        self.assertEqual(feedback.message, HTTP_EXCEPTION_MESSAGE)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "order_id": order_id,
            "amount_cents": str(amount_cents),
            "currency": str(currency),
            "expiration": 3600,
            "integration_id": integration_id,
            "billing_data": billing_data,
            "lock_order_when_paid": False,
        }
        mock_post.assert_called_with(url=URLsConfig.PAYMENT_KEY, json=request_body)

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_create_payment_key_success(self, mock_accept_connection, mock_post):
        """test create_payment_key: Success"""

        payment_key_data = {"token": "*****"}
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = SUCCESS, ResponseFeedBack(
            message=SUCCESS_MESSAGE,
            data=payment_key_data,
        )

        accept_api_client = AcceptAPIClient()
        order_id = 1
        amount_cents = "1000"
        currency = "EGP"
        billing_data = {}
        integration_id = 112233
        code, payment_key, feedback = accept_api_client.create_payment_key(
            order_id=order_id,
            amount_cents=amount_cents,
            currency=currency,
            billing_data=billing_data,
            integration_id=integration_id,
        )
        self.assertEqual(code, SUCCESS)
        self.assertEqual(payment_key, payment_key_data.get("token"))
        self.assertEqual(feedback.data, payment_key_data)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "order_id": order_id,
            "amount_cents": str(amount_cents),
            "currency": str(currency),
            "expiration": 3600,
            "integration_id": integration_id,
            "billing_data": billing_data,
            "lock_order_when_paid": False,
        }
        mock_post.assert_called_with(url=URLsConfig.PAYMENT_KEY, json=request_body)

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_create_payment_key_card_token_success(self, mock_accept_connection, mock_post):
        """test create_payment_key: Success"""

        payment_key_data = {"token": "*****"}
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = SUCCESS, ResponseFeedBack(
            message=SUCCESS_MESSAGE,
            data=payment_key_data,
        )

        accept_api_client = AcceptAPIClient()
        order_id = 1
        amount_cents = "1000"
        currency = "EGP"
        billing_data = {}
        integration_id = 112233
        card_token_key = "*****"
        code, payment_key, feedback = accept_api_client.create_payment_key(
            order_id=order_id,
            amount_cents=amount_cents,
            currency=currency,
            billing_data=billing_data,
            integration_id=integration_id,
            card_token_key=card_token_key,
        )
        self.assertEqual(code, SUCCESS)
        self.assertEqual(payment_key, payment_key_data.get("token"))
        self.assertEqual(feedback.data, payment_key_data)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "order_id": order_id,
            "amount_cents": str(amount_cents),
            "currency": str(currency),
            "expiration": 3600,
            "integration_id": integration_id,
            "billing_data": billing_data,
            "lock_order_when_paid": False,
            "token": card_token_key,
        }
        mock_post.assert_called_with(url=URLsConfig.PAYMENT_KEY, json=request_body)

    # ======= End create_payment_key Tests =======

    # =========== Start proceed_kiosk_payment Tests =======
    # Test cases to verify that processing Kiosk payment working properly

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_proceed_kiosk_payment_code_is_not_success(self, mock_accept_connection, mock_post):
        """test proceed_kiosk_payment: Code is not Success"""
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = HTTP_EXCEPTION, ResponseFeedBack(message=HTTP_EXCEPTION_MESSAGE)

        accept_api_client = AcceptAPIClient()
        payment_key = "*****"
        code, transaction_instance, feedback = accept_api_client.proceed_kiosk_payment(
            payment_key=payment_key,
        )
        self.assertEqual(code, HTTP_EXCEPTION)
        self.assertIsNone(transaction_instance)
        self.assertEqual(feedback.message, HTTP_EXCEPTION_MESSAGE)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "source": {
                "identifier": PaymentSubTypes.AGGREGATOR,
                "subtype": PaymentSubTypes.AGGREGATOR,
            },
            "payment_token": payment_key,
        }
        mock_post.assert_called_with(url=URLsConfig.PAY, json=request_body)

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_proceed_kiosk_payment_success(self, mock_accept_connection, mock_post):
        """test proceed_kiosk_payment: Success"""
        transaction_id = "1"
        transaction_data = {"id": transaction_id}
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = SUCCESS, ResponseFeedBack(
            message=SUCCESS_MESSAGE,
            data=transaction_data,
        )

        accept_api_client = AcceptAPIClient()
        payment_key = "*****"
        code, transaction_instance, feedback = accept_api_client.proceed_kiosk_payment(
            payment_key=payment_key,
        )
        self.assertEqual(code, SUCCESS)
        self.assertEqual(transaction_instance.id, transaction_data.get("id"))
        self.assertEqual(feedback.data, transaction_data)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "source": {
                "identifier": PaymentSubTypes.AGGREGATOR,
                "subtype": PaymentSubTypes.AGGREGATOR,
            },
            "payment_token": payment_key,
        }
        mock_post.assert_called_with(url=URLsConfig.PAY, json=request_body)

    # ======= End proceed_kiosk_payment Tests =======

    # =========== Start proceed_wallet_payment Tests =======
    # Test cases to verify that processing Wallet payment working properly

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_proceed_wallet_payment_code_is_not_success(self, mock_accept_connection, mock_post):
        """test proceed_wallet_payment: Code is not Success"""
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = HTTP_EXCEPTION, ResponseFeedBack(message=HTTP_EXCEPTION_MESSAGE)

        accept_api_client = AcceptAPIClient()
        payment_key = "*****"
        identifier = "01000000000"
        code, transaction_instance, feedback = accept_api_client.proceed_wallet_payment(
            payment_key=payment_key,
            identifier=identifier,
        )
        self.assertEqual(code, HTTP_EXCEPTION)
        self.assertIsNone(transaction_instance)
        self.assertEqual(feedback.message, HTTP_EXCEPTION_MESSAGE)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "source": {
                "identifier": identifier,
                "subtype": PaymentSubTypes.WALLET,
            },
            "payment_token": payment_key,
        }
        mock_post.assert_called_with(url=URLsConfig.PAY, json=request_body)

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_proceed_wallet_payment_success(self, mock_accept_connection, mock_post):
        """test proceed_wallet_payment: Success"""
        transaction_id = "1"
        transaction_data = {"id": transaction_id}
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = SUCCESS, ResponseFeedBack(
            message=SUCCESS_MESSAGE,
            data=transaction_data,
        )

        accept_api_client = AcceptAPIClient()
        payment_key = "*****"
        identifier = "01000000000"
        code, transaction_instance, feedback = accept_api_client.proceed_wallet_payment(
            payment_key=payment_key,
            identifier=identifier,
        )
        self.assertEqual(code, SUCCESS)
        self.assertEqual(transaction_instance.id, transaction_data.get("id"))
        self.assertEqual(feedback.data, transaction_data)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "source": {
                "identifier": identifier,
                "subtype": PaymentSubTypes.WALLET,
            },
            "payment_token": payment_key,
        }
        mock_post.assert_called_with(url=URLsConfig.PAY, json=request_body)

    # ======= End proceed_wallet_payment Tests =======

    # =========== Start proceed_cash_payment Tests =======
    # Test cases to verify that processing Cash payment working properly

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_proceed_cash_payment_code_is_not_success(self, mock_accept_connection, mock_post):
        """test proceed_cash_payment: Code is not Success"""
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = HTTP_EXCEPTION, ResponseFeedBack(message=HTTP_EXCEPTION_MESSAGE)

        accept_api_client = AcceptAPIClient()
        payment_key = "*****"
        code, transaction_instance, feedback = accept_api_client.proceed_cash_payment(
            payment_key=payment_key,
        )
        self.assertEqual(code, HTTP_EXCEPTION)
        self.assertIsNone(transaction_instance)
        self.assertEqual(feedback.message, HTTP_EXCEPTION_MESSAGE)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "source": {
                "identifier": PaymentSubTypes.CASH.lower(),
                "subtype": PaymentSubTypes.CASH,
            },
            "payment_token": payment_key,
        }
        mock_post.assert_called_with(url=URLsConfig.PAY, json=request_body)

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_proceed_cash_payment_success(self, mock_accept_connection, mock_post):
        """test proceed_cash_payment: Success"""
        transaction_id = "1"
        transaction_data = {"id": transaction_id}
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = SUCCESS, ResponseFeedBack(
            message=SUCCESS_MESSAGE,
            data=transaction_data,
        )

        accept_api_client = AcceptAPIClient()
        payment_key = "*****"
        code, transaction_instance, feedback = accept_api_client.proceed_cash_payment(
            payment_key=payment_key,
        )
        self.assertEqual(code, SUCCESS)
        self.assertEqual(transaction_instance.id, transaction_data.get("id"))
        self.assertEqual(feedback.data, transaction_data)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "source": {
                "identifier": PaymentSubTypes.CASH.lower(),
                "subtype": PaymentSubTypes.CASH,
            },
            "payment_token": payment_key,
        }
        mock_post.assert_called_with(url=URLsConfig.PAY, json=request_body)

    # ======= End proceed_cash_payment Tests =======

    # =========== Start proceed_card_token_payment Tests =======
    # Test cases to verify that processing Card Token payment working properly

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_proceed_card_token_payment_code_is_not_success(self, mock_accept_connection, mock_post):
        """test proceed_card_token_payment: Code is not Success"""
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = HTTP_EXCEPTION, ResponseFeedBack(message=HTTP_EXCEPTION_MESSAGE)

        accept_api_client = AcceptAPIClient()
        payment_key = "*****"
        card_token = "******"
        code, transaction_instance, feedback = accept_api_client.proceed_card_token_payment(
            payment_key=payment_key,
            card_token=card_token,
        )
        self.assertEqual(code, HTTP_EXCEPTION)
        self.assertIsNone(transaction_instance)
        self.assertEqual(feedback.message, HTTP_EXCEPTION_MESSAGE)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "source": {
                "identifier": card_token,
                "subtype": PaymentSubTypes.TOKEN,
            },
            "payment_token": payment_key,
        }
        mock_post.assert_called_with(url=URLsConfig.PAY, json=request_body)

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_proceed_card_token_payment_success(self, mock_accept_connection, mock_post):
        """test proceed_card_token_payment: Success"""
        transaction_id = "1"
        transaction_data = {"id": transaction_id}
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = SUCCESS, ResponseFeedBack(
            message=SUCCESS_MESSAGE,
            data=transaction_data,
        )

        accept_api_client = AcceptAPIClient()
        payment_key = "*****"
        card_token = "******"
        code, transaction_instance, feedback = accept_api_client.proceed_card_token_payment(
            payment_key=payment_key,
            card_token=card_token,
        )
        self.assertEqual(code, SUCCESS)
        self.assertEqual(transaction_instance.id, transaction_data.get("id"))
        self.assertEqual(feedback.data, transaction_data)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "source": {
                "identifier": card_token,
                "subtype": PaymentSubTypes.TOKEN,
            },
            "payment_token": payment_key,
        }
        mock_post.assert_called_with(url=URLsConfig.PAY, json=request_body)

    # ======= End proceed_card_token_payment Tests =======

    # =========== Start create_invoice_link Tests =======
    # Test cases to verify that Creating Invoice Link working properly

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_create_invoice_link_code_is_not_success(self, mock_accept_connection, mock_post):
        """test create_invoice_link: Code is not Success"""
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = HTTP_EXCEPTION, ResponseFeedBack(message=HTTP_EXCEPTION_MESSAGE)

        accept_api_client = AcceptAPIClient()

        amount_cents = "1000"
        shipping_data = {}
        items = []
        currency = "EGP"
        integrations = []
        code, invoice_instance, feedback = accept_api_client.create_invoice_link(
            amount_cents=amount_cents,
            shipping_data=shipping_data,
            items=items,
            currency=currency,
            integrations=integrations,
        )
        self.assertEqual(code, HTTP_EXCEPTION)
        self.assertIsNone(invoice_instance)
        self.assertEqual(feedback.message, HTTP_EXCEPTION_MESSAGE)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "api_source": "INVOICE",
            "amount_cents": amount_cents,
            "currency": currency,
            "shipping_data": shipping_data,
            "integrations": integrations,
            "items": items,
            "delivery_needed": False,
        }
        mock_post.assert_called_with(url=URLsConfig.CREATE_INVOICE_LINK, json=request_body)

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_create_invoice_link_success(self, mock_accept_connection, mock_post):
        """test create_invoice_link: Success"""
        invoice_id = "1"
        invoice_data = {"id": invoice_id}
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = SUCCESS, ResponseFeedBack(
            message=SUCCESS_MESSAGE,
            data=invoice_data,
        )

        accept_api_client = AcceptAPIClient()
        amount_cents = "1000"
        shipping_data = {}
        items = []
        currency = "EGP"
        integrations = []
        code, invoice_instance, feedback = accept_api_client.create_invoice_link(
            amount_cents=amount_cents,
            shipping_data=shipping_data,
            items=items,
            currency=currency,
            integrations=integrations,
        )
        self.assertEqual(code, SUCCESS)
        self.assertEqual(invoice_instance.id, invoice_data.get("id"))
        self.assertEqual(feedback.data, invoice_data)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "api_source": "INVOICE",
            "amount_cents": amount_cents,
            "currency": currency,
            "shipping_data": shipping_data,
            "integrations": integrations,
            "items": items,
            "delivery_needed": False,
        }
        mock_post.assert_called_with(url=URLsConfig.CREATE_INVOICE_LINK, json=request_body)

    # ======= End create_invoice_link Tests =======

    # =========== Start create_product_link Tests =======
    # Test cases to verify that Creating Product Link working properly

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_create_product_link_code_is_not_success(self, mock_accept_connection, mock_post):
        """test create_product_link: Code is not Success"""
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = HTTP_EXCEPTION, ResponseFeedBack(message=HTTP_EXCEPTION_MESSAGE)

        accept_api_client = AcceptAPIClient()

        product_name = ""
        product_description = ""
        inventory = 1
        amount_cents = "1000"
        currency = "EGP"
        integrations = []
        code, product_instance, feedback = accept_api_client.create_product_link(
            product_name=product_name,
            product_description=product_description,
            inventory=inventory,
            amount_cents=amount_cents,
            currency=currency,
            integrations=integrations,
        )
        self.assertEqual(code, HTTP_EXCEPTION)
        self.assertIsNone(product_instance)
        self.assertEqual(feedback.message, HTTP_EXCEPTION_MESSAGE)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "product_name": product_name,
            "product_description": product_description,
            "amount_cents": amount_cents,
            "currency": currency,
            "inventory": inventory,
            "integrations": integrations,
            "allow_quantity_edit": False,
            "delivery_needed": False,
        }
        mock_post.assert_called_with(url=URLsConfig.CREATE_PRODUCT_LINK, json=request_body)

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_create_product_link_success(self, mock_accept_connection, mock_post):
        """test create_product_link: Success"""
        product_id = "1"
        product_data = {"id": product_id}
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = SUCCESS, ResponseFeedBack(
            message=SUCCESS_MESSAGE,
            data=product_data,
        )

        accept_api_client = AcceptAPIClient()
        product_name = ""
        product_description = ""
        inventory = 1
        amount_cents = "1000"
        currency = "EGP"
        integrations = []
        code, product_instance, feedback = accept_api_client.create_product_link(
            product_name=product_name,
            product_description=product_description,
            inventory=inventory,
            amount_cents=amount_cents,
            currency=currency,
            integrations=integrations,
        )
        self.assertEqual(code, SUCCESS)
        self.assertEqual(product_instance.id, product_data.get("id"))
        self.assertEqual(feedback.data, product_data)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "product_name": product_name,
            "product_description": product_description,
            "amount_cents": amount_cents,
            "currency": currency,
            "inventory": inventory,
            "integrations": integrations,
            "allow_quantity_edit": False,
            "delivery_needed": False,
        }
        mock_post.assert_called_with(url=URLsConfig.CREATE_PRODUCT_LINK, json=request_body)

    # ======= End create_product_link Tests =======

    # =========== Start get_transaction By ID Tests =======
    # Test cases to verify that transaction data is retreived successfully

    @patch.object(AcceptConnection, "get")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_get_transaction_is_not_success(self, mock_accept_connection, mock_get):
        """test get_transaction: Code is not Success"""
        mock_accept_connection.return_value = AcceptConnection
        mock_get.return_value = HTTP_EXCEPTION, ResponseFeedBack(message=HTTP_EXCEPTION_MESSAGE)

        accept_api_client = AcceptAPIClient()

        transaction_id = 1
        code, transaction_instance, feedback = accept_api_client.get_transaction(
            transaction_id=transaction_id,
        )
        self.assertEqual(code, HTTP_EXCEPTION)
        self.assertIsNone(transaction_instance)
        self.assertEqual(feedback.message, HTTP_EXCEPTION_MESSAGE)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_get.called)

        mock_get.assert_called_with(url=URLsConfig.GET_TRANSACTION_BY_ID.format(transaction_id=transaction_id))

    @patch.object(AcceptConnection, "get")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_get_transaction_success(self, mock_accept_connection, mock_get):
        """test get_transaction: Success"""
        transaction_id = 1
        transaction_data = {"id": transaction_id}
        mock_accept_connection.return_value = AcceptConnection
        mock_get.return_value = SUCCESS, ResponseFeedBack(
            message=SUCCESS_MESSAGE,
            data=transaction_data,
        )

        accept_api_client = AcceptAPIClient()
        code, transaction_instance, feedback = accept_api_client.get_transaction(
            transaction_id=transaction_id,
        )
        self.assertEqual(code, SUCCESS)
        self.assertEqual(transaction_instance.id, transaction_data.get("id"))
        self.assertEqual(feedback.data, transaction_data)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_get.called)

        mock_get.assert_called_with(url=URLsConfig.GET_TRANSACTION_BY_ID.format(transaction_id=transaction_id))

    # ======= End get_transaction By ID Tests =======

    # =========== Start get_transaction By order/Merchant ID Tests =======
    # Test cases to verify that transaction data is retreived successfully

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_get_transaction_by_merchant_is_not_success(self, mock_accept_connection, mock_post):
        """test get_transaction: Code is not Success"""
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = HTTP_EXCEPTION, ResponseFeedBack(message=HTTP_EXCEPTION_MESSAGE)

        accept_api_client = AcceptAPIClient()

        order_id = 1
        merchant_order_id = 1
        code, transaction_instance, feedback = accept_api_client.get_transaction(
            merchant_order_id=merchant_order_id,
            order_id=order_id,
        )
        self.assertEqual(code, HTTP_EXCEPTION)
        self.assertIsNone(transaction_instance)
        self.assertEqual(feedback.message, HTTP_EXCEPTION_MESSAGE)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "merchant_order_id": merchant_order_id,
            "order_id": order_id,
        }
        mock_post.assert_called_with(url=URLsConfig.GET_TRANSACTION_BY_MERCHANT_ID, json=request_body)

    @patch.object(AcceptConnection, "post")
    @patch("paymob.accept.accept_client.AcceptConnection")
    def test_get_transaction_by_merchant_success(self, mock_accept_connection, mock_post):
        """test get_transaction: Success"""
        transaction_id = 1
        transaction_data = {"id": transaction_id}
        mock_accept_connection.return_value = AcceptConnection
        mock_post.return_value = SUCCESS, ResponseFeedBack(
            message=SUCCESS_MESSAGE,
            data=transaction_data,
        )

        accept_api_client = AcceptAPIClient()
        order_id = 1
        merchant_order_id = 1
        code, transaction_instance, feedback = accept_api_client.get_transaction(
            merchant_order_id=merchant_order_id,
            order_id=order_id,
        )
        self.assertEqual(code, SUCCESS)
        self.assertEqual(transaction_instance.id, transaction_data.get("id"))
        self.assertEqual(feedback.data, transaction_data)
        self.assertTrue(mock_accept_connection.called)
        self.assertTrue(mock_post.called)

        request_body = {
            "merchant_order_id": merchant_order_id,
            "order_id": order_id,
        }
        mock_post.assert_called_with(url=URLsConfig.GET_TRANSACTION_BY_MERCHANT_ID, json=request_body)

    # ======= End get_transaction By order/Merchant ID Tests =======

    # def test_integration(self):
    #     import pytest
    #     if config("SKIP_INTEGRATION_TESTS", cast=bool):
    #         pytest.skip("Skip Integration Tests")

    #     from paymob.accept.utils import AcceptUtils
    #     client = AcceptAPIClient()

    #     mid_key = "item"
    #     identifier = "1"
    #     merchant_order_id = AcceptUtils.generate_merchant_order_id(mid_key=mid_key, identifier=identifier)
    #     amount_cents = 1000
    #     currency = "EGP"
    #     code, order, feedback = client.create_order(
    #         merchant_order_id=merchant_order_id,
    #         amount_cents=amount_cents,
    #         currency=currency
    #     )
    #     self.assertEqual(code, SUCCESS)
    #     self.assertEqual(feedback.status_code, 201)
    #     self.assertHasAttr(order, "id")

    #     amount_cents = 1000
    #     currency = "EGP"
    #     billing_data = {
    #         "first_name": "test",
    #         "last_name": "test",
    #         "email": "test@test.test",
    #         "phone_number": "01000000000",
    #         "floor": "NA",
    #         "apartment": "NA",
    #         "street": "NA",
    #         "building": "NA",
    #         "postal_code": "NA",
    #         "city": "NA",
    #         "country": "NA",
    #         "state": "NA",
    #     }
    #     integration_id = 3871725
    #     code, payment_key, feedback = client.create_payment_key(
    #         order_id=order.id,
    #         amount_cents=amount_cents,
    #         currency=currency,
    #         billing_data=billing_data,
    #         integration_id=integration_id,
    #     )
    #     self.assertEqual(code, SUCCESS)
    #     self.assertEqual(feedback.status_code, 201)
    #     self.assertIsNotNone(payment_key)

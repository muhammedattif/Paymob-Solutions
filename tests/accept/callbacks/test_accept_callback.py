# Other Third Party Imports
import pytest

# First Party Imports
from paymob.accept import HMACValidator
from paymob.accept.callbacks import AcceptCallback, CardTokenCallback, DeliveryStatusCallback, TransactionCallback
from paymob.accept.constants import AcceptCallbackTypes
from paymob.accept.factories import CardTokenCallbackFactory, DeliveryStatusCallbackFactory, DynamicTransactionFactory
from tests.utils import AbstractTestCase


class TestAcceptCallback(AbstractTestCase):
    """Test AcceptCallback Class"""

    # =========== Start AcceptCallback Tests =======
    # Test cases to verify that the right callback class is returned based on the callback type

    def test_invalid_callback_type(self):
        """test DELIVERY_STATUS: Success"""
        incoming_hmac = "*****"
        callback_dict = {"type": "Invalid"}

        with pytest.raises(TypeError):
            AcceptCallback(incoming_hmac=incoming_hmac, callback_dict=callback_dict)

    def test_transaction_success(self):
        """test TRANSACTION: Success"""
        incoming_hmac = "*****"
        callback_dict = {"type": AcceptCallbackTypes.TRANSACTION, "obj": {"id": 1}}

        callback = AcceptCallback(incoming_hmac=incoming_hmac, callback_dict=callback_dict)

        self.assertTrue(issubclass(callback.__class__, DynamicTransactionFactory))
        self.assertTrue(issubclass(callback.__class__, HMACValidator))
        self.assertTrue(issubclass(callback.__class__, TransactionCallback))

        self.assertEqual(callback.type, AcceptCallbackTypes.TRANSACTION)
        self.assertEqual(callback.obj.id, callback_dict.get("obj").get("id"))

    def test_card_token_success(self):
        """test CARD_TOKEN: Success"""
        incoming_hmac = "*****"
        callback_dict = {"type": AcceptCallbackTypes.CARD_TOKEN, "obj": {"id": 1}}

        callback = AcceptCallback(incoming_hmac=incoming_hmac, callback_dict=callback_dict)

        self.assertTrue(issubclass(callback.__class__, CardTokenCallbackFactory))
        self.assertTrue(issubclass(callback.__class__, HMACValidator))
        self.assertTrue(issubclass(callback.__class__, CardTokenCallback))

        self.assertEqual(callback.type, AcceptCallbackTypes.CARD_TOKEN)
        self.assertEqual(callback.obj.id, callback_dict.get("obj").get("id"))

    def test_delivery_status_success(self):
        """test DELIVERY_STATUS: Success"""
        incoming_hmac = "*****"
        callback_dict = {"type": AcceptCallbackTypes.DELIVERY_STATUS, "obj": {"order_id": 1}}

        callback = AcceptCallback(incoming_hmac=incoming_hmac, callback_dict=callback_dict)

        self.assertTrue(issubclass(callback.__class__, DeliveryStatusCallbackFactory))
        self.assertTrue(issubclass(callback.__class__, HMACValidator))
        self.assertTrue(issubclass(callback.__class__, DeliveryStatusCallback))

        self.assertEqual(callback.type, AcceptCallbackTypes.DELIVERY_STATUS)
        self.assertEqual(callback.obj.order_id, callback_dict.get("obj").get("order_id"))

    # ======= End AcceptCallback Tests =======

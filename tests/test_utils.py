import time
from unittest.mock import patch

import pytest

from accept import AcceptUtils


@pytest.fixture
def accept_utils_instance():
    return AcceptUtils()


class TestGenerateMerchantOrderId:
    def test_generate_merchant_order_id(self, accept_utils_instance):
        """
        Test case to verify the behavior of the generate_merchant_order_id method.

        It checks if the method returns the expected order ID based on the provided inputs.
        """
        mid_key = "example_key"
        identifier = 12345
        expected_order_id = f"{mid_key}_{identifier}__{int(time.time())}"

        order_id = accept_utils_instance.generate_merchant_order_id(mid_key, identifier)

        assert order_id == expected_order_id


class TestExtractMidKeyAndIdentifier:

    def test_it_return_none_if_merchant_order_id_is_not_a_string(self, accept_utils_instance):
        """
        Test case to verify the behavior of the extract_mid_key_and_identifier method.

        It checks if the method returns None for both mid_key and identifier if the provided merchant order id is not a string.
        """
        merchant_order_id = 12345

        mid_key, identifier = accept_utils_instance.extract_mid_key_and_identifier(merchant_order_id)
        assert mid_key is None
        assert identifier is None
    def test_extract_mid_key_and_identifier(self, accept_utils_instance):
        """
        Test case to verify the behavior of the extract_mid_key_and_identifier method.

        It checks if the method correctly extracts the mid_key and identifier from a given merchant order id.
        """
        merchant_order_id = "examplekey_12345__1623695829"
        expected_mid_key = "examplekey"
        expected_identifier = "12345"

        mid_key, identifier = accept_utils_instance.extract_mid_key_and_identifier(merchant_order_id)

        assert mid_key == expected_mid_key
        assert identifier == expected_identifier


class TestConstructIframeUrl:
    def test_construct_iframe_url(self, accept_utils_instance):
        """
        Test case to verify the behavior of the construct_iframe_url method.

        It checks if the method constructs the correct iframe URL based on the provided iframe ID and payment key.
        """
        iframe_id = 9876
        payment_key = "example_payment_key"
        expected_url = "https://example.com/iframe?id=9876&token=example_payment_key"

        url = accept_utils_instance.construct_iframe_url(iframe_id, payment_key)

        assert url == expected_url


class TestValidateProcessedHmac:
    def test_validate_processed_hmac_transaction(self, accept_utils_instance):
        """
        Test case to verify the behavior of the validate_processed_hmac method for a transaction callback.

        It checks if the method correctly validates the HMAC for a transaction callback object.
        """
        incoming_hmac = "example_incoming_hmac"
        callback_obj_dict = {
            "amount_cents": 1000,
            "created_at": "2023-06-14T12:00:00",
            # Other required fields
        }
        callback_type = "TRANSACTION"

        is_valid_hmac = accept_utils_instance.validate_processed_hmac(incoming_hmac, callback_obj_dict, callback_type)

        assert is_valid_hmac is True

    def test_validate_processed_hmac_card_token(self, accept_utils_instance):
        """
        Test case to verify the behavior of the validate_processed_hmac method for a card token callback.

        It checks if the method correctly validates the HMAC for a card token callback object.
        """
        incoming_hmac = "example_incoming_hmac"
        callback_obj_dict = {
            "card_subtype": "VISA",
            "created_at": "2023-06-14T12:00:00",
            # Other required fields
        }
        callback_type = "CARD_TOKEN"

        is_valid_hmac = accept_utils_instance.validate_processed_hmac(incoming_hmac, callback_obj_dict, callback_type)

        assert is_valid_hmac is True

    def test_validate_processed_hmac_invalid_callback_type(self, accept_utils_instance):
        """
        Test case to verify the behavior of the validate_processed_hmac method with an invalid callback type.

        It checks if the method returns False when an invalid callback type is provided.
        """
        incoming_hmac = "example_incoming_hmac"
        callback_obj_dict = {
            # Callback object dictionary
        }
        callback_type = "INVALID_TYPE"

        is_valid_hmac = accept_utils_instance.validate_processed_hmac(incoming_hmac, callback_obj_dict, callback_type)

        assert is_valid_hmac is False


class TestGenerateTransactionProcessedHmac:
    def test_generate_transaction_processed_hmac(self, accept_utils_instance):
        """
        Test case to verify the behavior of the _generate_transaction_processed_hmac method.

        It checks if the method correctly generates the HMAC for a transaction callback body dictionary.
        """
        body_dict = {
            "amount_cents": 1000,
            "created_at": "2023-06-14T12:00:00",
            # Other required fields
        }
        expected_hmac = accept_utils_instance._calculate_hmac('')

        hmac = accept_utils_instance._generate_transaction_processed_hmac(body_dict)

        assert hmac == expected_hmac


class TestGenerateCardTokenProcessedHmac:
    def test_generate_card_token_processed_hmac(self, accept_utils_instance):
        """
        Test case to verify the behavior of the _generate_card_token_processed_hmac method.

        It checks if the method correctly generates the HMAC for a card token callback body dictionary.
        """
        body_dict = {
            "card_subtype": "VISA",
            "created_at": "2023-06-14T12:00:00",
            # Other required fields
        }
        hmac = accept_utils_instance._generate_card_token_processed_hmac(body_dict)
        expected_hmac = accept_utils_instance._calculate_hmac(hmac)

        assert hmac == expected_hmac


if __name__ == "__main__":
    pytest.main()

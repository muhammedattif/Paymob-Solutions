# First Party Imports
from paymob.accept import AcceptUtils
from paymob.accept.config import URLsConfig
from tests.utils import AbstractTestCase


class TestAcceptUtils(AbstractTestCase):
    """Test AcceptUtils Class"""

    # =========== Start generate_merchant_order_id Tests =======
    # Test case to verify the behavior of the generate_merchant_order_id method.
    # It checks if the method returns the expected order ID based on the provided inputs.

    def test_generate_merchant_order_id_success(self):
        """test generate_merchant_order_id: Success"""

        mid_key = "Test"
        identifier = "1"

        expected_merchant_order_id = f"{mid_key}_{identifier}__000".split("__")[0]
        actual_merchant_order_id = AcceptUtils.generate_merchant_order_id(
            mid_key=mid_key,
            identifier=identifier,
        )
        self.assertEqual(actual_merchant_order_id.split("__")[0], expected_merchant_order_id)

    # ======= End generate_merchant_order_id Tests =======

    # ======= Start extract_mid_key_and_identifier Tests =======
    # Test case to verify the behavior of the extract_mid_key_and_identifier method.
    # It checks if the method correctly extracts the mid_key and identifier from a given merchant order id.

    def test_extract_mid_key_and_identifier_merchant_order_id_is_not_str(self):
        """test extract_mid_key_and_identifier: Mechant Order ID is not a String"""

        merchant_order_id = 1

        actual_mid_key, actual_identifier = AcceptUtils.extract_mid_key_and_identifier(
            merchant_order_id=merchant_order_id,
        )
        self.assertIsNone(actual_mid_key)
        self.assertIsNone(actual_identifier)

    def test_extract_mid_key_and_identifier_invalid_merchant_order_id(self):
        """test extract_mid_key_and_identifier: Invalid Mechant Order ID"""

        merchant_order_id = "Invalid"

        actual_mid_key, actual_identifier = AcceptUtils.extract_mid_key_and_identifier(
            merchant_order_id=merchant_order_id,
        )
        self.assertIsNone(actual_mid_key)
        self.assertIsNone(actual_identifier)

    def test_extract_mid_key_and_identifier_success(self):
        """test extract_mid_key_and_identifier:  Success"""
        mid_key = "Test"
        identifier = "1"
        merchant_order_id = f"{mid_key}_{identifier}__0"

        actual_mid_key, actual_identifier = AcceptUtils.extract_mid_key_and_identifier(
            merchant_order_id=merchant_order_id,
        )
        self.assertEqual(actual_mid_key, mid_key)
        self.assertEqual(actual_identifier, identifier)

    # ======= End extract_mid_key_and_identifier Tests =======

    # ======= Start create_iframe_url Tests ========
    # Test case to verify the behavior of the construct_iframe_url method.
    # It checks if the method constructs the correct iframe URL based on the provided iframe ID and payment key.

    def test_create_iframe_url_success(self):
        """test create_iframe_url: Success"""

        iframe_id = 112233
        payment_key = "*****"

        expected_iframe_url = URLsConfig.IFRAME.format(iframe_id=iframe_id, payment_key=payment_key)
        actual_iframe_url = AcceptUtils.create_iframe_url(iframe_id=iframe_id, payment_key=payment_key)
        self.assertEqual(actual_iframe_url, expected_iframe_url)

    # ======= End create_iframe_url Tests ========

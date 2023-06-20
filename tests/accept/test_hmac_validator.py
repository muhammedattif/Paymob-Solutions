# Python Standard Library Imports
from unittest.mock import patch

# First Party Imports
from paymob.accept import HMACValidator
from paymob.accept.constants import AcceptCallbackTypes
from tests.utils import AbstractTestCase


class TestHMACValidator(AbstractTestCase):
    """Test HMACValidator Class"""

    # ======== Start SetUpClass ========

    @classmethod
    def setup_class(cls):

        cls.valid_incoming_hmac = "*****"
        cls.transaction_callback_dict = {
            "type": AcceptCallbackTypes.TRANSACTION,
            "obj": {
                "id": 109628234,
                "pending": False,
                "amount_cents": 1000,
                "success": True,
                "is_auth": False,
                "is_capture": False,
                "is_standalone_payment": True,
                "is_voided": False,
                "is_refunded": False,
                "is_3d_secure": False,
                "integration_id": 3871725,
                "profile_id": 787951,
                "has_parent_transaction": False,
                "order": {
                    "id": 126087094,
                    "created_at": "2023-06-01T21:45:56.993153",
                    "delivery_needed": False,
                    "merchant": {
                        "id": 787951,
                        "created_at": "2023-05-14T19:41:48.955870",
                        "phones": ["+201028362012"],
                        "company_emails": [],
                        "company_name": "Mahmoud",
                        "state": "",
                        "country": "EGY",
                        "city": "Cairo",
                        "postal_code": "",
                        "street": "",
                    },
                    "collector": None,
                    "amount_cents": 1000,
                    "shipping_data": {
                        "id": 61920183,
                        "first_name": "Brett",
                        "last_name": "Roberts",
                        "street": "NA",
                        "building": "NA",
                        "floor": "NA",
                        "apartment": "NA",
                        "city": "NA",
                        "state": "NA",
                        "country": "NA",
                        "email": "swsz2qbisz@amenli.com",
                        "phone_number": "01550272164",
                        "postal_code": "NA",
                        "extra_description": "",
                        "shipping_method": "UNK",
                        "order_id": 126087094,
                        "order": 126087094,
                    },
                    "currency": "EGP",
                    "is_payment_locked": False,
                    "is_return": False,
                    "is_cancel": False,
                    "is_returned": False,
                    "is_canceled": False,
                    "merchant_order_id": "lead_20__1685645156",
                    "wallet_notification": None,
                    "paid_amount_cents": 0,
                    "notify_user_with_email": False,
                    "items": [],
                    "order_url": "https://accept.paymob.com/standalone/?ref=i_LRR2Q3VHeUtzaTBFb0xSdG0rRVY2YzA4dz09X0JLelBTZElyRXRpM3hkR0tHU1RDQlE9PQ",
                    "commission_fees": 0,
                    "delivery_fees_cents": 0,
                    "delivery_vat_cents": 0,
                    "payment_method": "tbc",
                    "merchant_staff_tag": None,
                    "api_source": "OTHER",
                    "data": {},
                },
                "created_at": "2023-06-01T21:45:57.830530",
                "transaction_processed_callback_responses": [
                    {
                        "response": {
                            "status": "200",
                            "content": "None",
                            "headers": "{'Server': 'nginx', 'Content-Type': 'text/plain; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Vary': 'Accept-Encoding', 'X-Request-Id': 'd1cde7b7-5fda-4ea4-9d3b-ddc9b12ff94e', 'X-Token-Id': 'ac84f01e-0bc5-41d3-be08-b5b3912f8148', 'Cache-Control': 'no-cache, private', 'Date': 'Thu, 01 Jun 2023 18:46:17 GMT', 'Content-Encoding': 'gzip'}",
                            "encoding": "UTF-8",
                        },
                        "callback_url": "https://webhook.site/ac84f01e-0bc5-41d3-be08-b5b3912f8148",
                        "response_received_at": "2023-06-01T18:46:17.484494",
                    },
                ],
                "currency": "EGP",
                "source_data": {
                    "pan": "01010101010",
                    "type": "wallet",
                    "sub_type": "wallet",
                    "owner_name": None,
                    "phone_number": "01010101010",
                },
                "api_source": "OTHER",
                "terminal_id": None,
                "merchant_commission": 0,
                "installment": None,
                "discount_details": [],
                "is_void": False,
                "is_refund": False,
                "data": {
                    "klass": "WalletPayment",
                    "token": "",
                    "amount": 1000,
                    "method": 0,
                    "message": "Transaction has been completed successfully.",
                    "currency": "EGP",
                    "created_at": "2023-06-01T18:45:57.876617",
                    "mpg_txn_id": "213412341",
                    "order_info": "swsz2qbisz@amenli.com",
                    "uig_txn_id": "4351324134",
                    "upg_txn_id": None,
                    "mer_txn_ref": "3871725_3fb960d3f7495a998f8984e89b978f10",
                    "redirect_url": "https://accept.paymobsolutions.com/api/acceptance/wallet_other_test/wallet_template?token=****",
                    "wallet_issuer": "VODAFONE",
                    "wallet_msisdn": "01010101010",
                    "gateway_source": "",
                    "upg_qrcode_ref": "4351324134",
                    "txn_response_code": "200",
                    "gateway_integration_pk": 3871725,
                },
                "is_hidden": False,
                "payment_key_claims": {
                    "extra": {},
                    "pmk_ip": "197.62.181.81",
                    "user_id": 1363533,
                    "currency": "EGP",
                    "order_id": 126087094,
                    "amount_cents": 1000,
                    "billing_data": {
                        "city": "NA",
                        "email": "swsz2qbisz@amenli.com",
                        "floor": "NA",
                        "state": "NA",
                        "street": "NA",
                        "country": "NA",
                        "building": "NA",
                        "apartment": "NA",
                        "last_name": "Roberts",
                        "first_name": "Brett",
                        "postal_code": "NA",
                        "phone_number": "01550272164",
                        "extra_description": "NA",
                    },
                    "integration_id": 3871725,
                    "lock_order_when_paid": False,
                    "single_payment_attempt": False,
                },
                "error_occured": False,
                "is_live": False,
                "other_endpoint_reference": "4351324134",
                "refunded_amount_cents": 0,
                "source_id": -1,
                "is_captured": False,
                "captured_amount": 0,
                "merchant_staff_tag": None,
                "updated_at": "2023-06-17T17:53:32.176405",
                "is_settled": False,
                "bill_balanced": False,
                "is_bill": False,
                "owner": 1363533,
                "parent_transaction": None,
            },
            "transaction_processed_callback_responses": "",
        }
        cls.card_token_callback_dict = {
            "type": AcceptCallbackTypes.CARD_TOKEN,
            "obj": cls.transaction_callback_dict.get("obj"),
        }
        cls.delivery_status_callback_dict = {
            "type": AcceptCallbackTypes.DELIVERY_STATUS,
            "obj": cls.transaction_callback_dict.get("obj"),
        }
        cls.invalid_transaction_dict = {
            "type": "Invalid",
            "obj": cls.transaction_callback_dict.get("obj"),
        }

    # ======== End SetUpClass ========

    # ========= Start __init__ Tests =========

    def test___init__callback_dict_is_not_dict(self):
        """test __init__: callback_dict is not of type dict"""

        callback_dict = "invalid"
        hmac = HMACValidator(
            incoming_hmac=self.valid_incoming_hmac,
            callback_dict=callback_dict,
        )
        self.assertNoHasAttr(hmac, "callback_obj_dict")
        self.assertEqual(hmac.callback_dict, callback_dict)

    def test___init__success(self):
        """test __init__: Success"""

        callback_obj_dict = {"id": 1}
        callback_dict = {"obj": callback_obj_dict}
        hmac = HMACValidator(
            incoming_hmac=self.valid_incoming_hmac,
            callback_dict=callback_dict,
        )
        self.assertEqual(hmac.callback_obj_dict, callback_obj_dict)
        self.assertEqual(hmac.callback_dict, callback_dict)

    # ========= End __init__ Tests =========

    # ========= Start is_valid Tests =========
    # Test cases to verify the behavior of the is_valid method for a Transaction/CardToken/DeliveryStatus callbacks.

    def test_is_valid_callback_is_not_a_dict(self):
        """test is_valid: Callback is not a Dict"""
        hmac = HMACValidator(
            incoming_hmac=self.valid_incoming_hmac,
            callback_dict="invalid",
        )
        self.assertFalse(hmac.is_valid)

    def test_is_valid_invalid_callback_type(self):
        """test is_valid: Invalid callback_type"""
        hmac = HMACValidator(
            incoming_hmac=self.valid_incoming_hmac,
            callback_dict=self.invalid_transaction_dict,
        )
        self.assertFalse(hmac.is_valid)

    @patch.object(HMACValidator, "_generate_transaction_processed_hmac")
    def test_is_valid_invalid_incoming_hmac(self, mock_generate_transaction_processed_hmac):
        """test is_valid: Invalid Incoming HMAC"""
        mock_generate_transaction_processed_hmac.return_value = "Invalid"
        hmac = HMACValidator(
            incoming_hmac=self.valid_incoming_hmac,
            callback_dict=self.transaction_callback_dict,
        )
        self.assertFalse(hmac.is_valid)
        self.assertTrue(mock_generate_transaction_processed_hmac.called)

    @patch.object(HMACValidator, "_generate_transaction_processed_hmac")
    def test_is_valid_transaction_callback_success(self, mock_generate_transaction_processed_hmac):
        """test is_valid: callback_type=TRANSACTION Success"""

        mock_generate_transaction_processed_hmac.return_value = self.valid_incoming_hmac
        hmac = HMACValidator(
            incoming_hmac=self.valid_incoming_hmac,
            callback_dict=self.transaction_callback_dict,
        )
        self.assertTrue(hmac.is_valid)
        self.assertTrue(mock_generate_transaction_processed_hmac.called)

    @patch.object(HMACValidator, "_generate_card_token_processed_hmac")
    def test_is_valid_card_token_callback_success(self, mock_generate_card_token_processed_hmac):
        """test is_valid: callback_type=CARD_TOKEN Success"""

        mock_generate_card_token_processed_hmac.return_value = self.valid_incoming_hmac
        hmac = HMACValidator(
            incoming_hmac=self.valid_incoming_hmac,
            callback_dict=self.card_token_callback_dict,
        )
        self.assertTrue(hmac.is_valid)
        self.assertTrue(mock_generate_card_token_processed_hmac.called)

    @patch.object(HMACValidator, "_generate_delivery_status_processed_hmac")
    def test_is_valid_delivery_status_callback_success(self, mock_generate_delivery_status_processed_hmac):
        """test is_valid: callback_type=DELIVERY_STATUS Success"""

        mock_generate_delivery_status_processed_hmac.return_value = self.valid_incoming_hmac
        hmac = HMACValidator(
            incoming_hmac=self.valid_incoming_hmac,
            callback_dict=self.delivery_status_callback_dict,
        )
        self.assertTrue(hmac.is_valid)
        self.assertTrue(mock_generate_delivery_status_processed_hmac.called)

    # ========= End is_valid Tests =========

    # ========= Start _generate_processed_hmac Tests =========

    @patch.object(HMACValidator, "_calculate_hmac")
    def test_generate_processed_hmac_hmac_dict_is_not_dict(self, mock_calculate_hmac):
        """test _generate_processed_hmac: hmac_dict is not of type dict"""

        hmac = HMACValidator(
            incoming_hmac=self.valid_incoming_hmac,
            callback_dict=self.delivery_status_callback_dict,
        )
        actual_hmac_message = hmac._generate_processed_hmac(
            hmac_dict="Invalid",
        )
        expected_hmac_message = ""
        self.assertEqual(actual_hmac_message, expected_hmac_message)
        self.assertFalse(mock_calculate_hmac.called)

    @patch.object(HMACValidator, "_calculate_hmac")
    def test_generate_processed_hmac_success(self, mock_calculate_hmac):
        """test _generate_processed_hmac: Success"""

        expected_hmac_message = "HMAC Message"
        mock_calculate_hmac.return_value = expected_hmac_message

        hmac = HMACValidator(
            incoming_hmac=self.valid_incoming_hmac,
            callback_dict=self.delivery_status_callback_dict,
        )
        actual_hmac_message = hmac._generate_processed_hmac(
            hmac_dict={},
        )
        self.assertEqual(actual_hmac_message, expected_hmac_message)
        self.assertTrue(mock_calculate_hmac.called)

    # ========= End _generate_processed_hmac Tests =========

    # ========= Start _generate_transaction_processed_hmac Tests =========

    @patch.object(HMACValidator, "_generate_processed_hmac")
    def test_generate_transaction_processed_hmac_invalid_callback_obj_dict(self, mock_generate_processed_hmac):
        """test _generate_transaction_processed_hmac: Invalid callback_obj_dict"""

        hmac = HMACValidator(
            incoming_hmac=self.valid_incoming_hmac,
            callback_dict={},
        )
        actual_hmac = hmac._generate_transaction_processed_hmac()
        expected_hmac = ""
        self.assertEqual(actual_hmac, expected_hmac)
        self.assertFalse(mock_generate_processed_hmac.called)

    @patch.object(HMACValidator, "_generate_processed_hmac")
    def test_generate_transaction_processed_hmac_success(self, mock_generate_processed_hmac):
        """test _generate_transaction_processed_hmac: Success"""

        expected_hmac = "*****"
        mock_generate_processed_hmac.return_value = expected_hmac

        hmac = HMACValidator(
            incoming_hmac=self.valid_incoming_hmac,
            callback_dict=self.transaction_callback_dict,
        )
        actual_hmac = hmac._generate_transaction_processed_hmac()
        self.assertEqual(actual_hmac, expected_hmac)
        self.assertTrue(mock_generate_processed_hmac.called)

    # ========= End _generate_transaction_processed_hmac Tests =========

    # ========= Start _generate_card_token_processed_hmac Tests =========

    @patch.object(HMACValidator, "_generate_processed_hmac")
    def test_generate_card_token_processed_hmac_invalid_callback_obj_dict(self, mock_generate_processed_hmac):
        """test _generate_card_token_processed_hmac: Invalid callback_obj_dict"""

        hmac = HMACValidator(
            incoming_hmac=self.valid_incoming_hmac,
            callback_dict={},
        )
        actual_hmac = hmac._generate_card_token_processed_hmac()
        expected_hmac = ""
        self.assertEqual(actual_hmac, expected_hmac)
        self.assertFalse(mock_generate_processed_hmac.called)

    @patch.object(HMACValidator, "_generate_processed_hmac")
    def test_generate_card_token_processed_hmac_hmac_success(self, mock_generate_processed_hmac):
        """test _generate_card_token_processed_hmac: Success"""

        expected_hmac = "*****"
        mock_generate_processed_hmac.return_value = expected_hmac

        hmac = HMACValidator(
            incoming_hmac=self.valid_incoming_hmac,
            callback_dict=self.card_token_callback_dict,
        )
        actual_hmac = hmac._generate_card_token_processed_hmac()
        self.assertEqual(actual_hmac, expected_hmac)
        self.assertTrue(mock_generate_processed_hmac.called)

    # ========= End _generate_card_token_processed_hmac Tests =========

    # ========= Start _generate_card_token_processed_hmac Tests =========

    @patch.object(HMACValidator, "_generate_processed_hmac")
    def test_generate_delivery_status_processed_hmac_invalid_callback_obj_dict(self, mock_generate_processed_hmac):
        """test _generate_delivery_status_processed_hmac: Invalid callback_obj_dict"""

        hmac = HMACValidator(
            incoming_hmac=self.valid_incoming_hmac,
            callback_dict={},
        )
        actual_hmac = hmac._generate_delivery_status_processed_hmac()
        expected_hmac = ""
        self.assertEqual(actual_hmac, expected_hmac)
        self.assertFalse(mock_generate_processed_hmac.called)

    @patch.object(HMACValidator, "_generate_processed_hmac")
    def test_generate_delivery_status_processed_hmac_hmac_success(self, mock_generate_processed_hmac):
        """test _generate_delivery_status_processed_hmac: Success"""

        expected_hmac = "*****"
        mock_generate_processed_hmac.return_value = expected_hmac

        hmac = HMACValidator(
            incoming_hmac=self.valid_incoming_hmac,
            callback_dict=self.card_token_callback_dict,
        )
        actual_hmac = hmac._generate_delivery_status_processed_hmac()
        self.assertEqual(actual_hmac, expected_hmac)
        self.assertTrue(mock_generate_processed_hmac.called)

    # ========= End _generate_delivery_status_processed_hmac Tests =========

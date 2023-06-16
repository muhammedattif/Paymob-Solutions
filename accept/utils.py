# Python Standard Library Imports
import hashlib
import hmac
import time
from typing import Any, Dict, Tuple, Union

from .config import Credentials, URLsConfig


class AcceptCallbackTypes:
    TRANSACTION = "TRANSACTION"
    CARD_TOKEN = "TOKEN"


class PaymentSubTypes:
    AGGREGATOR = "AGGREGATOR"
    WALLET = "WALLET"


class HMACUtils:
    @staticmethod
    def _calculate_hmac(message: str) -> str:
        """Calculates HMAC

        Args:
            message (str): GeneratedHMAC Message

        Returns:
            str: Calculated HMAC
        """

        return (
            hmac.new(
                Credentials.ACCEPT_HMAC_SECRET.encode("utf-8"),
                message.encode("utf-8"),
                hashlib.sha512,
            )
            .hexdigest()
            .lower()
        )

    @classmethod
    def _generate_processed_hmac(cls, hmac_dict: Dict[str, Any]) -> str:
        """Creates HMAC from sent body_dic

        Args:
            hmac_dict (Dict[str, Any]): Hmac Dict

        Returns:
            str: Generated HMAC
        """
        if not isinstance(hmac_dict, dict):
            return ""

        message = ""
        for value in hmac_dict.values():
            if isinstance(value, bool):
                value = str(value).lower()
            if value is None:
                value = ""
            message += str(value)

        return cls._calculate_hmac(message=message)

    @classmethod
    def _generate_transaction_processed_hmac(cls, body_dict: Dict[str, Any]) -> str:
        """Creates HMAC from sent transaction callback body_dic

        Args:
            body_dict (Dict[str, Any]): Transaction Body Dict

        Returns:
            str: Generated HMAC
        """
        if not isinstance(body_dict, dict):
            return ""

        hmac_dict = {
            "amount_cents": body_dict.get("amount_cents"),
            "created_at": body_dict.get("created_at"),
            "currency": body_dict.get("currency"),
            "error_occured": body_dict.get("error_occured"),
            "has_parent_transaction": body_dict.get("has_parent_transaction"),
            "id": body_dict.get("id"),
            "integration_id": body_dict.get("integration_id"),
            "is_3d_secure": body_dict.get("is_3d_secure"),
            "is_auth": body_dict.get("is_auth"),
            "is_capture": body_dict.get("is_capture"),
            "is_refunded": body_dict.get("is_refunded"),
            "is_standalone_payment": body_dict.get("is_standalone_payment"),
            "is_voided": body_dict.get("is_voided"),
            "order.id": body_dict.get("order").get("id"),
            "owner": body_dict.get("owner"),
            "pending": body_dict.get("pending"),
            "source_data.pan": body_dict.get("source_data").get("pan"),
            "source_data.sub_type": body_dict.get("source_data").get("sub_type"),
            "source_data.type": body_dict.get("source_data").get("type"),
            "success": body_dict.get("success"),
        }

        return cls._generate_processed_hmac(hmac_dict=hmac_dict)

    @classmethod
    def _generate_card_token_processed_hmac(cls, body_dict: Dict[str, Any]) -> str:
        """Creates HMAC from sent card token callback body_dic

        Args:
            body_dict (Dict[str, Any]): Token Card Body Dict

        Returns:
            str: Generated HMAC
        """
        if not isinstance(body_dict, dict):
            return ""

        hmac_dict = {
            "card_subtype": body_dict.get("card_subtype"),
            "created_at": body_dict.get("created_at"),
            "email": body_dict.get("email"),
            "id": body_dict.get("id"),
            "masked_pan": body_dict.get("masked_pan"),
            "merchant_id": body_dict.get("merchant_id"),
            "order_id": body_dict.get("order_id"),
            "token": body_dict.get("token"),
        }

        return cls._generate_processed_hmac(hmac_dict=hmac_dict)

    # Public Method that can be used Directly to Validate HMAC
    @classmethod
    def validate_processed_hmac(cls, incoming_hmac: str, callback_dict: Dict[str, Any]) -> bool:
        """Validates HMAC for processed callback

        Args:
            incoming_hmac (str): Incomming Paymob's HMAC
            callback_obj_dict Dict[str, Any]: Obj Dict
            callback_type (str): Callback Type (Card Token or Transaction)

        Returns:
            bool: True if HMAC is Valid, False otherwise
        """
        if not isinstance(callback_dict, dict):
            return False

        callback_type = callback_dict.get("type")
        callback_obj_dict = callback_dict.get("obj")
        if callback_type == AcceptCallbackTypes.TRANSACTION:
            calculated_hmac = cls._generate_transaction_processed_hmac(callback_obj_dict)
        elif callback_type == AcceptCallbackTypes.CARD_TOKEN:
            calculated_hmac = cls._generate_card_token_processed_hmac(callback_obj_dict)
        else:
            return False

        if calculated_hmac != incoming_hmac:
            return False

        return True


class AcceptUtils:
    @staticmethod
    def generate_merchant_order_id(mid_key: str, identifier: int):
        """Constructs merchant order id from mid_key and identifier

        Args:
            mid_key (str):
            identifier (int): instance id

        Returns:
            str: Internal Order ID (Format: <mid_key>_<identifier>__<time>)
        """
        return "{0}_{1}__{2}".format(mid_key, identifier, int(time.time()))

    @staticmethod
    def extract_mid_key_and_identifier(merchant_order_id: str) -> Tuple[Union[str, None], Union[str, None]]:
        """Extracts mid_key and identifier from merchant order id

        Args:
            merchant_order_id (str): Internal Order ID (Format: <mid_key>_<identifier>__<time>

        Returns
            Tuple[Union[str, None], Union[str, None]]: mid_key, identifier
        """

        if not isinstance(merchant_order_id, str):
            return None, None

        mid_raw = merchant_order_id.split("__")[0]
        mid_ref_list = mid_raw.split("_")
        if len(mid_ref_list) != 2:
            return None, None

        mid_key = mid_ref_list[0]
        identifier = mid_ref_list[1]
        return mid_key, identifier

    @staticmethod
    def create_iframe_url(iframe_id: int, payment_key: str) -> str:
        """Constructs Iframe URL

        Args:
            iframe_id (int): Paymob's Iframe ID
            payment_key (str): Generated Payment Key

        Returns:
            str: Full Iframe URL
        """
        return URLsConfig.IFRAME_URL.format(
            iframe_id=iframe_id,
            payment_token=payment_key,
        )

    ##### HMAC Utils #####

# Python Standard Library Imports
import time
from typing import Tuple, Union

from .config import URLsConfig


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
        return URLsConfig.IFRAME.format(
            iframe_id=iframe_id,
            payment_key=payment_key,
        )

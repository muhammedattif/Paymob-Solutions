# Python Standard Library Imports
from typing import Any, Dict, Union, Tuple

from .config import URLsConfig
from .utils import PaymentSubTypes
from .accept_connection import AcceptConnection
from .response_codes import SUCCESS


class AcceptAPIClient:
    """Class for Accept APIs
    By Initializing an Instance from This class, an auth token is obtained automatically
    and You will be able to call The Following APIs:
        1- Create Order
        2- Get Order
        3- Create Payment Key
        4- Pay
    """

    def __init__(self) -> None:
        # Initialize Connection
        self.connection = AcceptConnection()
        
    def create_order(
        self,
        merchant_order_id: str,
        amount_cents: str,
        currency: str,
        delivery_needed: bool = False,
        items: list = [],
        shipping_data: dict = {},
        shipping_details: dict = {}
    ) -> Tuple[str, Dict[str, Any], Union[str, None]]:
        """Register an order to Accept's database

        Args:
            merchant_order_id (str): Internal Order ID
            amount_cents (str): Amount that will be paid (In Cents)
            currency (str): The currency related to this payment.
            delivery_needed (bool): Set it to be True if your order needs to be delivered by Accept's product delivery services. Defaults to False.
            items (list): list of objects contains the contents of the order if it is existing, send it as empty array if it is not available. Defaults to [].
            shipping_data (dict): Mandatory if your order needs to be delivered, otherwise you can delete the whole object. Defaults to {}.
            shipping_details (dict): Mandatory if your order needs to be delivered, otherwise you can delete the whole object. Defaults to {}.
            

        Returns:
            Tuple[str, Dict[str, Any], Union[str, None]]: (Code, Order Data Dict, Success/Error Message)
        """

        request_body = {
            "merchant_order_id": merchant_order_id,
            "amount_cents": str(amount_cents),
            "currency": currency,
            "delivery_needed": delivery_needed,
            "items": items,
            "shipping_data": shipping_data,
            "shipping_details": shipping_details
        }

        code, order_data, message = self.connection.post(
            url=URLsConfig.CREATE_ORDER_URL,
            json=request_body,
        )
    
        # TODO: Validates APIs Return Data Option
        if code == SUCCESS:
            message = "Order Created Successfully"
        return code, order_data, message

    def create_payment_key(
        self,
        order_id: str,
        amount_cents: str,
        currency: str,
        billing_data: dict,
        integration_id: int,
        card_token_key: str = None,
        expiration: int = 3600, # 1 Hour
        lock_order_when_paid: bool = False
    ) -> Tuple[str, Union[str, None], Union[str, None]]:
        """Create Payment Key

        Args:
            order_id (str): External order id
            expiration (int): The expiration time of this payment token in seconds. (The maximum is 3600 seconds which is an hour). Defaulkts to 3600.
            amount_cents (str): Amount that will be paid
            currency (str): Payment Currency
            billing_data (dict): The billing data related to the customer related to this payment.
            integration_id (int): Paymob's Integration ID
            card_token_key (str, optional): Card token. Defaults to None.
            lock_order_when_paid (bool, optional): A flag prevent this order to be paid again if it is paid. Defaults to False.

        Returns:
            Tuple[str, Union[str, None], Union[str, None]]: (Code, Payment Key, Success/Error Message)
        """

        request_body = {
            "order_id": order_id,
            "amount_cents": str(amount_cents),
            "currency": str(currency),
            "expiration": expiration,
            "integration_id": integration_id,
            "billing_data": billing_data,
            "lock_order_when_paid": lock_order_when_paid
        }
        if card_token_key:
            request_body["token"] = card_token_key

        code, data, message = self.connection.post(
            url=URLsConfig.PAYMENT_KEY_URL,
            json=request_body,
        )
        
        # TODO: Validates APIs Return Data Option
        payment_key = None
        if code == SUCCESS:
            message = "Payment Key Created Successfully"
            payment_key = data.get("token")
        return code, payment_key, message

    def get_order(
        self, 
        order_id: Union[int, str]
    ) -> Tuple[str, Dict[str, Any], Union[str, None]]:
        """Retrives Order Data

        Args:
            order_id (Union[int, str]): Paymob's External Order ID

        Returns:
            Tuple[str, Dict[str, Any], Union[str, None]]: (Code, Order Data Dict, Success/Error Message)
        """

        code, order_data, message = self.connection.get(
            url=URLsConfig.GET_ORDER_URL.format(order_id=order_id),
        )
        
        # TODO: Validates APIs Return Data Option
        if code == SUCCESS:
            message = "Successfully Retrieved Order: {0} Data: {0}".format(order_id)
        return code, order_data, message

    def proceed_kiosk_wallet_payment(
        self,
        payment_key: str,
        identifier: str,
        sub_type: str,
    ) -> Tuple[str, Dict[str, Any], Union[str, None]]:
        """Proceed Kiosk or Wallet Payment

        Args:
            payment_key (str): Obtained Payment Key
            identifier (str): Wallet Number or AGGREGATOR for Kiosk Payment
            sub_type (str): AGGREGATOR or WALLET.

        Returns:
            Tuple[str, Dict[str, Any], Union[str, None]]: (Code, Payment Data Dict, Success/Error Message)
        """

        if sub_type == PaymentSubTypes.AGGREGATOR:
            identifier = PaymentSubTypes.AGGREGATOR

        request_body = {
            "source": {
                "identifier": identifier,
                "subtype": sub_type,
            },
            "payment_token": payment_key,
        }

        code, payment_data, message = self.connection.post(
            url=URLsConfig.PAY_URL,
            json=request_body,
        )
        
        # TODO: Validates APIs Return Data Option
        if code == SUCCESS:
            message = "Kiosk or Wallet Payment Processed Successfully"
        return code, payment_data, message
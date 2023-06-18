# Python Standard Library Imports
from typing import Any, Dict, List, Tuple, Union

# Other Third Party Imports
from multimethod import overload

# First Party Imports
from paymob.data_classes import ResponseFeedBack

from .config import URLsConfig
from .connection import AcceptConnection
from .constants import PaymentSubTypes
from .factories import Invoice, Order, Product
from .response_codes import SUCCESS
from .transaction import Transaction


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
        shipping_details: dict = {},
    ) -> Tuple[str, Union[Order, None], ResponseFeedBack]:
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
            Tuple[str, Union[Order, None], ResponseFeedBack]: (Code, Order Insatnce, ResponseFeedBack Instance)
        """
        request_body = {
            "merchant_order_id": merchant_order_id,
            "amount_cents": str(amount_cents),
            "currency": currency,
            "delivery_needed": delivery_needed,
            "items": items,
            "shipping_data": shipping_data,
            "shipping_details": shipping_details,
        }

        code, order_data, feedback = self.connection.post(
            url=URLsConfig.CREATE_ORDER,
            json=request_body,
        )

        # TODO: Validates APIs Return Data Option
        order_instance = None
        if code == SUCCESS:
            order_instance = Order(**order_data)
            feedback.message = "Order with ID: {0} Created Successfully".format(order_instance.id)
        return code, order_instance, feedback

    def get_order(
        self,
        order_id: Union[int, str],
    ) -> Tuple[str, Union[Order, None], Union[str, None]]:
        """Retrives Order Data

        Args:
            order_id (Union[int, str]): Paymob's External Order ID

        Returns:
            Tuple[str, Union[Order, None], ResponseFeedBack]: (Code, Order Instance, ResponseFeedBack Instance)
        """

        code, order_data, feedback = self.connection.get(
            url=URLsConfig.GET_ORDER.format(order_id=order_id),
        )

        # TODO: Validates APIs Return Data Option
        order_instance = None
        if code == SUCCESS:
            order_instance = Order(**order_data)
            feedback.message = "Successfully Retrieved Order: {0}".format(order_id)
        return code, order_instance, feedback

    def create_payment_key(
        self,
        order_id: str,
        amount_cents: str,
        currency: str,
        billing_data: dict,
        integration_id: int,
        card_token_key: str = None,
        expiration: int = 3600,  # 1 Hour
        lock_order_when_paid: bool = False,
    ) -> Tuple[str, str, ResponseFeedBack]:
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
            Tuple[str, str, ResponseFeedBack]: (Code, Payment Key, ResponseFeedBack Instance)
        """

        request_body = {
            "order_id": order_id,
            "amount_cents": str(amount_cents),
            "currency": str(currency),
            "expiration": expiration,
            "integration_id": integration_id,
            "billing_data": billing_data,
            "lock_order_when_paid": lock_order_when_paid,
        }
        if card_token_key:
            request_body["token"] = card_token_key

        code, data, feedback = self.connection.post(
            url=URLsConfig.PAYMENT_KEY,
            json=request_body,
        )

        # TODO: Validates APIs Return Data Option
        payment_key = None
        if code == SUCCESS:
            feedback.message = "Payment Key for Order: {0} Created Successfully".format(order_id)
            payment_key = data.get("token")
        return code, payment_key, feedback

    def proceed_kiosk_payment(
        self,
        payment_key: str,
    ) -> Tuple[str, Union[Transaction, None], ResponseFeedBack]:
        """Proceed Kiosk Payment

        Args:
            payment_key (str): Obtained Payment Key

        Returns:
            Tuple[str, Union[Transaction, None], ResponseFeedBack]: (Code, Payment Data Dict, ResponseFeedBack Instance)
        """

        request_body = {
            "source": {
                "identifier": PaymentSubTypes.AGGREGATOR,
                "subtype": PaymentSubTypes.AGGREGATOR,
            },
            "payment_token": payment_key,
        }

        code, transaction_data, feedback = self.connection.post(
            url=URLsConfig.PAY,
            json=request_body,
        )

        # TODO: Validates APIs Return Data Option
        transaction_instance = None
        if code == SUCCESS:
            transaction_instance = Transaction(connection=self.connection, **transaction_data)
            feedback.message = "Kiosk Payment Processed Successfully"
        return code, transaction_instance, feedback

    def proceed_wallet_payment(
        self,
        payment_key: str,
        identifier: str,
    ) -> Tuple[str, Union[Transaction, None], ResponseFeedBack]:
        """Proceed Wallet Payment

        Args:
            payment_key (str): Obtained Payment Key
            identifier (str): Wallet Number or AGGREGATOR for Kiosk Payment

        Returns:
            Tuple[str, Union[Transaction, None], ResponseFeedBack]: (Code, Payment Data Dict, ResponseFeedBack Instance)
        """

        request_body = {
            "source": {
                "identifier": identifier,
                "subtype": PaymentSubTypes.WALLET,
            },
            "payment_token": payment_key,
        }

        code, transaction_data, feedback = self.connection.post(
            url=URLsConfig.PAY,
            json=request_body,
        )

        # TODO: Validates APIs Return Data Option
        transaction_instance = None
        if code == SUCCESS:
            transaction_instance = Transaction(connection=self.connection, **transaction_data)
            feedback.message = "Wallet Payment for Identifier: {0} Processed Successfully".format(identifier)
        return code, transaction_instance, feedback

    def proceed_cash_payment(
        self,
        payment_key: str,
    ) -> Tuple[str, Union[Transaction, None], ResponseFeedBack]:
        """Proceed Cash Payment

        Args:
            payment_key (str): Obtained Payment Key

        Returns:
            Tuple[str, Union[Transaction, None], ResponseFeedBack]: (Code, Payment Data Dict, ResponseFeedBack Instance)
        """

        request_body = {
            "source": {
                "identifier": PaymentSubTypes.CASH.lower(),
                "subtype": PaymentSubTypes.CASH,
            },
            "payment_token": payment_key,
        }

        code, transaction_data, feedback = self.connection.post(
            url=URLsConfig.PAY,
            json=request_body,
        )

        # TODO: Validates APIs Return Data Option
        transaction_instance = None
        if code == SUCCESS:
            transaction_instance = Transaction(connection=self.connection, **transaction_data)
            feedback.message = "Cash Payment Processed Successfully"
        return code, transaction_instance, feedback

    def proceed_card_token_payment(
        self,
        payment_key: str,
        card_token: str,
    ) -> Tuple[str, Union[Transaction, None], ResponseFeedBack]:
        """Proceed With Saved Card Payment

        Args:
            payment_key (str): Obtained Payment Key
            card_token (str): Saved Card Token

        Returns:
            Tuple[str, Union[Transaction, None], ResponseFeedBack]: (Code, Payment Data Dict, ResponseFeedBack Instance)
        """

        request_body = {
            "source": {
                "identifier": card_token,
                "subtype": PaymentSubTypes.TOKEN,
            },
            "payment_token": payment_key,
        }

        code, transaction_data, feedback = self.connection.post(
            url=URLsConfig.PAY,
            json=request_body,
        )

        # TODO: Validates APIs Return Data Option
        transaction_instance = None
        if code == SUCCESS:
            transaction_instance = Transaction(connection=self.connection, **transaction_data)
            feedback.message = "Payment With Saved Card Token Processed Successfully"
        return code, transaction_instance, feedback

    def create_invoice_link(
        self,
        amount_cents: str,
        shipping_data: Dict[str, Any],
        items: List[Dict[str, Any]],
        currency: str,
        integrations: List[int],
        delivery_needed: bool = False,
    ) -> Tuple[str, Union[Invoice, None], ResponseFeedBack]:
        """_summary_

        Args:
            amount_cents (str): The amount in cents to be paid for in the invoice.
            shipping_data (Dict[str, Any]): The details of the customer or end-user.
            items (List[Dict[str, Any]]): It will include the details of the order.
            currency (str): The currency used in the invoice. By default, it will be EGP.
            integrations (List[int]): The payment methods that will be listed in the invoice link. You should enter the integration ID of every payment method.
            delivery_needed (bool): Determines if you use our delivery. Defaults to False.

        Returns:
            Tuple[str, Union[Invoice, None], ResponseFeedBack]: (Code, Invoice Instance, ResponseFeedBack Instance)
        """

        request_body = {
            "api_source": "INVOICE",
            "amount_cents": amount_cents,
            "currency": currency,
            "shipping_data": shipping_data,
            "integrations": integrations,
            "items": items,
            "delivery_needed": delivery_needed,
        }

        code, invoice_data, feedback = self.connection.post(
            url=URLsConfig.CREATE_INVOICE_LINK,
            json=request_body,
        )

        # TODO: Validates APIs Return Data Option
        invoice_instance = None
        if code == SUCCESS:
            invoice_instance = Invoice(**invoice_data)
            feedback.message = "Invoice Link Data Retrieved Successfully"
        return code, invoice_instance, feedback

    def create_product_link(
        self,
        product_name: str,
        product_description: str,
        amount_cents: str,
        currency: str,
        inventory: str,
        integrations: List[int],
        allow_quantity_edit: bool = False,
        delivery_needed: bool = False,
    ) -> Tuple[str, Union[Product, None], ResponseFeedBack]:
        """Creates a Product Link

        Args:
            product_name (str): The name of your product.
            product_description (str): The description of your product.
            amount_cents (str): The price in cents of the product.
            currency (str): The currency used in the invoice. By default, it will be EGP.
            inventory (str): The stock of your product in your inventory.
            integrations (List[int]): The payment methods that will be listed in the invoice link. You should enter the integration ID of every payment method.
            allow_quantity_edit (bool): If the stock will be reduced when a product is paid for. Defaults to False.
            delivery_needed (bool): Determines if you use our delivery. Defaults to False.

        Returns:
            Tuple[str, Union[Product, None], ResponseFeedBack]: (Code, Product Instance, ResponseFeedBack Instance)
        """

        request_body = {
            "product_name": product_name,
            "product_description": product_description,
            "amount_cents": amount_cents,
            "currency": currency,
            "inventory": inventory,
            "integrations": integrations,
            "allow_quantity_edit": allow_quantity_edit,
            "delivery_needed": delivery_needed,
        }

        code, product_data, feedback = self.connection.post(
            url=URLsConfig.CREATE_PRODUCT_LINK,
            json=request_body,
        )

        # TODO: Validates APIs Return Data Option
        product_instance = None
        if code == SUCCESS:
            product_instance = Product(**product_data)
            feedback.message = "Product Link Data Retrieved Successfully"
        return code, product_instance, feedback

    @overload
    def get_transaction(
        self,
        transaction_id: int,
    ) -> Tuple[str, Union[Transaction, None], ResponseFeedBack]:
        """Retrieves Transaction Data by Transaction ID

        Args:
            transaction_id (int): Paymob's Transaction ID

        Returns:
            Tuple[str, Union[Transaction, None], ResponseFeedBack]: (Code, Transaction Instance, ResponseFeedBack Instance)
        """

        code, transaction_data, feedback = self.connection.get(
            url=URLsConfig.GET_TRANSACTION_ID.format(transaction_id=transaction_id),
        )
        # TODO: Validates APIs Return Data Option
        transaction_instance = None
        if code == SUCCESS:
            transaction_instance = Transaction(connection=self.connection, **transaction_data)
            feedback.message = "Transaction: {0} Retrieved Successfully".format(transaction_instance.id)
        return code, transaction_instance, feedback

    @overload
    def get_transaction(
        self,
        merchant_order_id: str = None,
        order_id: int = None,
    ) -> Tuple[str, Union[Transaction, None], ResponseFeedBack]:
        """Retrieves Transaction Data by Merchant Order ID and Order ID

        Args:
            merchant_order_id (str): Internal Order ID. Defaults to None.
            order_id (int): Paymob's External Order ID. Defaults to None.

        Note: Either merchant order_id or order_id must be passed

        Returns:
            Tuple[str, Union[Transaction, None], ResponseFeedBack]: (Code, Transaction Instance, ResponseFeedBack Instance)
        """

        request_body = {}
        if merchant_order_id:
            request_body["merchant_order_id"] = merchant_order_id
        if order_id:
            request_body["order_id"] = order_id

        code, transaction_data, feedback = self.connection.post(
            url=URLsConfig.GET_TRANSACTION_MERCHANT_ID,
            json=request_body,
        )

        # TODO: Validates APIs Return Data Option
        transaction_instance = None
        if code == SUCCESS:
            transaction_instance = Transaction(connection=self.connection, **transaction_data)
            feedback.message = (
                "Transaction: {0} of Order ID: {1} and Merchant Order ID: {2} Retrieved Successfully".format(
                    transaction_instance.id,
                    order_id,
                    merchant_order_id,
                )
            )
        return code, transaction_instance, feedback

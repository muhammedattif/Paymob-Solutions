# Python Standard Library Imports
from typing import Any, Dict, Tuple, Union

from .accept_connection import AcceptConnection
from .config import URLsConfig
from .data_classes import TransactionDataClass
from .response_codes import SUCCESS


class AcceptTransaction(TransactionDataClass):
    def __init__(self, connection: AcceptConnection, *args, **kwargs) -> None:
        """Initializing Transaction Attributes

        Args:
            connection (AcceptConnection): Accept Connection Insatance
        """
        super().__init__(*args, **kwargs)
        self.connection = connection

    def refund(
        self,
        amount_cents: int,
    ) -> Tuple[str, Dict[str, Any], Union[str, None]]:
        """Refund a Transaction

        Args:
            amount_cents (int): Amount that will be Refunded

        Returns:
            Tuple[str, Dict[str, Any], Union[str, None]]: (Code, Transaction Data Dict, Success/Error Message)
        """

        request_body = {
            "transaction_id": self.obj.id,
            "amount_cents": amount_cents,
        }

        code, transaction_data, message = self.connection.post(
            url=URLsConfig.REFUND_TRANSACTION,
            json=request_body,
        )

        # TODO: Validates APIs Return Data Option
        if code == SUCCESS:
            message = "Transaction: {0} Refund Processed Successfully".format(
                self.obj.id,
            )
        return code, transaction_data, message

    def void(
        self,
    ) -> Tuple[str, Dict[str, Any], Union[str, None]]:
        """Void a Transaction

        Returns:
            Tuple[str, Dict[str, Any], Union[str, None]]: (Code, Transaction Data Dict, Success/Error Message)
        """

        request_body = {
            "transaction_id": self.obj.id,
        }

        code, transaction_data, message = self.connection.post(
            url=URLsConfig.VOID_TRANSACTION,
            json=request_body,
        )

        # TODO: Validates APIs Return Data Option
        if code == SUCCESS:
            message = "Transaction: {0} Void Processed Successfully".format(
                self.obj.id,
            )
        return code, transaction_data, message

    def capture(
        self,
        amount_cents: int,
    ) -> Tuple[str, Dict[str, Any], Union[str, None]]:
        """Capture a Transaction

        Args:
            amount_cents (int): Amount that will be Captured

        Returns:
            Tuple[str, Dict[str, Any], Union[str, None]]: (Code, Transaction Data Dict, Success/Error Message)
        """

        request_body = {
            "transaction_id": self.obj.id,
            "amount_cents": amount_cents,
        }

        code, transaction_data, message = self.connection.post(
            url=URLsConfig.CAPTURE,
            json=request_body,
        )

        # TODO: Validates APIs Return Data Option
        if code == SUCCESS:
            message = "Transaction: {0} Capture Processed Successfully".format(
                self.obj.id,
            )
        return code, transaction_data, message

# Future Imports
from __future__ import annotations

# Python Standard Library Imports
from typing import Tuple, Union

from .config import URLsConfig
from .connection import AcceptConnection
from .data_classes import TransactionDataClass
from .factories import DynamicTransactionFactory
from .response_codes import SUCCESS

# TODO: Allow it to return DynamicTransactionFactory or TransactionDataClass once Validation settings is supported
AbstractTransaction = (
    DynamicTransactionFactory or TransactionDataClass
)  # NOTE: It will always return DynamicTransactionFactory for Now


class Transaction(AbstractTransaction):
    """Final Transaction Class"""

    def __init__(self, connection: AcceptConnection, *args, **kwargs) -> None:
        """Initializing Transaction Attributes

        Args:
            connection (AcceptConnection): Accept Connection Insatance
        """
        super().__init__(*args, **kwargs)
        self.connection = connection

    def __str__(self) -> str:
        if hasattr(self, "id"):
            return f"Transaction No: {self.id}"
        return self.__repr__()

    def refund(
        self,
        amount_cents: int,
    ) -> Tuple[str, Union[Transaction, None], Union[str, None]]:
        """Refund a Transaction

        Args:
            amount_cents (int): Amount that will be Refunded

        Returns:
            Tuple[str, Union[Transaction, None], Union[str, None]]: (Code, Transaction Instance, Success/Error Message)
        """

        request_body = {
            "transaction_id": self.id,
            "amount_cents": amount_cents,
        }

        code, transaction_data, message = self.connection.post(
            url=URLsConfig.REFUND_TRANSACTION,
            json=request_body,
        )

        # TODO: Validates APIs Return Data Option
        transaction_instance = None
        if code == SUCCESS:
            transaction_instance = Transaction(connection=self.connection, **transaction_data)
            message = "Transaction: {0} Refund Processed Successfully".format(
                self.id,
            )
        return code, transaction_instance, message

    def void(
        self,
    ) -> Tuple[str, Union[Transaction, None], Union[str, None]]:
        """Void a Transaction

        Returns:
            Tuple[str, Union[Transaction, None], Union[str, None]]: (Code, Transaction Instance, Success/Error Message)
        """

        request_body = {
            "transaction_id": self.id,
        }

        code, transaction_data, message = self.connection.post(
            url=URLsConfig.VOID_TRANSACTION,
            json=request_body,
        )

        # TODO: Validates APIs Return Data Option
        transaction_instance = None
        if code == SUCCESS:
            transaction_instance = Transaction(connection=self.connection, **transaction_data)
            message = "Transaction: {0} Void Processed Successfully".format(
                self.id,
            )
        return code, transaction_instance, message

    def capture(
        self,
        amount_cents: int,
    ) -> Tuple[str, Union[Transaction, None], Union[str, None]]:
        """Capture a Transaction

        Args:
            amount_cents (int): Amount that will be Captured

        Returns:
            Tuple[str, Union[Transaction, None], Union[str, None]]: (Code, Transaction Instance, Success/Error Message)
        """

        request_body = {
            "transaction_id": self.id,
            "amount_cents": amount_cents,
        }

        code, transaction_data, message = self.connection.post(
            url=URLsConfig.CAPTURE,
            json=request_body,
        )

        # TODO: Validates APIs Return Data Option
        transaction_instance = None
        if code == SUCCESS:
            transaction_instance = Transaction(connection=self.connection, **transaction_data)
            message = "Transaction: {0} Capture Processed Successfully".format(
                self.id,
            )
        return code, transaction_instance, message

# First Party Imports
from paymob.accept.factories import DynamicTransactionFactory
from paymob.accept.hmac_validator import HMACValidator


class TransactionCallback(HMACValidator, DynamicTransactionFactory):
    pass


__all__ = ["TransactionCallback"]

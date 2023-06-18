# First Party Imports
from paymob.accept.factories import CardTokenCallbackFactory
from paymob.accept.hmac_validator import HMACValidator


class CardTokenCallback(HMACValidator, CardTokenCallbackFactory):
    pass


__all__ = ["CardTokenCallback"]

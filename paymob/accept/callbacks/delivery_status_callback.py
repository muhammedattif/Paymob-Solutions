# First Party Imports
from paymob.accept.factories import DeliveryStatusCallbackFactory
from paymob.accept.hmac_validator import HMACValidator


class DeliveryStatusCallback(HMACValidator, DeliveryStatusCallbackFactory):
    pass


__all__ = ["DeliveryStatusCallback"]

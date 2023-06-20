# First Party Imports
from paymob.accept.constants import AcceptCallbackTypes

from .card_token_callback import CardTokenCallback
from .delivery_status_callback import DeliveryStatusCallback
from .transaction_callback import TransactionCallback


def AcceptCallback(incoming_hmac, callback_dict):

    callback_type = callback_dict.get("type")
    callback_class = None
    if callback_type == AcceptCallbackTypes.TRANSACTION:
        callback_class = TransactionCallback
    elif callback_type == AcceptCallbackTypes.CARD_TOKEN:
        callback_class = CardTokenCallback
    elif callback_type == AcceptCallbackTypes.DELIVERY_STATUS:
        callback_class = DeliveryStatusCallback
    else:
        raise TypeError("Invalid Callback Type")

    return callback_class(incoming_hmac=incoming_hmac, callback_dict=callback_dict, **callback_dict)

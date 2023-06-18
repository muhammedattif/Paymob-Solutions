# Other Third Party Imports
from decouple import config

# Constants
ACCEPT_APIS_TIMEOUT_SECONDES = config("ACCEPT_APIS_TIMEOUT_SECONDES", cast=int, default=10)

# Credentials Config
class Credentials:
    ACCEPT_API_KEY = config("ACCEPT_API_KEY", default="")
    ACCEPT_HMAC_SECRET = config("ACCEPT_HMAC_SECRET", default="")


# URLs Config
class URLsConfig:
    ACCEPT_BASE_URL = config("PAYMOB_ACCEPT_BASE_URL", default="https://accept.paymob.com")
    AUTH_TOKEN = ACCEPT_BASE_URL + "/api/auth/tokens"
    CREATE_ORDER = ACCEPT_BASE_URL + "/api/ecommerce/orders"
    GET_ORDER = ACCEPT_BASE_URL + "/api/ecommerce/orders/{order_id}"
    PAYMENT_KEY = ACCEPT_BASE_URL + "/api/acceptance/payment_keys"
    PAY = ACCEPT_BASE_URL + "/api/acceptance/payments/pay"
    IFRAME = ACCEPT_BASE_URL + "/api/acceptance/iframes/{iframe_id}?payment_token={payment_key}"
    GET_TRANSACTION_ID = ACCEPT_BASE_URL + "/api/acceptance/transactions/{transaction_id}"
    GET_TRANSACTION_MERCHANT_ID = ACCEPT_BASE_URL + "/api/ecommerce/orders/transaction_inquiry"
    REFUND_TRANSACTION = ACCEPT_BASE_URL + "/api/acceptance/void_refund/refund"
    VOID_TRANSACTION = ACCEPT_BASE_URL + "/api/acceptance/void_refund/void"
    CAPTURE = ACCEPT_BASE_URL + "/api/acceptance/capture"
    CREATE_INVOICE_LINK = ACCEPT_BASE_URL + "/api/ecommerce/orders"
    CREATE_PRODUCT_LINK = ACCEPT_BASE_URL + "/api/ecommerce/products"

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
    ACCEPT_BASE_URL = config("PAYMOB_ACCEPT_BASE_URL", default="https://accept.paymobsolutions.com")
    AUTH_TOKEN_URL = "{0}/api/auth/tokens".format(ACCEPT_BASE_URL)
    CREATE_ORDER_URL = "{0}/api/ecommerce/orders".format(ACCEPT_BASE_URL)
    GET_ORDER_URL = "{0}/api/ecommerce/orders/".format(ACCEPT_BASE_URL) + "{order_id}"
    PAYMENT_KEY_URL = "{0}/api/acceptance/payment_keys".format(ACCEPT_BASE_URL)
    PAY_URL = "{0}/api/acceptance/payments/pay".format(ACCEPT_BASE_URL)
    IFRAME_URL = "{0}/api/acceptance/iframes".format(ACCEPT_BASE_URL) + "/{iframe_id}?payment_token={payment_token}"

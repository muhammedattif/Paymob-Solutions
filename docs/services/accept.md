# Requirements

Before starting to use Accept APIs it needs to be configured with your account's secret keys which is
available in your [Accept Paymob Dashboard][accept-dashboard]. in `.env` Set the following variables:
```
ACCEPT_API_KEY=<YOUR API KEY>
ACCEPT_HMAC_SECRET=<YOUR HMAC SECRET>
```

After setting up your secret keys, now you can use Accept API interfaces.

#### Initialize `AcceptAPIClient`

```python
from paymob.accept import AcceptAPIClient

accept_api_client = AcceptAPIClient()
```

by initializing an object from `AcceptAPIClient` a TCP connection session is established with Paymob and an `Auth Token` is automatically retrieved.

#### Create Order

**Example**

```python
from paymob.accept import AcceptAPIClient
from paymob.accept.utils import AcceptUtils

accept_api_client = AcceptAPIClient()

mid_key = "<Type>" # MidKey is useful if you support multiple types of items.
identifier = "<Internal Order ID>"
merchant_order_id = AcceptUtils.generate_merchant_order_id(mid_key=mid_key, identifier=identifier)
amount_cents = 1000
currency = "EGP"

code, order_data, message = accept_api_client.create_order(
    merchant_order_id=merchant_order_id,
    amount_cents=amount_cents,
    currency=currency
)
```

**Parameters**

| Parameter | Required? | Default | Description |
| --- | --- | --- | --- |
| `merchant_order_id` | `Yes` | - |  Your Internal Order ID |
| `amount_cents` | `Yes` | - |  The price of the order in cents. |
| `currency` | `Yes` | - |  The currency related to this payment |
| `delivery_needed` | `No` | `False` | Set it to be true if your order needs to be delivered by Accept's product delivery services |
| `items` | `No` | `list` |  list of objects contains the contents of the order if it is existing, send it as empty array if it is not available. However, Mandatory for Souhoula and GET_GO payment methods |
| `shipping_data` | `No` | `dict` |  Mandatory if your order needs to be delivered, otherwise you can delete the whole object |
| `shipping_details` | `No` | `dict` |  Mandatory if your order needs to be delivered, otherwise you can delete the whole object |



#### Create Payment Key

**Example**

```python
from paymob.accept import AcceptAPIClient
from paymob.accept.utils import AcceptUtils

accept_api_client = AcceptAPIClient()

order_id = "<order_id>"
amount_cents = 1000
currency = "EGP"
billing_data = {}
integration_id = <Your Integration ID>
code, order_data, message = accept_api_client.create_payment_key(
    order_id=order_id,
    amount_cents=amount_cents,
    currency=currency,
    billing_data=billing_data,
    integration_id=integration_id,
)
```

**Parameters**

| Parameter | Required? | Default | Description |
| --- | --- | --- | --- |
| `order_id` | `Yes` | - | Order ID retrieved from [Create Order API](#create-order) |
| `amount_cents` | `Yes` | - | The price should be paid through this payment channel with this payment key token |
| `currency` | `Yes` | - | The currency related to this payment |
| `billing_data` | `Yes` | `dict` | The billing data related to the customer related to this payment |
| `integration_id` | `Yes` | `False` | An identifier for the payment channel you want your customer to pay through |
| `card_token_key` | `No` | `str` | Card Token received from token callback if the user choices to save his card information for future payment |
| `expiration` | `No` | `int` | The expiration time of this payment token in seconds. (The maximum is 3600 seconds which is an hour) |
| `lock_order_when_paid` | `No` | `False` | A flag prevent this order to be paid again if it is paid |


[accept-dashboard]: https://accept.paymob.com/portal2/en/home

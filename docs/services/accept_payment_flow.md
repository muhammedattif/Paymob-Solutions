# Iframe Flow Full Example 

```python
from paymob.accept import AcceptAPIClient
from paymob.accept.response_codes import SUCCESS
from paymob.accept.utils import AcceptUtils

# 1- Initialize Accept API Client
accept_api_client = AcceptAPIClient()

# 2- Create Order
mid_key = "Service" # MidKey is useful if you support multiple types of items.
identifier = "1"
merchant_order_id = AcceptUtils.generate_merchant_order_id(mid_key=mid_key, identifier=identifier)
amount_cents = 1000
currency = "EGP"
items = [
    {
        "name": "ASC1515",
        "amount_cents": "1000",
        "description": "Smart Watch",
        "quantity": "1"
    }
]
shipping_data = {
    "apartment": "803", 
    "email": "claudette09@exa.com", 
    "floor": "42", 
    "first_name": "Clifford", 
    "street": "Ethan Land", 
    "building": "8028", 
    "phone_number": "+86(8)9135210487", 
    "postal_code": "01898", 
     "extra_description": "8 Ram , 128 Giga",
    "city": "Jaskolskiburgh", 
    "country": "CR", 
    "last_name": "Nicolas", 
    "state": "Utah"
}
shipping_details = {
    "notes" : " test",
    "number_of_packages": 1,
    "weight" : 1,
    "weight_unit" : "Kilogram",
    "length" : 1,
    "width" :1,
    "height" :1,
    "contents" : "product of some sorts"
}
code, order, feedback = accept_api_client.create_order(
    merchant_order_id=merchant_order_id,
    amount_cents=amount_cents,
    currency=currency,
    items=items,
    shipping_data=shipping_data,
    shipping_details=shipping_details
)
# NOTE: You have to check the code before proceeding to the next step

amount_cents = 1000
currency = "EGP"
billing_data = {
    "apartment": "803", 
    "email": "claudette09@exa.com", 
    "floor": "42", 
    "first_name": "Clifford", 
    "street": "Ethan Land", 
    "building": "8028", 
    "phone_number": "+86(8)9135210487", 
    "shipping_method": "PKG", 
    "postal_code": "01898", 
    "city": "Jaskolskiburgh", 
    "country": "CR", 
    "last_name": "Nicolas", 
    "state": "Utah"
}
integration_id = 1
code, payment_key, feedback = accept_api_client.create_payment_key(
    order_id=order.id,
    amount_cents=amount_cents,
    currency=currency,
    billing_data=billing_data,
    integration_id=integration_id,
    billing_data=billing_data
)

# NOTE: You have to check the code/payment_key before proceeding to the next step

iframe_id = 1
iframe_url = AcceptUtils.create_iframe_url(
    iframe_id=iframe_id,
    payment_key=payment_key
)
print(f"Payment Key: {payment_key}")
print(f"Iframe URL: {iframe_url}")
```

**Output**:
```bash 
Payment Key ID: *****
Iframe URL: https://accept.paymob.com/api/acceptance/iframes/1?payment_token=*****
```


# Wallet Payment Full Example 

```python
from paymob.accept import AcceptAPIClient
from paymob.accept.response_codes import SUCCESS
from paymob.accept.utils import AcceptUtils

# 1- Initialize Accept API Client
accept_api_client = AcceptAPIClient()

# 2- Create Order
mid_key = "Service" # MidKey is useful if you support multiple types of items.
identifier = "1"
merchant_order_id = AcceptUtils.generate_merchant_order_id(mid_key=mid_key, identifier=identifier)
amount_cents = 1000
currency = "EGP"
items = [
    {
        "name": "ASC1515",
        "amount_cents": "1000",
        "description": "Smart Watch",
        "quantity": "1"
    }
]
shipping_data = {
    "apartment": "803", 
    "email": "claudette09@exa.com", 
    "floor": "42", 
    "first_name": "Clifford", 
    "street": "Ethan Land", 
    "building": "8028", 
    "phone_number": "+86(8)9135210487", 
    "postal_code": "01898", 
     "extra_description": "8 Ram , 128 Giga",
    "city": "Jaskolskiburgh", 
    "country": "CR", 
    "last_name": "Nicolas", 
    "state": "Utah"
}
shipping_details = {
    "notes" : " test",
    "number_of_packages": 1,
    "weight" : 1,
    "weight_unit" : "Kilogram",
    "length" : 1,
    "width" :1,
    "height" :1,
    "contents" : "product of some sorts"
}
code, order, feedback = accept_api_client.create_order(
    merchant_order_id=merchant_order_id,
    amount_cents=amount_cents,
    currency=currency,
    items=items,
    shipping_data=shipping_data,
    shipping_details=shipping_details
)
# NOTE: You have to check the code before proceeding to the next step

amount_cents = 1000
currency = "EGP"
billing_data = {
    "apartment": "803", 
    "email": "claudette09@exa.com", 
    "floor": "42", 
    "first_name": "Clifford", 
    "street": "Ethan Land", 
    "building": "8028", 
    "phone_number": "+86(8)9135210487", 
    "shipping_method": "PKG", 
    "postal_code": "01898", 
    "city": "Jaskolskiburgh", 
    "country": "CR", 
    "last_name": "Nicolas", 
    "state": "Utah"
}
integration_id = 1
code, payment_key, feedback = accept_api_client.create_payment_key(
    order_id=order.id,
    amount_cents=amount_cents,
    currency=currency,
    billing_data=billing_data,
    integration_id=integration_id,
    billing_data=billing_data
)

# NOTE: You have to check the code/payment_key before proceeding to the next step

identifier = "01000000000"
code, transaction, feedback = accept_api_client.proceed_wallet_payment(
    payment_key=payment_key,
    identifier=identifier
)
# NOTE: You have to check the code before accessing redirect_url
print(f"Redirect URL: {transaction.redirect_url}")

```

**Output**:
```bash 
Redirect URL: https://accept.paymob.com/****
```


# Kiosk Payment Full Example 

```python
from paymob.accept import AcceptAPIClient
from paymob.accept.response_codes import SUCCESS
from paymob.accept.utils import AcceptUtils

# 1- Initialize Accept API Client
accept_api_client = AcceptAPIClient()

# 2- Create Order
mid_key = "Service" # MidKey is useful if you support multiple types of items.
identifier = "1"
merchant_order_id = AcceptUtils.generate_merchant_order_id(mid_key=mid_key, identifier=identifier)
amount_cents = 1000
currency = "EGP"
items = [
    {
        "name": "ASC1515",
        "amount_cents": "1000",
        "description": "Smart Watch",
        "quantity": "1"
    }
]
shipping_data = {
    "apartment": "803", 
    "email": "claudette09@exa.com", 
    "floor": "42", 
    "first_name": "Clifford", 
    "street": "Ethan Land", 
    "building": "8028", 
    "phone_number": "+86(8)9135210487", 
    "postal_code": "01898", 
     "extra_description": "8 Ram , 128 Giga",
    "city": "Jaskolskiburgh", 
    "country": "CR", 
    "last_name": "Nicolas", 
    "state": "Utah"
}
shipping_details = {
    "notes" : " test",
    "number_of_packages": 1,
    "weight" : 1,
    "weight_unit" : "Kilogram",
    "length" : 1,
    "width" :1,
    "height" :1,
    "contents" : "product of some sorts"
}
code, order, feedback = accept_api_client.create_order(
    merchant_order_id=merchant_order_id,
    amount_cents=amount_cents,
    currency=currency,
    items=items,
    shipping_data=shipping_data,
    shipping_details=shipping_details
)
# NOTE: You have to check the code before proceeding to the next step

amount_cents = 1000
currency = "EGP"
billing_data = {
    "apartment": "803", 
    "email": "claudette09@exa.com", 
    "floor": "42", 
    "first_name": "Clifford", 
    "street": "Ethan Land", 
    "building": "8028", 
    "phone_number": "+86(8)9135210487", 
    "shipping_method": "PKG", 
    "postal_code": "01898", 
    "city": "Jaskolskiburgh", 
    "country": "CR", 
    "last_name": "Nicolas", 
    "state": "Utah"
}
integration_id = 1
code, payment_key, feedback = accept_api_client.create_payment_key(
    order_id=order.id,
    amount_cents=amount_cents,
    currency=currency,
    billing_data=billing_data,
    integration_id=integration_id,
    billing_data=billing_data
)

# NOTE: You have to check the code/payment_key before proceeding to the next step

code, transaction, feedback = accept_api_client.proceed_kiosk_payment(
    payment_key=payment_key,
)
# NOTE: You have to check the code before accessing bill_reference
print(f"Bill Reference: {transaction.data.bill_reference}")
```

**Output**:
```bash
Bill Reference: 123456789
```


# CASH Payment Full Example 

```python
from paymob.accept import AcceptAPIClient
from paymob.accept.response_codes import SUCCESS
from paymob.accept.utils import AcceptUtils

# 1- Initialize Accept API Client
accept_api_client = AcceptAPIClient()

# 2- Create Order
mid_key = "Service" # MidKey is useful if you support multiple types of items.
identifier = "1"
merchant_order_id = AcceptUtils.generate_merchant_order_id(mid_key=mid_key, identifier=identifier)
amount_cents = 1000
currency = "EGP"
items = [
    {
        "name": "ASC1515",
        "amount_cents": "1000",
        "description": "Smart Watch",
        "quantity": "1"
    }
]
shipping_data = {
    "apartment": "803", 
    "email": "claudette09@exa.com", 
    "floor": "42", 
    "first_name": "Clifford", 
    "street": "Ethan Land", 
    "building": "8028", 
    "phone_number": "+86(8)9135210487", 
    "postal_code": "01898", 
     "extra_description": "8 Ram , 128 Giga",
    "city": "Jaskolskiburgh", 
    "country": "CR", 
    "last_name": "Nicolas", 
    "state": "Utah"
}
shipping_details = {
    "notes" : " test",
    "number_of_packages": 1,
    "weight" : 1,
    "weight_unit" : "Kilogram",
    "length" : 1,
    "width" :1,
    "height" :1,
    "contents" : "product of some sorts"
}
code, order, feedback = accept_api_client.create_order(
    merchant_order_id=merchant_order_id,
    amount_cents=amount_cents,
    currency=currency,
    items=items,
    shipping_data=shipping_data,
    shipping_details=shipping_details
)
# NOTE: You have to check the code before proceeding to the next step

amount_cents = 1000
currency = "EGP"
billing_data = {
    "apartment": "803", 
    "email": "claudette09@exa.com", 
    "floor": "42", 
    "first_name": "Clifford", 
    "street": "Ethan Land", 
    "building": "8028", 
    "phone_number": "+86(8)9135210487", 
    "shipping_method": "PKG", 
    "postal_code": "01898", 
    "city": "Jaskolskiburgh", 
    "country": "CR", 
    "last_name": "Nicolas", 
    "state": "Utah"
}
integration_id = 1
code, payment_key, feedback = accept_api_client.create_payment_key(
    order_id=order.id,
    amount_cents=amount_cents,
    currency=currency,
    billing_data=billing_data,
    integration_id=integration_id,
    billing_data=billing_data
)

# NOTE: You have to check the code/payment_key before proceeding to the next step

code, transaction, feedback = accept_api_client.proceed_cash_payment(
    payment_key=payment_key,
)

# NOTE: You have to check the code before accessing transaction attributes
print(f"Transaction ID: {transaction.id}")
```

**Output**:
```bash
Transaction ID: 1
```


# Card Token Payment Full Example 

```python
from paymob.accept import AcceptAPIClient
from paymob.accept.response_codes import SUCCESS
from paymob.accept.utils import AcceptUtils

# 1- Initialize Accept API Client
accept_api_client = AcceptAPIClient()

# 2- Create Order
mid_key = "Service" # MidKey is useful if you support multiple types of items.
identifier = "1"
merchant_order_id = AcceptUtils.generate_merchant_order_id(mid_key=mid_key, identifier=identifier)
amount_cents = 1000
currency = "EGP"
items = [
    {
        "name": "ASC1515",
        "amount_cents": "1000",
        "description": "Smart Watch",
        "quantity": "1"
    }
]
shipping_data = {
    "apartment": "803", 
    "email": "claudette09@exa.com", 
    "floor": "42", 
    "first_name": "Clifford", 
    "street": "Ethan Land", 
    "building": "8028", 
    "phone_number": "+86(8)9135210487", 
    "postal_code": "01898", 
     "extra_description": "8 Ram , 128 Giga",
    "city": "Jaskolskiburgh", 
    "country": "CR", 
    "last_name": "Nicolas", 
    "state": "Utah"
}
shipping_details = {
    "notes" : " test",
    "number_of_packages": 1,
    "weight" : 1,
    "weight_unit" : "Kilogram",
    "length" : 1,
    "width" :1,
    "height" :1,
    "contents" : "product of some sorts"
}
code, order, feedback = accept_api_client.create_order(
    merchant_order_id=merchant_order_id,
    amount_cents=amount_cents,
    currency=currency,
    items=items,
    shipping_data=shipping_data,
    shipping_details=shipping_details
)
# NOTE: You have to check the code before proceeding to the next step

amount_cents = 1000
currency = "EGP"
billing_data = {
    "apartment": "803", 
    "email": "claudette09@exa.com", 
    "floor": "42", 
    "first_name": "Clifford", 
    "street": "Ethan Land", 
    "building": "8028", 
    "phone_number": "+86(8)9135210487", 
    "shipping_method": "PKG", 
    "postal_code": "01898", 
    "city": "Jaskolskiburgh", 
    "country": "CR", 
    "last_name": "Nicolas", 
    "state": "Utah"
}
integration_id = 1
code, payment_key, feedback = accept_api_client.create_payment_key(
    order_id=order.id,
    amount_cents=amount_cents,
    currency=currency,
    billing_data=billing_data,
    integration_id=integration_id,
    billing_data=billing_data
)

# NOTE: You have to check the code/payment_key before proceeding to the next step

card_token = "****"
code, transaction, feedback = accept_api_client.proceed_card_token_payment(
    payment_key=payment_key,
    card_token=card_token
)

# NOTE: You have to check the code before accessing transaction attributes
print(f"Transaction ID: {transaction.id}")
```

**Output**:
```bash
Transaction ID: 1
```

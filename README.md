# Paymob Python Package

[![python](https://img.shields.io/badge/Python-v3.8-3776AB.svg?style=flat&logo=python&logoColor=yellow)](https://www.python.org)  [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)  [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
  - [Services](#services)
  - [Handling APIs Response](#handling-apis-response)
- [Codes Reference](#codes-reference)

# Description

The Paymob Python package provides convenient access to the `Paymob` APIs from applications written in the Python language.
Current version only supports the following services:
- `Accept`

`Payouts` and the other services will be added in the next releases.

# Requirements
Before you begin, ensure you have met the following requirements:
* Python 3.8+
* You have installed the latest version of [python-decouple](https://pypi.org/project/python-decouple)

# Installation Instructions

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

```bash
pip install --upgrade paymob
```

# Usage

### Services

1- [Accept Client](docs/services/accept.md)

---

### Handling APIs Response

Each API Call retrieves a tuple which contains three values (Code, An Object of the API's Return, ResponseFeedBack Instance)

- **Code**: A Number that represents API state. [Codes Reference](#codes-reference) <span id="code"></span>
- **API's Return Object**: An object class of the API's Return and its attributes can be accessed using dot notation.
- **Response FeedBack**: An object of `ResponseFeedBack` class which has the following attributes: <span id="feedback"></span>
    - `message`: A human readable description of the [Code](#code)
    - `data`: A `dict` represents the actual API's Response
    - `status_code`: Status code that has been returned from the API (`2xx`, `4xx`, `5xx`)

**Successful API calls will return the following values:**

- **Code**: [One of the Following Codes](#success-codes)
- **API's Return Object**: `object` (Depending on the API response)
- **Response FeedBack**: `ResponseFeedBack` Object with the following attributes:
    - `message`: A success message depending on the API (Example: Get Order API will return a message like "Successfully Retrieved Order: 1")
    - `data`: `None`
    - `status_code`: `2xx`

**Example:**
```python
from paymob.accept import AcceptAPIClient

accept_api_client = AcceptAPIClient()
code, transaction, feedback = accept_api_client.get_transaction(
    transaction_id=112233
)

print(f"Code: {code}")
print(f"Transaction: {transaction}")
print(f"Transaction ID: {transaction.id}")
print(f"Feedback Message: {feedback.message}")
print(f"Feedback Data: {feedback.data}")
print(f"Feedback Status Code: {feedback.status_code}")
```

Output:
```bash
Code: 10
Transaction: Transaction No: 111859918
Transaction ID: 111859918
Feedback Message: Transaction: 111859918 Retrieved Successfully
Feedback Data: None
Feedback Status Code: 200
```


**Unsuccessful API calls will return the following values:**

- **Code**: [One of the Following Codes](#error-codes)
- **API's Return Object**: Example: Get Transaction API will return a `Transaction` instance (transaction.id, transaction.success, ..etc)
- **Response FeedBack**: `ResponseFeedBack` Object with the following attributes:
    - `message`: A failure message depending on exception occured (Example: "An Error Occurred During the Request")
    - `data`: API's response `dict` (`response.json()`)
    - `status_code`: `4xx` or `5xx`


**Example:**
```python
from paymob.accept import AcceptAPIClient

accept_api_client = AcceptAPIClient()
code, transaction, feedback = accept_api_client.get_transaction(
    transaction_id=112233
)

print(f"Code: {code}")
print(f"Transaction: {transaction}")
print(f"Feedback Message: {feedback.message}")
print(f"Feedback Data: {feedback.data}")
print(f"Feedback Status Code: {feedback.status_code}")
```

Output:
```bash
Code: 22
Transaction: None
Feedback Message: Non 2xx Status Code Returned.
Feedback Data: {'detail': 'Not found.'}
Feedback Status Code: 404
```

-----

# Codes Reference

### Success Codes
| Variable | Code | Description | 
| --- | --- | --- |
| `SUCCESS` | `10` | API Called Successfully Without any Failures |

### Error Codes
| Variable | Code | Description | 
| --- | --- | --- |
| `JSON_DECODE_EXCEPTION` | `20` | An Error Occurred While Parsing the Response into JSON |
| `REQUEST_EXCEPTION` | `21` | An Error Occurred During the Request |
| `HTTP_EXCEPTION` | `22` | Non 2xx Status Code Returned |
| `UNHANDLED_EXCEPTION` | `23` | Unhandled Exception [comment]: # Trace Error will be provided in the [message](#message) |


You can import these codes like the following: 
```python
from paymob.accept.response_codes import (
    SUCCESS, 
    JSON_DECODE_EXCEPTION, 
    REQUEST_EXCEPTION, 
    HTTP_EXCEPTION, 
    UNHANDLED_EXCEPTION
)
```

----

# Settings

You can customized some behaves of `Paymob` by adding the following settings in `.env` file.

**- ACCEPT_APIS_TIMEOUT_SECONDES**

Sets Timeout for API Calls (The connect timeout is the number of seconds Requests will wait for your client to establish a connection or read data with/from `Paymob` server)

**Example:**
```bash
ACCEPT_APIS_TIMEOUT_SECONDES=20
```

**- VALIDATE_API_RESPONSE** (Not Added Yet)

Automatically validates the returned data of the APIs to ensure that there are no changed keys or data types

# Paymob Python Package

[![python](https://img.shields.io/badge/Python-v3.8-3776AB.svg?style=flat&logo=python&logoColor=yellow)](https://www.python.org)  [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)  [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Table of Contents

- [Description](#1--description)
- [Requirements](#2--requirements)
- [Installation Instructions](#3--installation-instructions)
- [Usage](#4--usage)
  - [Services](#41-services)
  - [Handling APIs Response](#42-handling-apis-response)
- [Codes Reference](#5--codes-reference)

# 1- Description

The Paymob Python package provides convenient access to the `Paymob` APIs from applications written in the Python language.
Current version only supports the following services:
- `Accept`

`Payouts` and other services will be added in the next releases.

# 2- Requirements
Before you begin, ensure you have met the following requirements:
* Python 3.8+

# 3- Installation Instructions

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

```bash
pip install --upgrade paymob-solutions
```

# 4- Usage

### 4.1 Services

1- [Accept](docs/services/accept.md)

---

### 4.2 Handling APIs Response

Each API Call retrieves a tuple which contains three values (Code, An Object of the API's Return, ResponseFeedBack Instance)

- **Code**: A Number that represents API state. [Codes Reference](#codes-reference) <span id="code"></span>
- **API's Return Object**: An object class of the API's Return and its attributes can be accessed using dot notation.
- **Response FeedBack**: An object of `ResponseFeedBack` class which has the following attributes: <span id="feedback"></span>
    - `message`: A human readable description of the [Code](#code)
    - `data`: A `dict` represents the actual API's Response
    - `status_code`: Status code that has been returned from the API (`2xx`, `4xx`, `5xx`)
    - `exception_error`: In case an exception is raised (Based on this [Codes](#error-codes)), you can see the error using this attribute.

**Successful API calls will return the following values:**

- **Code**: [One of the Following Codes](#success-codes)
- **API's Return Object**: `object` (Depending on the API response)
- **Response FeedBack**: `ResponseFeedBack` Object with the following attributes:
    - `message`: A success message depending on the API (Example: Get Order API will return a message like "Successfully Retrieved Order: 1")
    - `data`: `None`
    - `status_code`: `2xx`
    - `exception_error`: `None`

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
print(f"Feedback Exception Error: {feedback.exception_error}")
```

Output:
```bash
Code: 10
Transaction: Transaction No: 111859918
Transaction ID: 111859918
Feedback Message: Transaction: 111859918 Retrieved Successfully
Feedback Data: None
Feedback Status Code: 200
Feedback Exception Error: None
```


**Unsuccessful API calls will return the following values:**

- **Code**: [One of the Following Codes](#error-codes)
- **API's Return Object**: Example: Get Transaction API will return a `Transaction` instance (transaction.id, transaction.success, ..etc)
- **Response FeedBack**: `ResponseFeedBack` Object with the following attributes:
    - `message`: A failure message depending on exception occured (Example: "An Error Occurred During the Request")
    - `data`: API's response `dict` (`response.json()`)
    - `status_code`: `4xx` or `5xx`
    - `exception_error`: `Expecting value: line 1 column 1 (char 0)`


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
print(f"Feedback Exception Error: {feedback.exception_error}")

```

Output:
```bash
Code: 22
Transaction: None
Feedback Message: Non 2xx Status Code Returned.
Feedback Data: {'detail': 'Not found.'}
Feedback Status Code: 404
Feedback Exception Error: 404 Client Error: Not Found for url: https://accept.paymob.com/api/acceptance/transactions/112233
```

-----

# 5- Codes Reference

### 5.1 Success Codes
| Variable | Code | Description | 
| --- | --- | --- |
| `SUCCESS` | `10` | API Called Successfully Without any Failures |

### 5.2 Error Codes
| Variable | Code | Description | 
| --- | --- | --- |
| `JSON_DECODE_EXCEPTION` | `20` | An Error Occurred While Parsing the Response into JSON |
| `REQUEST_EXCEPTION` | `21` | An Error Occurred During the Request |
| `HTTP_EXCEPTION` | `22` | Non 2xx Status Code Returned |
| `UNHANDLED_EXCEPTION` | `23` | Unhandled Exception |


You can import these codes like the following: 
```python
from paymob.response_codes import (
    SUCCESS, 
    JSON_DECODE_EXCEPTION, 
    REQUEST_EXCEPTION, 
    HTTP_EXCEPTION, 
    UNHANDLED_EXCEPTION
)
```

----

# 6- Settings

You can customized some behaves of `Paymob` by adding the following settings in `.env` file.

**- ACCEPT_APIS_TIMEOUT_SECONDES**

Sets Timeout for API Calls (The connect timeout is the number of seconds Requests will wait for your client to establish a connection or read data with/from `Paymob` server)

Default value is `10`

**Example:**
```bash
ACCEPT_APIS_TIMEOUT_SECONDES=20
```

**- VALIDATE_API_RESPONSE** (Not Added Yet)

Automatically validates the returned data of the APIs to ensure that there are no changed keys or data types

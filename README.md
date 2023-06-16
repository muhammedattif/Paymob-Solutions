# Paymob Python Library

[![python](https://img.shields.io/badge/Python-v3.8-3776AB.svg?style=flat&logo=python&logoColor=yellow)](https://www.python.org)


# Description

The Paymob Python library provides convenient access to the `Paymob` APIs from applications written in the Python language.
Current version only supports the following services:
- Accept

The rest of the services will be added in the next releases.

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

Each API Call retrieves a tuple which contains three values (Code, Data, Message)

- **Code**: A Number that represents API state. [Codes Reference](#codes-reference) <span id="code"></span>
- **Data**: The returned data from the API.
- **Message**: A human readable description of the [Code](#code). (You can use this message for debugging) <span id="message"></span>


**Successful API calls will return the following values:**

- **Code**: [One of the Following Codes](#success-codes)
- **Data**: `dict`, `list`, or `object` (Depending on the API response)
- **Message**: Success meesage (Varies depending on what the API done)

**Unsuccessful API calls will return the following values:**

- **Code**: [One of the Following Codes](#error-codes)
- **Data**: `None`
- **Message**: Error meesage (Varies depending on the returned [code](#code))


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


You can import these codes from 
```python
from paymob.accept.response_codes import (
    SUCCESS, 
    JSON_DECODE_EXCEPTION, 
    REQUEST_EXCEPTION, 
    HTTP_EXCEPTION, 
    UNHANDLED_EXCEPTION
)
```

# Settings

You can customized some behaves of `Paymob` by adding the following settings in `.env` file.

**- ACCEPT_APIS_TIMEOUT_SECONDES**

Sets Timeout for API Calls (The connect timeout is the number of seconds Requests will wait for your client to establish a connection or read data with/from `Paymob` server)

**- VALIDATE_API_RESPONSE** (Not Added Yet)

Automatically validates the returned data of the APIs to ensure that there are no changed keys or data types

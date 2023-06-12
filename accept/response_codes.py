# Response Codes
SUCCESS = 10

# Request Related Error Codes
JSON_DECODE_EXCEPTION = 20
REQUEST_EXCEPTION = 21
HTTP_EXCEPTION = 22
UNHANDLED_EXCEPTION = 23
NON_2XX_STATUS_CODE = 24

# Error Messages Templates
JSON_DECODE_EXCEPTION_MESSAGE = "An Error Occurred While Parsing the Response into JSON. Error: {error}"
REQUEST_EXCEPTION_MESSAGE = "HTTP Error Occurred, Error: {error}"
HTTP_EXCEPTION_MESSAGE = "An Error Occurred During the Request. Error: {error}"
UNHANDLED_EXCEPTION_MESSAGE = "Unhandled Exception: {error}"
NON_2XX_ERROR_MESSAGE = "API Returned non 2xx Status: {status_code}"

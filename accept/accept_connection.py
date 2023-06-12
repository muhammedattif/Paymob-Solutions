# Python Standard Library Imports
import json
from typing import Any, Dict, Union, Tuple

# Other Third Party Imports
import requests

from .config import ACCEPT_APIS_TIMEOUT_SECONDES, Credentials, URLsConfig
from .response_codes import (
    SUCCESS, 
    JSON_DECODE_ERROR, 
    UNHANDLED_EXCEPTION, 
    NON_2XX_STATUS_CODE, 
    REQUEST_EXCEPTION,
    HTTP_EXCEPTION,
    JSON_DECODE_EXCEPTION_MESSAGE, 
    REQUEST_EXCEPTION_MESSAGE, 
    HTTP_EXCEPTION_MESSAGE, 
    UNHANDLED_EXCEPTION_MESSAGE,
    NON_2XX_ERROR_MESSAGE,
)

class AcceptConnection:
    
    def __init__(self) -> None:
        """Initializing the Following:
        1- Requests Session
        2- Auth Token
        3- Set Headers
        """
        self.session = requests.Session()
        self.auth_token = self._get_auth_token()
        self.session.headers.update(self._get_headers())
        
    def _get_headers(self) -> Dict[str, Any]:
        """Initialize Header for Requests

        Returns:
            Dict[str, Any]: Initialized Header Dict
        """
        return {
            "Content-Type": "application/json",
            "Authorization": f"{self.auth_token}",
        }

    def _get_auth_token(self) -> str:
        """Retrieve an Auth Token

        Returns:
            str: Auth Token
        """

        request_body = {"api_key": Credentials.ACCEPT_API_KEY}

        _, data, _ = self.get(
            url=URLsConfig.AUTH_TOKEN_URL,
            json=request_body
        )

        # TODO: Validates APIs Return Data Option
        
        return data.get("token")
    
    def get(self, *args, **kwargs) -> Tuple[str, Dict[str, Any], Union[str, None]]:
        """Wrapper of requests.get method

        Args: 
            Same Args of requests.post/requests.get methods
            
        Returns:
            Tuple[str, Dict[str, Any], Union[str, None]]: Tuple containes the Following (Code, Data, Success/Error Message)
        """
        # TODO: The Following Logic will be Abstracted
        try:
            response = self.session.get(
                timeout=ACCEPT_APIS_TIMEOUT_SECONDES,
                *args, **kwargs
            )
            reponse_data = response.json()
        except json.JSONDecodeError as error:
            return JSON_DECODE_ERROR, None, JSON_DECODE_EXCEPTION_MESSAGE.format(error=error)
        except requests.exceptions.HTTPError as error:
            return HTTP_EXCEPTION, None, HTTP_EXCEPTION_MESSAGE.format(error=error)
        except requests.exceptions.RequestException as error:
            return REQUEST_EXCEPTION, None, REQUEST_EXCEPTION_MESSAGE.format(error=error)
        except Exception as error:
            return UNHANDLED_EXCEPTION, None, UNHANDLED_EXCEPTION_MESSAGE.format(error=error)

        if not response.ok:
            return NON_2XX_STATUS_CODE, None, NON_2XX_ERROR_MESSAGE.format(status_code=response.status_code)
        
        message = "API Successfully Called."
        return SUCCESS, reponse_data, message

    def post(self, *args, **kwargs) -> Tuple[str, Dict[str, Any], Union[str, None]]:
        """Wrapper of requests.get method

        Args: 
            Same Args of requests.post/requests.get methods
            
        Returns:
            Tuple[str, Dict[str, Any], Union[str, None]]: Tuple containes the Following (Code, Data, Success/Error Message)
        """
        # TODO: The Following Logic will be Abstracted
        try:
            response = self.session.post(
                timeout=ACCEPT_APIS_TIMEOUT_SECONDES,
                *args, **kwargs
            )
            reponse_data = response.json()
        except json.JSONDecodeError as error:
            return JSON_DECODE_ERROR, None, JSON_DECODE_EXCEPTION_MESSAGE.format(error=error)
        except requests.exceptions.HTTPError as error:
            return HTTP_EXCEPTION, None, HTTP_EXCEPTION_MESSAGE.format(error=error)
        except requests.exceptions.RequestException as error:
            return REQUEST_EXCEPTION, None, REQUEST_EXCEPTION_MESSAGE.format(error=error)
        except Exception as error:
            return UNHANDLED_EXCEPTION, None, UNHANDLED_EXCEPTION_MESSAGE.format(error=error)

        if not response.ok:
            return NON_2XX_STATUS_CODE, None, NON_2XX_ERROR_MESSAGE.format(status_code=response.status_code)
        
        message = "API Successfully Called."
        return SUCCESS, reponse_data, message

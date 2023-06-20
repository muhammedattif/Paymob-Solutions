# Python Standard Library Imports
import json
from typing import Any, Dict, Tuple, Union

# Other Third Party Imports
import requests

# First Party Imports
from paymob.data_classes import ResponseFeedBack

from .config import ACCEPT_APIS_TIMEOUT_SECONDES, Credentials, URLsConfig
from .response_codes import (
    HTTP_EXCEPTION,
    HTTP_EXCEPTION_MESSAGE,
    JSON_DECODE_EXCEPTION,
    JSON_DECODE_EXCEPTION_MESSAGE,
    REQUEST_EXCEPTION,
    REQUEST_EXCEPTION_MESSAGE,
    SUCCESS,
    UNHANDLED_EXCEPTION,
    UNHANDLED_EXCEPTION_MESSAGE,
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

    def _get_auth_token(self) -> Union[str, None]:
        """Retrieve an Auth Token

        Returns:
            Union[str, None]: Auth Token
        """

        request_body = {"api_key": Credentials.ACCEPT_API_KEY}

        code, data, _ = self.post(
            url=URLsConfig.AUTH_TOKEN,
            json=request_body,
        )

        # TODO: Validates APIs Return Data Option
        token = None
        if code == SUCCESS:
            token = data.get("token")
        return token

    def get(self, *args, **kwargs) -> Tuple[str, Dict[str, Any], ResponseFeedBack]:
        """Wrapper of requests.get method

        Args:
            Same Args of requests.post/requests.get methods

        Returns:
            Tuple[str, Dict[str, Any], ResponseFeedBack]: Tuple containes the Following (Code, Data, Success/Error Message)
        """
        # TODO: The Following Logic will be Abstracted
        reponse_data = None
        try:
            response = self.session.get(timeout=ACCEPT_APIS_TIMEOUT_SECONDES, *args, **kwargs)
            reponse_data = response.json()
            response.raise_for_status()
        except json.JSONDecodeError as error:
            reponse_feedback = ResponseFeedBack(
                message=JSON_DECODE_EXCEPTION_MESSAGE,
                data=error,
                status_code=response.status_code,
            )
            return JSON_DECODE_EXCEPTION, None, reponse_feedback
        except requests.exceptions.HTTPError as error:
            reponse_feedback = ResponseFeedBack(
                message=HTTP_EXCEPTION_MESSAGE,
                data=reponse_data,
                status_code=response.status_code,
            )
            return HTTP_EXCEPTION, reponse_data, reponse_feedback
        except requests.exceptions.RequestException as error:
            reponse_feedback = ResponseFeedBack(message=REQUEST_EXCEPTION_MESSAGE, data=error)
            return REQUEST_EXCEPTION, None, reponse_feedback
        except Exception as error:
            reponse_feedback = ResponseFeedBack(
                message=UNHANDLED_EXCEPTION_MESSAGE,
                data=error,
                status_code=response.status_code,
            )
            return UNHANDLED_EXCEPTION, None, reponse_feedback

        message = "API Successfully Called."
        reponse_feedback = ResponseFeedBack(message=message, status_code=response.status_code)
        return SUCCESS, reponse_data, reponse_feedback

    def post(self, *args, **kwargs) -> Tuple[str, Dict[str, Any], ResponseFeedBack]:
        """Wrapper of requests.get method

        Args:
            Same Args of requests.post/requests.get methods

        Returns:
            Tuple[str, Dict[str, Any], ResponseFeedBack]: Tuple containes the Following (Code, Data, Success/Error Message)
        """
        # TODO: The Following Logic will be Abstracted
        reponse_data = None
        try:
            response = self.session.post(timeout=ACCEPT_APIS_TIMEOUT_SECONDES, *args, **kwargs)
            reponse_data = response.json()
            response.raise_for_status()
        except json.JSONDecodeError as error:
            reponse_feedback = ResponseFeedBack(
                message=JSON_DECODE_EXCEPTION_MESSAGE,
                data=error,
                status_code=response.status_code,
            )
            return JSON_DECODE_EXCEPTION, None, reponse_feedback
        except requests.exceptions.HTTPError as error:
            reponse_feedback = ResponseFeedBack(
                message=HTTP_EXCEPTION_MESSAGE,
                data=reponse_data,
                status_code=response.status_code,
            )
            return HTTP_EXCEPTION, reponse_data, reponse_feedback
        except requests.exceptions.RequestException as error:
            reponse_feedback = ResponseFeedBack(message=REQUEST_EXCEPTION_MESSAGE, data=error)
            return REQUEST_EXCEPTION, None, reponse_feedback
        except Exception as error:
            reponse_feedback = ResponseFeedBack(
                message=UNHANDLED_EXCEPTION_MESSAGE,
                data=error,
                status_code=response.status_code,
            )
            return UNHANDLED_EXCEPTION, None, reponse_feedback

        message = "API Successfully Called."
        reponse_feedback = ResponseFeedBack(message=message, status_code=response.status_code)
        return SUCCESS, reponse_data, reponse_feedback

# Other Third Party Imports
from requests import HTTPError, JSONDecodeError


class ResponseFactory(object):
    def __init__(self, json_data, status_code, text=""):
        self.json_data = json_data
        self.status_code = status_code
        self.text = text
        self.content = ""

    @property
    def ok(self):
        return self.status_code < 400

    def raise_for_status(self):
        if self.status_code > 200:
            raise HTTPError("", "", 0)

    def json(self):
        if self.json_data is None:
            raise JSONDecodeError("", "", 0)
        return self.json_data

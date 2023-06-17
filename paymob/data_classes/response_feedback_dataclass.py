# Python Standard Library Imports
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class ResponseFeedBack:

    message: Optional[str]
    data: Any = None
    status_code: int = 500

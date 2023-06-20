# Python Standard Library Imports
from typing import Union

# Other Third Party Imports
from pydantic import BaseModel


class OrderItemDataClass(BaseModel):
    name: str
    amount_cents: Union[str, int]
    quantity: Union[str, int]
    description: str

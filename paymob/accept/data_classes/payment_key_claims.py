# Python Standard Library Imports
from typing import Union

# Other Third Party Imports
from pydantic import BaseModel

from .shipping_data import ShippingDataDataClass


class PaymentKeyClaimsDataClass(BaseModel):
    exp: Union[int, float]
    currency: str
    amount_cents: int
    user_id: int
    integration_id: int
    shipping_data: ShippingDataDataClass

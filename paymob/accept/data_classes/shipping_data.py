# Python Standard Library Imports
from typing import Optional

# Other Third Party Imports
from pydantic import BaseModel


class ShippingDataDataClass(BaseModel):
    id: Optional[int]
    order_id: Optional[int]
    order: Optional[int]

    first_name: str
    last_name: str
    country: str
    state: str
    city: str
    street: str
    building: str
    floor: str
    apartment: str
    postal_code: str
    phone_number: str
    extra_description: str
    shipping_method: str
    email: str

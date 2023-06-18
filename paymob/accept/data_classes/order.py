# Python Standard Library Imports
from datetime import datetime
from typing import List, Optional

# Other Third Party Imports
from pydantic import BaseModel

from .order_item import OrderItemDataClass
from .shipping_data import ShippingDataDataClass


class OrderDataClass(BaseModel):
    id: int
    created_at: datetime
    delivery_needed: bool
    amount_cents: int
    currency: str
    is_payment_locked: bool
    merchant_order_id: Optional[str] = None
    wallet_notification: Optional[str] = None
    paid_amount_cents: int
    items: List[OrderItemDataClass]
    shipping_data: ShippingDataDataClass

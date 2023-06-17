# Python Standard Library Imports
from dataclasses import dataclass
from datetime import datetime


@dataclass
class DeliveryStatus:
    order_id: int
    order_delivery_status: str
    merchant_id: int
    merchant_name: str
    updated_at: datetime


@dataclass
class DeliveryStatusCallback:
    type: str
    obj: DeliveryStatus


__all__ = ["DeliveryStatusCallback"]

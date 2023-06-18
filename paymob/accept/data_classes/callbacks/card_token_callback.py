# Python Standard Library Imports
from dataclasses import dataclass
from datetime import datetime


@dataclass
class CardToken:
    id: int
    order_id: int
    token: str
    masked_pan: str
    merchant_id: int
    card_subtype: str
    email: str
    created_at: datetime


@dataclass
class CardTokenCallback:
    type: str
    obj: CardToken


__all__ = ["CardTokenCallback"]

# Python Standard Library Imports
from datetime import datetime

# Other Third Party Imports
from pydantic import BaseModel

from .data import DataDataClass
from .order import OrderDataClass
from .source_data import SourceDataDataClass


class TransactionDataClass(BaseModel):
    id: int
    pending: bool
    amount_cents: int
    success: bool
    is_auth: bool
    is_capture: bool
    is_voided: bool
    is_refunded: bool
    is_standalone_payment: bool
    is_3d_secure: bool
    has_parent_transaction: bool
    integration_id: int
    profile_id: int
    order: OrderDataClass
    currency: str
    source_data: SourceDataDataClass
    data: DataDataClass
    transaction_processed_callback_responses: list
    error_occured: bool
    owner: int
    parent_transaction: bool
    created_at: datetime

# Python Standard Library Imports
from typing import Optional

# Other Third Party Imports
from pydantic import BaseModel


class DataDataClass(BaseModel):
    merchant_txn_ref: str
    card_num: Optional[str] = None
    avs_result_code: str
    merchant: str
    avs_acq_response_code: str
    transaction_no: str
    batch_no: str
    message: str
    txn_response_code: str
    txn_response_code: str
    card_type: str
    receipt_no: str
    created_at: str
    currency: str
    klass: str
    authorize_id: str
    amount: str
    acq_response_code: str
    command: str
    gateway_integration_pk: int

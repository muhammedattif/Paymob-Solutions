# Python Standard Library Imports
from datetime import datetime
from typing import List

# Other Third Party Imports
from pydantic import BaseModel


class MerchantDataClass(BaseModel):
    id: int
    phones: List[str]
    company_emails: List[str]
    created_at: datetime
    company_name: str
    country: str
    state: str
    city: str
    street: str
    postal_code: str

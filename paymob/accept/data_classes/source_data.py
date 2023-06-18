# Other Third Party Imports
from pydantic import BaseModel


class SourceDataDataClass(BaseModel):
    type: str
    sub_type: str
    pan: str

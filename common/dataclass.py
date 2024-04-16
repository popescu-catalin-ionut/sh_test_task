from pydantic import BaseModel
from typing import Dict


class Documentation(BaseModel):
    title: str
    description: str
    summary: str
    version: str
    terms_of_service: str
    contact: Dict[str, str]
    license_info: Dict[str, str]


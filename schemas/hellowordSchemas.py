from typing import Generic, TypeVar, List, Optional
from pydantic import BaseModel, Json


class respond(BaseModel):
    data: Optional[dict] = "Hellow Word"

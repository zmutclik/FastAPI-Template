
from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import Generic, TypeVar, List, Optional

DataT = TypeVar('DataT')


class ResponseMetadata(BaseModel):
    message: str
    code: int


class Response(GenericModel, Generic[DataT]):
    metadata: Optional[ResponseMetadata]
    response: Optional[DataT] = None


class Request(GenericModel, Generic[DataT]):
    request: Optional[DataT] = None

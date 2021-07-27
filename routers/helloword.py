from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import respondSchemas,hellowordSchemas
from ..database import get_db

router = APIRouter()


@router.get("/test/",
            response_model=respondSchemas.Response,
            tags=["TESTER"])
async def get_(db: Session = Depends(get_db)):
    metadata_ = respondSchemas.ResponseMetadata(message="OK", code=200)
    response = None

    return respondSchemas.Response[hellowordSchemas.respond](metadata=metadata_, response=response)
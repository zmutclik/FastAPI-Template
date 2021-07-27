from fastapi import Depends, FastAPI

from .routers import helloword

app = FastAPI(
    title="My Super Project",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="1.0.0",
)

app.include_router(helloword.router)

@app.get("")
async def root():
    return {"message": "Hello BOZ !"}

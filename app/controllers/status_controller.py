import http

from fastapi import APIRouter
from fastapi.responses import JSONResponse

# from data_adapter.db import db_engine

router = APIRouter(tags=["root"])


#  health check endpoints

@router.get("/", status_code=http.HTTPStatus.OK)
async def read_root() -> dict:
    return {"message": "Welcome to your blog!"}

@router.get("/status", status_code=http.HTTPStatus.OK)
async def status_check():
    return JSONResponse(status_code=http.HTTPStatus.OK, content={"status": "OK"})


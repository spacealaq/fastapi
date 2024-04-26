import http

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.post import Items

router = APIRouter(tags=["posts"])


@router.get("/posts", response_model=list[Items])
async def read_items() -> list[Items]:
    return [
        Items(name="Portal Gun", price=42.0),
        Items(name="Plumbus", price=32.0),
    ]


@router.get("/posts/{id}", tags=["posts"])
async def get_single_post(id: int) -> dict:
    if id > len(Items):
        return {
            "error": "No such post with the supplied ID."
        }

    for post in Items:
        if post["id"] == id:
            return {
                "data": post
            }
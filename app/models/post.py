from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, validator, HttpUrl, constr

from app.models.base import DBBaseModel


class Items(BaseModel):
    nombre: str
    email: str
    nacionalidad: str | None = None
    sitio_turitico: str
    presupuesto: str | None = None
    aerolinea: str | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nombre": "Jhon Doe",
                    "email": "jhondoe@gmail.com",
                    "nacionalidad": "Estados Unidos",
                    "sitio_turitico": "Sanatamarta",
                    "presupuesto": "5000 USD",
                    "aerolinea": "Avianca",
                }
            ]
        }
    }


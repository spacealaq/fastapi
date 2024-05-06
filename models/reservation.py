from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, validator, HttpUrl, constr

from models.base import DBBaseModel



class ReservationBaseModel(BaseModel):
    nombre: constr(min_length=1, max_length=255, strip_whitespace=True)
    email: constr(min_length=1, max_length=255, strip_whitespace=True)
    nacionalidad: constr(min_length=1, max_length=255, strip_whitespace=True)
    sitio_turistico: constr(min_length=1, max_length=255, strip_whitespace=True)
    presupuesto: constr(min_length=1, max_length=255, strip_whitespace=True)
    aerolinea: constr(min_length=1, max_length=255, strip_whitespace=True)


class ReservationInsertModel(ReservationBaseModel):
    """Item model for insert"""

    def build_db_model(self):
        from data_adapter.inventory import Item
        return Item(**self.dict())


class ReservationResponseModel(ReservationInsertModel):
    """Item response model"""
    uuid: UUID


class ReservationModel(ReservationInsertModel, DBBaseModel):
    """Base DB model for item"""
    pass

    class Config:
        orm_mode = True

    def build_response_model(self) -> ReservationResponseModel:
        return ReservationResponseModel(**self.dict())

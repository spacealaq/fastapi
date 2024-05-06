from typing import List

from sqlalchemy import Column, String, Float, INTEGER
from sqlalchemy.orm import Session

from data_adapter.db import CartDBBase, DBBase
from models.reservation import ReservationModel


class Reservation(DBBase, CartDBBase):
    __tablename__ = 'reservation'

    nombre = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    nacionalidad = Column(String(255), nullable=False)
    sitio_turistico = Column(String(255), nullable=False)
    presupuesto = Column(String(255), nullable=False)
    aerolinea = Column(String(255), nullable=False)

    def __to_model(self) -> ReservationModel:
        """converts db orm object to pydantic model"""
        return ReservationModel.from_orm(self)

    @classmethod
    def create_item(cls, item) -> ReservationModel:
        from controller.context_manager import get_db_session
        db: Session = get_db_session()
        db.add(item)
        db.flush()
        return item.__to_model()

    @classmethod
    def get_by_id(cls, id) -> ReservationModel:
        item = super().get_by_id(id)
        return item.__to_model() if item else None

    @classmethod
    def get_by_uuid(cls, uuid) -> ReservationModel:
        item = super().get_by_uuid(uuid)
        return item.__to_model() if item else None

    @classmethod
    def get_all_items(cls) -> List[ReservationModel]:
        from controller.context_manager import get_db_session
        db = get_db_session()
        items = db.query(cls).filter(cls.is_deleted.is_(False)).all()
        return [item.__to_model() for item in items]

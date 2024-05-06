import http
from typing import List

from controller.context_manager import context_log_meta
from data_adapter.reservation import Reservation
from logger import logger
from models.base import GenericResponseModel
from models.reservation import ReservationModel, ReservationInsertModel


class ReservationService:
    ERROR_NO_RESERVATION = "No Reservation found"
    ERROR_RESERVATION_ALREADY = "Reservation already exist , try updating existing Reservation"

    @staticmethod
    def get_all_items() -> GenericResponseModel:
        """
        Get all items from reservation
        :return: GenericResponseModel
        """
        items: List[ReservationModel] = Reservation.get_all_items()
        if not items:
            logger.error(extra=context_log_meta.get(), msg="No items found in inventory")
            return GenericResponseModel(status_code=http.HTTPStatus.NOT_FOUND,
                                        error=ReservationService.ERROR_NO_RESERVATION, data=[])
        return GenericResponseModel(status_code=http.HTTPStatus.OK,
                                    data=[item.build_response_model() for item in items])

    @staticmethod
    def add_item(item: ReservationInsertModel) -> GenericResponseModel:
        """
        Add Reservation
        :param item: ReservationInsertModel
        :return: GenericResponseModel
        """
        item = Reservation.create_item(item.build_db_model())
        return GenericResponseModel(status_code=http.HTTPStatus.CREATED, data=item.build_response_model())

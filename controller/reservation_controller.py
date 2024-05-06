import http

from fastapi import APIRouter, Depends

from logger import logger
from controller.context_manager import build_request_context
from models.base import GenericResponseModel
from models.reservation import ReservationInsertModel
from server.auth import rbac_access_checker, RBACResource, RBACAccessType
from service.reservation_service import ReservationService
from utils.helper import build_api_response

reservation_router = APIRouter(prefix="/v1/reservation", tags=["reservation"])


@reservation_router.get("", status_code=http.HTTPStatus.OK, response_model=GenericResponseModel)
# @rbac_access_checker(resource=RBACResource.reservation, rbac_access_type=RBACAccessType.read)
async def get_items(_=Depends(build_request_context)):
    """
    Get all reservations
    :param _: build_request_context dependency injection handles the request context
    :return: GenericResponseModel
    """
    response = ReservationService.get_all_items()
    logger.error("response")
    logger.error(response)
    return response


@reservation_router.post("", status_code=http.HTTPStatus.CREATED, response_model=GenericResponseModel)
# @rbac_access_checker(resource=RBACResource.reservation, rbac_access_type=RBACAccessType.write)
async def add_item(item: ReservationInsertModel, _=Depends(build_request_context)):
    """
    Add reservation
    :param _: build_request_context dependency injection handles the request context
    :param item: item details to add
    :return:
    """
    response = ReservationService.add_item(item=item)
    return build_api_response(response)

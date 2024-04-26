import http
import json

import uvicorn
from fastapi import FastAPI, Depends, Request
from pydantic import ValidationError
# from sqlalchemy.exc import ProgrammingError, DataError, IntegrityError

from app.controllers import status_controller,post_controller
# from controller.context_manager import context_log_meta, context_set_db_session_rollback
# from logger import logger
# from models.base import GenericResponseModel
# from routes.auth import authenticate_token
# from utils.exceptions import AppException
# from utils.helper import build_api_response

# https://github.com/KetanSomvanshi/cart-service/blob/master/config/settings.py
# https://testdriven.io/blog/fastapi-jwt-auth/

app = FastAPI()

#  register routers here and add dependency on authenticate_token if token based authentication is required
app.include_router(status_controller.router)
app.include_router(post_controller.router)
# user creation and login apis should be open
# app.include_router(user_controller.user_router)
#  token based authentication apis should have dependency on authenticate_token
# app.include_router(customer_controller.customer_router, dependencies=[Depends(authenticate_token)])
# app.include_router(inventory_controller.inventory_router, dependencies=[Depends(authenticate_token)])
# app.include_router(cart_controller.cart_router, dependencies=[Depends(authenticate_token)])

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8081, reload=True)
from typing import Annotated
from fastapi import APIRouter, Depends
from services.user_employees import user_employees_service
from schemas import IdResponseSchema
from schemas.user_employees import CreateUserEmployeeSchema
from utils.locale_handler import LocaleHandler

router = APIRouter(
    prefix="/user-employees",
    tags=["User Employees (employees of travel expert)"],
)


@router.post("/{locale}", response_model=IdResponseSchema)
async def create_user_employee(
    locale: Annotated[LocaleHandler, Depends()],
    employee_data: CreateUserEmployeeSchema,
):
    """
    user_id is the id of the travel expert

    - returns the id of new user(employee)
    """
    return await user_employees_service.create_user_employee(employee_data, locale)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_user_employee(
    user_id: int,
    employee_id: int,
):
    """
    user_id is the id of the travel expert

    - returns the id of user (travel expert) and employee association
    """
    return await user_employees_service.delete_user_employee(user_id, employee_id)

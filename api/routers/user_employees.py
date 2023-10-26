from typing import Annotated
from fastapi import APIRouter, Depends
from services.user_employees import user_employees_service
from schemas import IdResponseSchema
from repositories import Page
from schemas.user_employees import CreateEmployeeSchema, EmployeeSchema
from utils.locale_handler import LocaleHandler
from database import UOWDependency

router = APIRouter(
    prefix="/user-employees",
    tags=["User Employees (employees of travel expert)"],
)


@router.post("/{locale}", response_model=IdResponseSchema)
async def create_user_employee(
    uow: UOWDependency,
    locale: Annotated[LocaleHandler, Depends()],
    employee_data: CreateEmployeeSchema,
):
    """
    user_id is the id of the travel expert

    - returns the id of new user(employee)
    """
    return await user_employees_service.create_user_employee(uow, employee_data, locale)

@router.get('/{travel_expert_id}', response_model=Page[EmployeeSchema])
async def get_employees_of_travel_expert(
    uow: UOWDependency,
    travel_expert_id: int,
):
    return await user_employees_service.get_employees_of_travel_expert(uow, travel_expert_id)


@router.delete("/{id}", response_model=IdResponseSchema)
async def delete_user_employee(
    uow: UOWDependency,
    id: int,
):
    """
    - params: id of the association of travel expert and employee
    """
    return await user_employees_service.delete_user_employee(uow, id)

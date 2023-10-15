from schemas.user_employees import (
    CreateUserEmployeeSchema,
    CreateUserEmployeeAssociationSchema,
)
from database import UnitOfWork, email_sender
from utils.exceptions import CustomExceptions
import models
from utils.locale_handler import LocaleHandler
from security.password import PasswordHandler


class UserEmployeesService:
    async def send_email_message_to_welcome_employee(
        self, employee: models.User, locale: LocaleHandler, travel_expert: models.User
    ):
        await email_sender.send_welcome_email_message(
            user=employee,
            locale=locale.get_language,
            subject="Welcome to market place MINZIFATRAVEL",
            template_name="new_employee.html",
            travel_expert=travel_expert,
        )

    async def create_user_employee(
        self,
        uow: UnitOfWork,
        employee_data: CreateUserEmployeeSchema,
        locale: LocaleHandler,
    ) -> models.User:
        employee_dict = employee_data.model_dump()
        hashed_password = PasswordHandler.hash(employee_data.password)

        employee_dict["password"] = hashed_password
        async with uow:
            existing_user = await uow.users.get_by_email(employee_data.email)
            if existing_user:
                raise CustomExceptions.conflict("Already exists user with this email")

            employee: models.User = await uow.users.create(employee_dict)
            await uow.user_employees.create(
                CreateUserEmployeeAssociationSchema(
                    user_id=employee_data.user_id, employee_id=employee.id
                ).model_dump()
            )
            await uow.commit()
            await self.send_email_message_to_welcome_employee(
                employee=employee, locale=locale, travel_expert=employee.travel_expert
            )
            return employee

    async def delete_user_employee(
        self,
        uow: UnitOfWork,
        user_id: int,
        employee_id: int,
    ) -> models.UserEmployee:
        async with uow:
            deleted_user_employee = await uow.user_employees.delete_by(
                user_id=user_id, employee_id=employee_id
            )
            await uow.commit()
            return deleted_user_employee


user_employees_service = UserEmployeesService()

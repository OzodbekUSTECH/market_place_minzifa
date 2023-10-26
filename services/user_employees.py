from schemas.user_employees import (
    CreateEmployeeSchema,
    CreateEmployeeAssociationSchema,
)
from database import UnitOfWork, email_sender
from utils.exceptions import CustomExceptions
import models
from utils.locale_handler import LocaleHandler
from security.password import PasswordHandler
from repositories import paginate


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
        employee_data: CreateEmployeeSchema,
        locale: LocaleHandler,
    ) -> models.UserEmployee:
        employee_dict = employee_data.model_dump()
        hashed_password = PasswordHandler.hash(employee_data.password)

        employee_dict["password"] = hashed_password
        async with uow:
            existing_user = await uow.users.get_by_email(employee_data.email)
            if existing_user:
                raise CustomExceptions.conflict("Already exists user with this email")

            employee: models.User = await uow.users.create(employee_dict)
            employee_assosiaction = await uow.user_employees.create(
                CreateEmployeeAssociationSchema(
                    travel_expert_id=employee_data.travel_expert_id, employee_id=employee.id
                ).model_dump()
            )
            await uow.commit()
            travel_expert: models.User = await uow.users.get_by_id(employee_data.travel_expert_id)
            await self.send_email_message_to_welcome_employee(
                employee=employee, locale=locale, travel_expert=travel_expert
            )
            return employee_assosiaction
        
    async def get_employees_of_travel_expert(self, uow: UnitOfWork, travel_expert_id: int) -> list[models.User]:
        async with uow:
            return paginate(await uow.user_employees.get_all_by(travel_expert_id=travel_expert_id))


    async def delete_user_employee(
        self,
        uow: UnitOfWork,
        id: int,
    ) -> models.UserEmployee:
        async with uow:
            employee_association: models.UserEmployee = await uow.user_employees.get_by_id(id)
            await uow.user_employees.delete(employee_association.id)
            await uow.commit()
            return employee_association


user_employees_service = UserEmployeesService()

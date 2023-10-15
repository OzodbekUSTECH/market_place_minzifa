from schemas.roles import CreateRoleSchema, UpdateRoleSchema
from database import UnitOfWork
from models import Role


class RolesService:
    async def create_role(self, uow: UnitOfWork, role_data: CreateRoleSchema) -> Role:
        role_dict = role_data.model_dump()
        async with uow:
            role = await uow.roles.create(role_dict)
            await uow.commit()
            return role

    async def get_all_roles(self, uow: UnitOfWork) -> list[Role]:
        async with uow:
            return await uow.roles.get_all()

    async def get_role_by_id(self, uow: UnitOfWork, id: int) -> Role:
        async with uow:
            return await uow.roles.get_by_id(id)

    async def update_role(
        self, uow: UnitOfWork, id: int, role_data: UpdateRoleSchema
    ) -> Role:
        role_dict = role_data.model_dump()
        async with uow:
            role = await uow.roles.update(id, role_dict)
            await uow.commit()
            return role

    async def delete_role(self, uow: UnitOfWork, id: int) -> Role:
        async with uow:
            role = await uow.roles.delete(id)
            await uow.commit()
            return role


roles_service = RolesService()

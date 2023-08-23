from repositories.roles import RolesRepository
from repositories.base import Pagination
from fastapi import HTTPException, status
from schemas.roles import RoleSchema, CreateRoleSchema, UpdateRoleSchema
from repositories.unitofwork import UnitOfWork

class RolesService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_all_roles(self, pagination: Pagination) -> list[RoleSchema]:
        async with self.uow:
            list_of_roles = await self.uow.roles.get_all(pagination)
            await self.uow.commit()
            return list_of_roles
    
    async def get_role_by_id(self, role_id: int) -> RoleSchema:
        async with self.uow:
            role = await self.uow.roles.get_by_id(role_id)
            await self.uow.commit()
            return role
    
    async def create_role(self, role_data: CreateRoleSchema) -> RoleSchema:
        role_dict = role_data.model_dump()
        async with self.uow:

            existing_role = await self.uow.roles.has_already_role_name(role_data)
            if existing_role:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Role with this name already exists")
            
            created_role = await self.uow.roles.create(role_dict)
            await self.uow.commit()
            return created_role

    async def update_role(self, role_id: int, role_data: UpdateRoleSchema) -> RoleSchema:
        role_dict = role_data.model_dump()
        async with self.uow:

            existing_role = await self.uow.roles.has_already_role_name(role_data)
            if existing_role:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Role with this name already exists")
            created_role = await self.uow.roles.update(role_id, role_dict)
            await self.uow.commit()
            return created_role
    
    async def delete_role(self, role_id: int) -> RoleSchema:
        async with self.uow:
            deleted_role = await self.uow.roles.delete(role_id)
            await self.uow.commit()
            return deleted_role
    
    
    #extends
    async def get_role_permissions(self, role_id: int):
        async with self.uow:
            role = await self.uow.roles.get_by_id(role_id)
            await self.uow.commit()
            return [rp.permission for rp in role.role_permissions]

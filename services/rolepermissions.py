from repositories.rolepermissions import RolePermissionsRepository
from repositories.base import Pagination
from fastapi import HTTPException, status
from schemas.rolepermissions import RolePermissionsSchema, CreateRolePermissionsSchema, DeleteRolePermissionsSchema
from repositories.unitofwork import UnitOfWork

class RolePermissionsService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def give_permission_for_role(self, role_permission_data: CreateRolePermissionsSchema) -> RolePermissionsSchema:
        role_permission_dict = role_permission_data.model_dump()
        async with self.uow:
            role_permission = await self.uow.role_permissions.has_role_permission(role_permission_data)
            if role_permission:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This permission already exists")
            created_role_permission = await self.uow.role_permissions.create(role_permission_dict)
            await self.uow.commit()
            return created_role_permission
        

    
    async def delete_permission_for_role(self, role_permission_data: DeleteRolePermissionsSchema) -> RolePermissionsSchema:
        async with self.uow:
            deleted_role_permission = await self.uow.role_permissions.delete_permission_for_role(role_permission_data)
            await self.uow.commit()
            return deleted_role_permission
        
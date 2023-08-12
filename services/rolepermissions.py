from repositories.rolepermissions import RolePermissionsRepository
from repositories.base import Pagination
from fastapi import HTTPException, status
from schemas.rolepermissions import RolePermissionsSchema, CreateRolePermissionsSchema, DeleteRolePermissionsSchema

class RolePermissionsService:
    def __init__(self, roleperms_repo: RolePermissionsRepository):
        self.roleperms_repo: RolePermissionsRepository = roleperms_repo

    async def give_permission_for_role(self, role_permission_data: CreateRolePermissionsSchema) -> RolePermissionsSchema:
        role_permission = await self.roleperms_repo.has_role_permission(role_permission_data)
        if role_permission:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This permission already exists")
        return await self.roleperms_repo.create(role_permission_data.model_dump())
        

    
    async def delete_permission_for_role(self, role_permission_data: DeleteRolePermissionsSchema) -> RolePermissionsSchema:
        return await self.roleperms_repo.delete_permission_for_role(role_permission_data)
        
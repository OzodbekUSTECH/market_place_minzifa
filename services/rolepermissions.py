from repositories import Pagination
from schemas.rolepermissions import CreateRolePermissionsSchema, DeleteRolePermissionsSchema, UpdateRolePermissionsSchema
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
from models import RolePermission
class RolePermissionsService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_permission_for_role(self, role_permission_data: CreateRolePermissionsSchema) -> RolePermission:
        role_permission_dict = role_permission_data.model_dump()
        async with self.uow:
            role_permission = await self.uow.role_permissions.has_role_permission(role_permission_data)
            if role_permission:
                raise CustomExceptions.conflict("This permission already exists")
            created_role_permission = await self.uow.role_permissions.create(role_permission_dict)
            
            return created_role_permission
        
    async def get_list_of_role_permissions(self, pagination: Pagination) -> list[RolePermission]:
        async with self.uow:
            return await self.uow.role_permissions.get_all(pagination)

    async def get_list_of_permissions_of_role(self, role_id: int) -> list[RolePermission]:
        async with self.uow:
            role = await self.uow.roles.get_by_id(role_id)
            return role.role_permissions

    async def get_role_permission_by_id(self, id: int) -> RolePermission:
        async with self.uow:
            return await self.uow.role_permissions.get_by_id(id)
        
    async def delete_role_permission(self, id: int) -> RolePermission:
        async with self.uow:
            return await self.uow.role_permissions.delete(id)
        
    async def give_permission_for_role(self, role_permission_data: CreateRolePermissionsSchema) -> RolePermission:
        role_permission_dict = role_permission_data.model_dump()
        async with self.uow:
            role_permission = await self.uow.role_permissions.has_role_permission(role_permission_data)
            if role_permission:
                raise CustomExceptions.conflict("This permission already exists")
            created_role_permission = await self.uow.role_permissions.create(role_permission_dict)
            
            return created_role_permission
        

    
    async def delete_permission_for_role(self, role_permission_data: DeleteRolePermissionsSchema) -> RolePermission:
        async with self.uow:
            deleted_role_permission = await self.uow.role_permissions.delete_permission_for_role(role_permission_data)
            
            return deleted_role_permission
        
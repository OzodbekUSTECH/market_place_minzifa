from repositories import Pagination
from schemas.permissions import CreatePermissionSchema, UpdatePermissionSchema
from database.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
from security.permissionhandler import PermissionHandler
from models import Permission
class PermissionsService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_all_permissions(self, pagination: Pagination) -> list[Permission]:
        async with self.uow:
            all_permissions = await self.uow.permissions.get_all(pagination)
            
            return all_permissions
        
    async def get_permission_by_id(self, permission_id: int) -> Permission:
        async with self.uow:
            permission = await self.uow.permissions.get_by_id(permission_id)
            
            return permission 
    
    async def create_permission(self, permission_data: CreatePermissionSchema) -> Permission:

        async with self.uow:

            permission = await self.uow.permissions.get_by_endpoint(permission_data.endpoint)
            if permission:
                raise CustomExceptions.conflict("Such endpoint already has been registered")
            created_permission = await self.uow.permissions.create(permission_data.model_dump())
            
            return created_permission
    
    async def update_permission(self, permission_id: int, permission_data: UpdatePermissionSchema) -> Permission:
        role_dict = permission_data.model_dump()
        async with self.uow:
            updated_permission = await self.uow.permissions.update(permission_id, role_dict)
            
            return updated_permission
        
    
    async def delete_permission(self, permission_id: int) -> Permission:
        async with self.uow:
            deleted_permission = await self.uow.permissions.delete(permission_id)
            
            return deleted_permission
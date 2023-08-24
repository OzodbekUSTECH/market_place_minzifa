from repositories.permissions import PermissionsRepository
from repositories.base import Pagination
from fastapi import HTTPException, status
from schemas.permissions import PermissionSchema, CreatePermissionSchema, UpdatePermissionSchema
from repositories.unitofwork import UnitOfWork
from utils.exceptions import CustomExceptions
from security.permissionhandler import PermissionHandler
class PermissionsService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_all_permissions(self, pagination: Pagination) -> list[PermissionSchema]:
        async with self.uow:
            all_permissions = await self.uow.permissions.get_all(pagination)
            await self.uow.commit()
            return all_permissions
        
    async def get_permission_by_id(self, permission_id: int) -> PermissionSchema:
        async with self.uow:
            permission = await self.uow.permissions.get_by_id(permission_id)
            await self.uow.commit()
            return permission 
    
    async def create_permission(self, permission_data: CreatePermissionSchema) -> PermissionSchema:
        await PermissionHandler.is_allowed_permission_endpoint(permission_data.endpoint)

        async with self.uow:

            permission = await self.uow.permissions.get_by_endpoint(permission_data.endpoint)
            if permission:
                raise CustomExceptions.conflict("Such endpoint already has been registered")
            created_permission = await self.uow.permissions.create(permission_data.model_dump())
            await self.uow.commit()
            return created_permission
    
    async def update_permission(self, permission_id: int, permission_data: UpdatePermissionSchema) -> PermissionSchema:
        await PermissionHandler.is_allowed_permission_endpoint(permission_data.endpoint)
        role_dict = permission_data.model_dump()
        async with self.uow:
            updated_permission = await self.uow.permissions.update(permission_id, role_dict)
            await self.uow.commit()
            return updated_permission
        
    
    async def delete_permission(self, permission_id: int) -> PermissionSchema:
        async with self.uow:
            deleted_permission = await self.uow.permissions.delete(permission_id)
            await self.uow.commit()
            return deleted_permission
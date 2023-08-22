from repositories.permissions import PermissionsRepository
from repositories.base import Pagination
from fastapi import HTTPException, status
from schemas.permissions import PermissionSchema, CreatePermissionSchema, UpdatePermissionSchema

class PermissionsService:
    def __init__(self, perms_repo: PermissionsRepository):
        self.perms_repo: PermissionsRepository = perms_repo

    async def get_all_permissions(self, pagination: Pagination) -> list[PermissionSchema]:
        return await self.perms_repo.get_all(pagination)
        
    async def get_permission_by_id(self, permission_id: int) -> PermissionSchema:
        return await self.perms_repo.get_by_id(permission_id)
    
    async def create_permission(self, permission_data: CreatePermissionSchema) -> PermissionSchema:
        permission = await self.perms_repo.get_by_endpoint(permission_data.endpoint)
        if permission:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Such endpoint already has been registered")
        return await self.perms_repo.create(permission_data.model_dump())
    
    async def update_permission(self, permission_id: int, permission_data: UpdatePermissionSchema) -> PermissionSchema:
        role_dict = permission_data.model_dump()
        return await self.perms_repo.update(permission_id, permission_data)
    
    async def delete_permission(self, permission_id: int) -> PermissionSchema:
        return await self.perms_repo.delete(permission_id)
from typing import Annotated
from fastapi import APIRouter, Depends
from services.rolepermissions import RolePermissionsService
from utils.dependency import get_rolepermissions, get_current_user
from repositories.base import Pagination
from schemas.rolepermissions import RolePermissionsSchema, CreateRolePermissionsSchema, DeleteRolePermissionsSchema
from models import User
from security.permissionhandler import PermissionHandler, Permissions
router = APIRouter(
    prefix="/rolepermissions",
    tags=["Role and Permission connection"],
)



@router.post('', name='Give permission for a role', response_model=RolePermissionsSchema)
async def give_permission_data_for_role(
    role_permission_data: CreateRolePermissionsSchema,
    roleperms_service: Annotated[RolePermissionsService, Depends(get_rolepermissions)],
    current_user: Annotated[User, Depends(get_current_user)]
) -> RolePermissionsSchema:
    
    await PermissionHandler.has_permission(
        required_permission=Permissions.CONTROL_ROLES_AND_PERMISSIONS.value, 
        current_user=current_user
    )

    return await roleperms_service.give_permission_for_role(role_permission_data)


@router.delete('', name='Give permission for a role', response_model=RolePermissionsSchema)
async def give_permission_data_for_role(
    role_permission_data: DeleteRolePermissionsSchema,
    roleperms_service: Annotated[RolePermissionsService, Depends(get_rolepermissions)],
    current_user: Annotated[User, Depends(get_current_user)]
) -> RolePermissionsSchema:
    
    await PermissionHandler.has_permission(
        required_permission=Permissions.CONTROL_ROLES_AND_PERMISSIONS.value,
        current_user=current_user
    )

    return await roleperms_service.delete_permission_for_role(role_permission_data)


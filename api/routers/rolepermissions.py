from typing import Annotated
from fastapi import APIRouter, Depends
from services.rolepermissions import RolePermissionsService
from utils.dependency import get_rolepermissions, get_current_user
from repositories.base import Pagination
from schemas.rolepermissions import RolePermissionsSchema, CreateRolePermissionsSchema, DeleteRolePermissionsSchema, UpdateRolePermissionsSchema
from models import User
from security.permissionhandler import PermissionHandler, Permissions
router = APIRouter(
    prefix="/role_permissions",
    tags=["Role and Permission connection"],
)



# @router.post('', name='Give permission for a role', response_model=RolePermissionsSchema)
# async def give_permission_data_for_role(
#     role_permission_data: CreateRolePermissionsSchema,
#     roleperms_service: Annotated[RolePermissionsService, Depends(get_rolepermissions)],
#     # current_user: Annotated[User, Depends(get_current_user)]
# ) -> RolePermissionsSchema:
    
#     # await PermissionHandler.has_permission(
#     #     required_permission=Permissions.CONTROL_ROLES_AND_PERMISSIONS.value, 
#     #     current_user=current_user
#     # )

#     return await roleperms_service.give_permission_for_role(role_permission_data)


# @router.delete('', name='Give permission for a role', response_model=RolePermissionsSchema)
# async def give_permission_data_for_role(
#     role_permission_data: DeleteRolePermissionsSchema,
#     roleperms_service: Annotated[RolePermissionsService, Depends(get_rolepermissions)],
#     # current_user: Annotated[User, Depends(get_current_user)]
# ) -> RolePermissionsSchema:
    
#     # await PermissionHandler.has_permission(
#     #     required_permission=Permissions.CONTROL_ROLES_AND_PERMISSIONS.value,
#     #     current_user=current_user
#     # )

#     return await roleperms_service.delete_permission_for_role(role_permission_data)


@router.post('', response_model=RolePermissionsSchema)
async def create_permission_for_role(
    role_permission_data: CreateRolePermissionsSchema,
    roleperms_service: Annotated[RolePermissionsService, Depends(get_rolepermissions)],
):
    return await roleperms_service.create_permission_for_role(role_permission_data)

@router.get('', response_model=list[RolePermissionsSchema])
async def get_list_of_roles_permissions(
    pagination: Annotated[Pagination, Depends()],
    roleperms_service: Annotated[RolePermissionsService, Depends(get_rolepermissions)]
):
    return await roleperms_service.get_list_of_role_permissions(pagination)

@router.get('/{id}', response_model=RolePermissionsSchema)
async def get_role_permission_by_id(
    id: int,
    roleperms_service: Annotated[RolePermissionsService, Depends(get_rolepermissions)]
):
    return await roleperms_service.get_role_permission_by_id(id)

@router.get('/role/{role_id}', response_model=list[RolePermissionsSchema])
async def get_permissions_of_role(
    role_id: int,
    roleperms_service: Annotated[RolePermissionsService, Depends(get_rolepermissions)]
):
    return await roleperms_service.get_list_of_permissions_of_role(role_id)

@router.delete('/{id}', response_model=RolePermissionsSchema)
async def delete_role_permission(
    id: int,
    roleperms_service: Annotated[RolePermissionsService, Depends(get_rolepermissions)]
):
    return await roleperms_service.delete_role_permission(id)
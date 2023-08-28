from typing import Annotated
from fastapi import APIRouter, Depends
from services import RolesService
from utils.dependency import get_rolesservices, get_current_user
from repositories.base import Pagination
from schemas.roles import RoleSchema, CreateRoleSchema, UpdateRoleSchema, RolePermissionsSchema
from models import User
from security.permissionhandler import PermissionHandler, Permissions

router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)


@router.get('', name="get list of roles", response_model=list[RoleSchema])
async def get_list_of_roles(
    pagination: Annotated[Pagination, Depends()],
    roles_service: Annotated[RolesService, Depends(get_rolesservices)]
) -> list[RoleSchema]:
    return await roles_service.get_all_roles(pagination)

@router.get('/{id}/permissions', name="get all permissions of role", response_model=list[RolePermissionsSchema])
async def get_permissions(
    id: int,
    roles_service: Annotated[RolesService, Depends(get_rolesservices)]
):  
    return await roles_service.get_role_permissions(id)



@router.get('/{id}', name="get role by ID", response_model=RoleSchema)
async def get_role_data_by_id(
    id: int,
    roles_service: Annotated[RolesService, Depends(get_rolesservices)]
) -> RoleSchema:
    return await roles_service.get_role_by_id(id)

@router.post('', name="Create Role", response_model=RoleSchema)
async def create_role_data(
    role_data: CreateRoleSchema,
    roles_service: Annotated[RolesService, Depends(get_rolesservices)],
    current_user: Annotated[User, Depends(get_current_user)]
) -> RoleSchema:
    
    await PermissionHandler.has_permission(
        required_permission=Permissions.CONTROL_ROLES_AND_PERMISSIONS.value,
        current_user=current_user
    )
    return await roles_service.create_role(role_data)

@router.put('/{id}', name="Update Role", response_model=RoleSchema)
async def update_role_data(
    id: int,
    role_data: UpdateRoleSchema,
    roles_service: Annotated[RolesService, Depends(get_rolesservices)],
    current_user: Annotated[User, Depends(get_current_user)]
) -> RoleSchema:
    await PermissionHandler.has_permission(
        required_permission=Permissions.CONTROL_ROLES_AND_PERMISSIONS.value,
        current_user=current_user
    )
    return await roles_service.update_role(id, role_data)


@router.delete('/{id}', name="Create Role", response_model=RoleSchema)
async def delete_role_data(
    id: int,
    roles_service: Annotated[RolesService, Depends(get_rolesservices)],
    current_user: Annotated[User, Depends(get_current_user)]
) -> RoleSchema:
    await PermissionHandler.has_permission(
        required_permission=Permissions.CONTROL_ROLES_AND_PERMISSIONS.value,
        current_user=current_user
    )
    return await roles_service.delete_role(id)
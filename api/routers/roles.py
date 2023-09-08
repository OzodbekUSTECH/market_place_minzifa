from typing import Annotated
from fastapi import APIRouter, Depends
from services import RolesService
from utils.dependency import get_rolesservices, get_current_user
from repositories.base import Pagination
from schemas.roles import RoleSchema, CreateRoleSchema, UpdateRoleSchema, RolePermissionsSchema
from schemas.rolepermissions import RolePermissionsSchema
from models import User
from security.permissionhandler import PermissionHandler, Permissions
from utils.locale_handler import LocaleHandler

router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)


@router.get('/{locale}', name="get list of roles", response_model=list[RoleSchema])
async def get_list_of_roles(
    locale: Annotated[LocaleHandler, Depends()],
    pagination: Annotated[Pagination, Depends()],
    roles_service: Annotated[RolesService, Depends(get_rolesservices)]
) -> list[RoleSchema]:
    return await roles_service.get_all_roles(pagination, locale)


@router.get('/{locale}/{id}', name="get role by ID", response_model=RoleSchema)
async def get_role_data_by_id(
    locale: Annotated[LocaleHandler, Depends()],
    id: int,
    roles_service: Annotated[RolesService, Depends(get_rolesservices)]
) -> RoleSchema:
    return await roles_service.get_role_by_id(id, locale)

@router.post('',  response_model=RoleSchema)
async def create_role(
    role_data: CreateRoleSchema,
    roles_service: Annotated[RolesService, Depends(get_rolesservices)],
    # current_user: Annotated[User, Depends(get_current_user)]
) -> RoleSchema:
    
    # await PermissionHandler.has_permission(
    #     required_permission=Permissions.CONTROL_ROLES_AND_PERMISSIONS.value,
    #     current_user=current_user
    # )
    return await roles_service.create_role(role_data)

@router.put('/{id}',  response_model=RoleSchema)
async def update_role(
    id: int,
    role_data: UpdateRoleSchema,
    roles_service: Annotated[RolesService, Depends(get_rolesservices)],
    # current_user: Annotated[User, Depends(get_current_user)]
) -> RoleSchema:
    # await PermissionHandler.has_permission(
    #     required_permission=Permissions.CONTROL_ROLES_AND_PERMISSIONS.value,
    #     current_user=current_user
    # )
    return await roles_service.update_role(id, role_data)


@router.delete('/{id}', response_model=RoleSchema)
async def delete_role(
    id: int,
    roles_service: Annotated[RolesService, Depends(get_rolesservices)],
    # current_user: Annotated[User, Depends(get_current_user)]
) -> RoleSchema:
    # await PermissionHandler.has_permission(
    #     required_permission=Permissions.CONTROL_ROLES_AND_PERMISSIONS.value,
    #     current_user=current_user
    # )
    return await roles_service.delete_role(id)
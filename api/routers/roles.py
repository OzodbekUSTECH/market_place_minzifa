from typing import Annotated
from fastapi import APIRouter, Depends
from services.roles import RolesService
from utils.dependency import get_rolesservices, get_current_user
from repositories.base import Pagination
from schemas.roles import RoleSchema, CreateRoleSchema, UpdateRoleSchema, RolePermissionsSchema
# from utils.permissions import read_roles, read_role_permissions, create_role, update_role, delete_role
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

@router.get('/{role_id}/permissions', name="get all permissions of role", response_model=list[RolePermissionsSchema])
async def get_permissions(
    role_id: int,
    roles_service: Annotated[RolesService, Depends(get_rolesservices)]
):  
    return await roles_service.get_role_permissions(role_id)



@router.get('/{role_id}', name="get role by ID", response_model=RoleSchema)
async def get_role_data_by_id(
    role_id: int,
    roles_service: Annotated[RolesService, Depends(get_rolesservices)]
) -> RoleSchema:
    return await roles_service.get_role_by_id(role_id)

@router.post('', name="Create Role", response_model=RoleSchema)
async def create_role_data(
    role_data: CreateRoleSchema,
    roles_service: Annotated[RolesService, Depends(get_rolesservices)]
) -> RoleSchema:
    return await roles_service.create_role(role_data)

@router.put('/{role_id}', name="Update Role", response_model=RoleSchema)
async def update_role_data(
    role_id: int,
    role_data: UpdateRoleSchema,
    roles_service: Annotated[RolesService, Depends(get_rolesservices)]
) -> RoleSchema:
    return await roles_service.update_role(role_id, role_data)


@router.delete('/{role_id}', name="Create Role", response_model=RoleSchema)
async def delete_role_data(
    role_id: int,
    roles_service: Annotated[RolesService, Depends(get_rolesservices)]
) -> RoleSchema:
    return await roles_service.delete_role(role_id)
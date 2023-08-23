from typing import Annotated
from fastapi import APIRouter, Depends
from services.rolepermissions import RolePermissionsService
from utils.dependency import get_rolepermissions, get_current_user
from repositories.base import Pagination
from schemas.rolepermissions import RolePermissionsSchema, CreateRolePermissionsSchema, DeleteRolePermissionsSchema
from utils.permissions import give_role_permission, delete_role_permission
router = APIRouter(
    prefix="/rolepermissions",
    tags=["Role and Permission connection"],
)



@router.post('', name='Give permission for a role', response_model=RolePermissionsSchema, dependencies=[Depends(give_role_permission)])
async def give_permission_data_for_role(
    role_permission_data: CreateRolePermissionsSchema,
    roleperms_service: Annotated[RolePermissionsService, Depends(get_rolepermissions)]
) -> RolePermissionsSchema:
    return await roleperms_service.give_permission_for_role(role_permission_data)


@router.delete('', name='Give permission for a role', response_model=RolePermissionsSchema, dependencies=[Depends(delete_role_permission)])
async def give_permission_data_for_role(
    role_permission_data: DeleteRolePermissionsSchema,
    roleperms_service: Annotated[RolePermissionsService, Depends(get_rolepermissions)]
) -> RolePermissionsSchema:
    return await roleperms_service.delete_permission_for_role(role_permission_data)


from typing import Annotated
from fastapi import APIRouter, Depends
from services.permissions import PermissionsService
from utils.dependency import get_permissionsservices, get_current_user
from repositories.base import Pagination
from schemas.permissions import PermissionSchema, CreatePermissionSchema, UpdatePermissionSchema
from utils.permissions import read_permissions,  create_permission, update_permission, delete_permission
router = APIRouter(
    prefix="/permessions",
    tags=["Permissions"],
)


@router.get('', name="get list of permessions", response_model=list[PermissionSchema], dependencies=[Depends(read_permissions)])
async def get_list_of_permessions(
    pagination: Annotated[Pagination, Depends()],
    perms_service: Annotated[PermissionsService, Depends(get_permissionsservices)]
) -> PermissionSchema:
    return await perms_service.get_all_permissions(pagination)


@router.get('/{permission_id}', name="get permission by ID", response_model=PermissionSchema, dependencies=[Depends(read_permissions)])
async def get_permission_data_by_id(
    permission_id: int,
    perms_service: Annotated[PermissionsService, Depends(get_permissionsservices)]
) -> PermissionSchema:
    return await perms_service.get_permission_by_id(permission_id)

@router.post('', name="create permission", response_model=PermissionSchema, dependencies=[Depends(create_permission)])
async def create_permission_data(
    permission_data: CreatePermissionSchema,
    perms_service: Annotated[PermissionsService, Depends(get_permissionsservices)]
) -> PermissionSchema:
    return await perms_service.create_permission(permission_data)


@router.put('/{permission_id}', name="update permission data", response_model=PermissionSchema, dependencies=[Depends(update_permission)])
async def update_permission_data(
    permission_id: int,
    permission_data: UpdatePermissionSchema,
    perms_service: Annotated[PermissionsService, Depends(get_permissionsservices)]
) -> PermissionSchema:
    return await perms_service.update_permission(permission_id, permission_data)


@router.delete("/{permission_id}", name="delete permission", response_model=PermissionSchema, dependencies=[Depends(delete_permission)])
async def delete_permission_data(
    permission_id: int,
    perms_service: Annotated[PermissionsService, Depends(get_permissionsservices)]
) -> PermissionSchema:
    return await perms_service.delete_permission(permission_id)
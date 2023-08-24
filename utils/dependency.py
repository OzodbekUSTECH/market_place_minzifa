from models import User, MailList, Role, Permission, RolePermission, TravelersAndManagersAssociation

from repositories.users import UsersRepository
from services.users import UsersService

from repositories.maillist import MailListRepository
from services.maillist import MailListService

from repositories.roles import RolesRepository
from services.roles import RolesService

from repositories.permissions import PermissionsRepository
from services.permissions import PermissionsService

from repositories.rolepermissions import RolePermissionsRepository
from services.rolepermissions import RolePermissionsService

from repositories.travelermanagers import TravelerManagersRepository
from services.travelermanagers import TravelerManagersService

from database.db import get_db
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer


#services dependencies
from repositories.unitofwork import UnitOfWork
from typing import Annotated

UOWDependency = Annotated[UnitOfWork, Depends(UnitOfWork)]

async def get_users_services(uow: UOWDependency):
    return UsersService(uow)


async def get_maillist_services(uow: UOWDependency):
    return MailListService(uow)

async def get_rolesservices(uow: UOWDependency):
    return RolesService(uow)

async def get_permissionsservices(uow: UOWDependency):
    return PermissionsService(uow)

async def get_rolepermissions(uow: UOWDependency):
    return RolePermissionsService(uow)

async def get_travelermanagers_services(uow: UOWDependency):
    return TravelerManagersService(uow)



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/users/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    users_service: UsersService = Depends(get_users_services)
):
    return await users_service.get_current_user(token)


from fastapi import Path

class PermissionChecker:
    def __init__(self, permission_endpoint: str):
        self.allowed_permission = permission_endpoint

    def __call__(
            self,
            current_user: User,
            user_id: int = None, 
        ) -> bool:
        
        if user_id and user_id == current_user.id:
            return True
        elif self.allowed_permission not in [rp.permission.endpoint for rp in current_user.role.role_permissions]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied. Insufficient privileges."
            )
        return True
    

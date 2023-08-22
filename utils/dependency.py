from models import User, MailList, Role, Permission, RolePermission, TravelersAndManagersAssociation

from services.users import UsersService
from services.maillist import MailListService
from services.roles import RolesService
from services.permissions import PermissionsService
from services.rolepermissions import RolePermissionsService
from services.travelermanagers import TravelerManagersService

from database.db import get_db
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from repositories.unitofwork import UnitOfWork
from typing import Annotated
UOWDep = Annotated[UnitOfWork, Depends(UnitOfWork)]

#services dependencies

async def get_users_services(db = Depends(get_db)):
    return UsersService(UnitOfWork(sess=db))


async def get_maillist_services(uow: UOWDep):
    return MailListService(uow)

async def get_rolesservices(uow: UOWDep):
    return RolesService(uow)

async def get_permissionsservices(uow: UOWDep):
    return PermissionsService(uow)

async def get_rolepermissions(uow: UOWDep):
    return RolePermissionsService(uow)

async def get_travelermanagers_services(uow: UOWDep):
    return TravelerManagersService(uow)



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/users/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    users_service: UsersService = Depends(get_users_services)
):
    return await users_service.get_current_user(token)



class PermissionChecker:
    def __init__(self, permission_endpoint: str):
        self.allowed_permission = permission_endpoint

    def __call__(self, current_user = Depends(get_current_user)):
        if self.allowed_permission not in [rp.permission.endpoint for rp in current_user.role.role_permissions]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied. Insufficient privileges."
            )
        return True
    


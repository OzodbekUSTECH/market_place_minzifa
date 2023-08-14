from models import User, MailList, Role, Permission, RolePermission, TravelersAndManagersAssociation

from repositories.users import UsersRepository
from services.users import UsersService

from repositories.maillist import MailListRepository
from services.maillist import MailListService

from repositories.roles import RolesRepository
from services.roles import RolesService

from repositories.permissions import PermissonsRepository
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

async def get_users_services(db: Session = Depends(get_db)):
    return UsersService(UsersRepository(session=db, model=User))


async def get_maillist_services(db: Session = Depends(get_db)):
    return MailListService(MailListRepository(session=db, model=MailList))

async def get_rolesservices(db: Session = Depends(get_db)):
    return RolesService(RolesRepository(session=db, model=Role))

async def get_permissionsservices(db: Session = Depends(get_db)):
    return PermissionsService(PermissonsRepository(session=db, model=Permission))

async def get_rolepermissions(db: Session = Depends(get_db)):
    return RolePermissionsService(RolePermissionsRepository(session=db, model=RolePermission))

async def get_travelermanagers_services(db: Session = Depends(get_db)):
    return TravelerManagersService(TravelerManagersRepository(session=db, model=TravelersAndManagersAssociation))



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
from models import User, MailList, Role, Permession

from repositories.users import UsersRepository
from services.users import UsersService

from repositories.maillist import MailListRepository
from services.maillist import MailListService

from repositories.roles import RolesRepository
from services.roles import RolesService

from repositories.permissions import PermissonsRepository
from services.permissions import PermissionsService

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
    return PermissionsService(PermissonsRepository(session=db, model=Permession))





oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/users/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    users_service: UsersService = Depends(get_users_services)
):
    print(token)
    return await users_service.get_current_user(token)



class RoleChecker:
    def __init__(self, roles: list[str]):
        self.allowed_roles = roles

    def __call__(self, current_user = Depends(get_current_user)):
        if current_user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied. Insufficient privileges."
            )
        return True
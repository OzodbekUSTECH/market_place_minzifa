from typing import Type
from models import User, MailList, Role, Permission, RolePermission, TravelersAndManagersAssociation

from database.db import Session
from repositories.users import UsersRepository
from repositories.maillist import MailListRepository
from repositories.roles import RolesRepository
from repositories.permissions import PermissionsRepository
from repositories.rolepermissions import RolePermissionsRepository
from repositories.travelermanagers import TravelerManagersRepository






class UnitOfWork:
    users: Type[UsersRepository]
    maillist: Type[MailListRepository]
    roles: Type[RolesRepository]
    permissions: Type[PermissionsRepository]
    role_permissions: Type[RolePermissionsRepository]
    travelers_managers: Type[TravelerManagersRepository]

    def __init__(self):
        self.session_factory = Session

    async def __aenter__(self):
        self.session = self.session_factory()
        self.users = UsersRepository(self.session, model=User)
        self.maillist = MailListRepository(self.session, model=MailList)
        self.roles = RolePermissionsRepository(self.session, model=Role)
        self.permissions = PermissionsRepository(self.session, model=Permission)
        self.role_permissions = RolePermissionsRepository(self.session, model=RolePermission)
        self.travelers_managers = TravelerManagersRepository(self.session, model=TravelersAndManagersAssociation)

    async def __aexit__(self, *args):
        await self.rollback()
        self.session.close()

    async def commit(self):
        self.session.commit()

    async def rollback(self):
        self.session.rollback()
        
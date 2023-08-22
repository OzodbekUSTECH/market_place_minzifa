from typing import Type
from models import User, MailList, Role, Permission, RolePermission, TravelersAndManagersAssociation

from database.db import session_maker
from repositories.users import UsersRepository
from repositories.maillist import MailListRepository
from repositories.roles import RolesRepository
from repositories.permissions import PermissionsRepository
from repositories.rolepermissions import RolePermissionsRepository
from repositories.travelermanagers import TravelerManagersRepository
from sqlalchemy.orm import Session






class UnitOfWork:
    users: Type[UsersRepository]
    maillist: Type[MailListRepository]
    roles: Type[RolesRepository]
    permissions: Type[PermissionsRepository]
    role_permissions: Type[RolePermissionsRepository]
    travelers_managers: Type[TravelerManagersRepository]

    def __init__(self, sess):
        

        self.session = sess
        self.users = UsersRepository(self.session, model=User)
        self.maillist = MailListRepository(self.session, model=MailList)
        self.roles = RolePermissionsRepository(self.session, model=Role)
        self.permissions = PermissionsRepository(self.session, model=Permission)
        self.role_permissions = RolePermissionsRepository(self.session, model=RolePermission)
        self.travelers_managers = TravelerManagersRepository(self.session, model=TravelersAndManagersAssociation)

    


        
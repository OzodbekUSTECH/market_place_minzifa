from typing import Type
from models import (
    User, 
    MailList, 
    Role, 
    Permission, 
    RolePermission, 
    TravelersAndManagersAssociation,
    Tour,
    TourPrice,
    Currency,
    TourStatus
)

from database.db import session_maker
from repositories import (
    UsersRepository, 
    MailListRepository, 
    RolesRepository, 
    PermissionsRepository,
    RolePermissionsRepository,
    TravelerManagersRepository,
    CurrenciesRepository,
    ToursRepository,
    TourPricesRepository,
    TourStatusesRepository
)







class UnitOfWork:
    users: Type[UsersRepository]
    maillist: Type[MailListRepository]
    roles: Type[RolesRepository]
    permissions: Type[PermissionsRepository]
    role_permissions: Type[RolePermissionsRepository]
    travelers_managers: Type[TravelerManagersRepository]
    tours: Type[ToursRepository]
    tour_prices: Type[TourPricesRepository]
    currencies: Type[CurrenciesRepository]
    tour_statuses: Type[TourStatusesRepository]

    def __init__(self):
        self.session_factory = session_maker

    async def __aenter__(self):
        self.session = self.session_factory()
        self.users = UsersRepository(self.session, model=User)
        self.maillist = MailListRepository(self.session, model=MailList)
        self.roles = RolesRepository(self.session, model=Role)
        self.permissions = PermissionsRepository(self.session, model=Permission)
        self.role_permissions = RolePermissionsRepository(self.session, model=RolePermission)
        self.travelers_managers = TravelerManagersRepository(self.session, model=TravelersAndManagersAssociation)
        self.tours = ToursRepository(self.session, model=Tour)
        self.tour_prices = TourPricesRepository(self.session, model=TourPrice)
        self.currencies = CurrenciesRepository(self.session, model=Currency)
        self.tour_statuses = TourStatusesRepository(self.session, model=TourStatus)

    async def __aexit__(self, *args):
        await self.rollback()
        self.session.close()

    async def commit(self):
        self.session.commit()

    async def rollback(self):
        self.session.rollback()
        
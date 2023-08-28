from models import User
from services import (
    UsersService, 
    MailListService, 
    RolesService, 
    PermissionsService, 
    RolePermissionsService, 
    TravelerManagersService,
    ToursService,
    CurrenciesService,
    TourPricesService,
    TourStatusesService,
    TourActivitiesService,
    ActivitiesService,
    FavoriteToursService,
    TourCommentsService,
    TourCommentsMediaService,
)
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from database.unitofwork import UnitOfWork
from typing import Annotated

#services dependencies


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

async def get_tours_services(uow: UOWDependency):
    return ToursService(uow)

async def get_tour_prices_services(uow: UOWDependency):
    return TourPricesService(uow)

async def get_currencies_services(uow: UOWDependency):
    return CurrenciesService(uow)

async def get_tour_statuses_services(uow: UOWDependency):
    return TourStatusesService(uow)

async def get_tour_activities_services(uow: UOWDependency):
    return TourActivitiesService(uow)

async def get_activities_services(uow: UOWDependency):
    return ActivitiesService(uow)

async def get_favorites_services(uow: UOWDependency):
    return FavoriteToursService(uow)

async def get_tour_comments_services(uow: UOWDependency):
    return TourCommentsService(uow)

async def get_tour_comments_media_services(uow: UOWDependency):
    return TourCommentsMediaService(uow)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/users/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    users_service: UsersService = Depends(get_users_services)
) -> User:
    return await users_service.get_current_user(token)




    

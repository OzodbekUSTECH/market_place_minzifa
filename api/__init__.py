from api.routers.users import router as auth_router
from api.routers.maillist import router as maillist_router
from api.routers.roles import router as roles_router
from api.routers.permissions import router as permissions_router
from api.routers.rolepermissions import router as rolepermissions_router
from api.routers.travelermanagers import router as travelermanagers_router
from api.routers.currencies import router as currency_router
from api.routers.tours import router as tour_router
from api.routers.tourprices import router as tour_prices_router
from api.routers.tourstatuses import router as statuses_router
from api.routers.activities import router as activities_router
from api.routers.tour_activities import router as tour_activities_router
from api.routers.favorite_tours import router as tour_favorites_router
all_routers = [
    auth_router,
    maillist_router,
    roles_router,
    permissions_router,
    rolepermissions_router,
    travelermanagers_router,
    currency_router,
    tour_router,
    tour_prices_router,
    tour_activities_router,
    tour_favorites_router,
    statuses_router,
    activities_router,
]
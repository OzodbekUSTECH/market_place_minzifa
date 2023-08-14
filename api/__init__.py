from api.routers.users import router as auth_router
from api.routers.maillist import router as maillist_router
from api.routers.roles import router as roles_router
from api.routers.permissions import router as permissions_router
from api.routers.rolepermissions import router as rolepermissions_router
from api.routers.travelermanagers import router as travelermanagers_router
all_routers = [
    auth_router,
    maillist_router,
    roles_router,
    permissions_router,
    rolepermissions_router,
    travelermanagers_router
]
from api.routers.users import router as auth_router
from api.routers.maillist import router as maillist_router
all_routers = [
    auth_router,
    maillist_router
]
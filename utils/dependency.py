from models import User
import services
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from database import UOWDependency
#services dependencies




oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")


async def get_current_user(
    uow: UOWDependency,
    token: str = Depends(oauth2_scheme),
    # users_service: services.UsersService = Depends(get_users_services)
) -> User:
    return await services.users_service.get_current_user(uow, token)




    

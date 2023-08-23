from repositories.users import UsersRepository
from schemas.users import UserCreateSchema, UserUpdateSchema, UserSchema, TokenSchema
from security.password import PasswordHandler
from repositories.base import Pagination
from fastapi import HTTPException, status
from datetime import timedelta
from jose import JWTError, jwt
from schemas.users import TokenData
from datetime import datetime
from security.jwthandler import JWTHandler

from repositories.unitofwork import UnitOfWork

class UsersService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def register_user(self, user_data: UserCreateSchema) -> UserSchema:
        async with self.uow:
            existing_user = await self.uow.users.get_by_email(user_data.email)
            if existing_user:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already registered")

            hashed_password = PasswordHandler.hash(user_data.password)

            user_dict = user_data.model_dump()
            user_dict["password"] = hashed_password
            new_user = await self.uow.users.create(user_dict)
            await self.uow.commit()
            return new_user
        
    async def get_list_of_users(self, pagination: Pagination) -> list[UserSchema]:
        async with self.uow:
            users = await self.uow.users.get_all(pagination)
            await self.uow.commit()
            return users

    async def get_user_by_id(self, user_id: int) -> UserSchema:
        async with self.uow:
            user = await self.uow.users.get_by_id(user_id)
            await self.uow.commit()
            return user

    async def update_user(self, user_id: int, user_data: UserUpdateSchema) -> UserSchema:
        user_dict = user_data.model_dump()
        async with self.uow:
            updated_user = await self.uow.users.update(user_id, user_dict)
            await self.uow.commit()
            return updated_user


    async def delete_user(self, user_id: int) -> UserSchema:
        async with self.uow:
            deleted_user = await self.uow.users.delete(user_id)
            await self.uow.commit()
            return deleted_user

    async def authenticate_user(self, email: str, password: str) -> TokenSchema:
        async with self.uow:
            user = await self.uow.users.get_by_email(email)
                
            if not user or not PasswordHandler.verify(password, user.password):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect username or password",
                    headers={"WWW-Authenticate": "Bearer"},
                )

            access_token_expires = timedelta(minutes=JWTHandler.ACCESS_TOKEN_EXPIRE_MINUTES)

            access_token = await JWTHandler.create_access_token(
                data={"email": user.email}, expires_delta=access_token_expires
            )
            return TokenSchema(access_token=access_token, token_type="Bearer")

    
    
    async def get_current_user(self, token: str) -> UserSchema:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,   
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = await JWTHandler.decode(token)
            email: str = payload.get("email")  # "sub" is the key used by JWT to represent the subject (usually user ID or email)
            if email is None:
                raise credentials_exception
            token_data = TokenData(email=email)
        except JWTError:
            raise credentials_exception
        async with self.uow:
        
            user = await self.uow.users.get_by_email(token_data.email)
            
            if user is None:
                raise credentials_exception

            await self.uow.commit()

            return user

    async def get_user_by_email(self, email: str) -> UserSchema:
        async with self.uow:
            user = await self.uow.users.get_by_email(email)
            await self.uow.commit()
            return user
    
    async def generate_reset_token(self, email: str) -> str:
        payload = {
            "email": email,
            "exp": datetime.utcnow() + timedelta(hours=2)
        }
        token = await JWTHandler.encode(payload)
        return token
    
    async def reset_password(self, token: str, password: str) -> UserSchema:
        
        user = await self.get_current_user(token)
        hashed_password = PasswordHandler.hash(password)
        password_dict = {
            "password": hashed_password
        }
        async with self.uow:
            updated_user = await self.uow.users.update(user.id, password_dict)
            await self.uow.commit()
            return updated_user

    
    # async def get_travelers(self, manager_id: int):
    #     async with self.uow:
    #         return await self.uow.users.get_travelers_of_manager(manager_id)
from repositories.users import UsersRepository
from schemas.users import UserCreateSchema, UserUpdateSchema, UserSchema, TokenSchema
from utils.password import PasswordHandler
from repositories.base import Pagination
from fastapi import HTTPException, status
from datetime import timedelta
from jose import JWTError, jwt
from schemas.users import TokenData
from datetime import datetime

class UsersService:
    def __init__(self, users_repo: UsersRepository):
        self.users_repo: UsersRepository = users_repo

    async def register_user(self, user_data: UserCreateSchema) -> UserSchema:
        existing_user = await self.users_repo.get_by_email(user_data.email)
        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already registered")

        hashed_password = PasswordHandler.hash(user_data.password)

        user_dict = user_data.model_dump()
        user_dict["password"] = hashed_password
        new_user = await self.users_repo.create(user_dict)
        return new_user
    
    async def get_all_users(self, pagination: Pagination) -> list[UserSchema]:
        users = await self.users_repo.get_all(pagination)
        return users

    async def get_user_by_id(self, user_id: int) -> UserSchema:
        user = await self.users_repo.get_by_id(user_id)
        return user

    async def update_user(self, user_id: int, user_data: UserUpdateSchema) -> UserSchema:
        user_dict = user_data.model_dump()
        updated_user = await self.users_repo.update(user_id, user_dict)
        return updated_user


    async def delete_user(self, user_id: int) -> UserSchema:
        deleted_user = await self.users_repo.delete(user_id)
        return deleted_user

    async def authenticate_user(self, email: str, password: str) -> TokenSchema:
        user = await self.users_repo.get_by_email(email)
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        if not PasswordHandler.verify(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token_expires = timedelta(minutes=self.users_repo.ACCESS_TOKEN_EXPIRE_MINUTES)

        access_token = await self.users_repo.create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        return TokenSchema(access_token=access_token, token_type="Bearer")

    
    
    async def get_current_user(self, token: str) -> UserSchema:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,   
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, self.users_repo.SECRET_KEY, algorithms=[self.users_repo.ALGORITHM])
            email: str = payload.get("sub")  # "sub" is the key used by JWT to represent the subject (usually user ID or email)
            if email is None:
                raise credentials_exception
            token_data = TokenData(email=email)
        except JWTError:
            raise credentials_exception
        
        user = await self.users_repo.get_by_email(token_data.email)
        
        if user is None:
            raise credentials_exception

        return user

    async def get_user_by_email(self, email: str) -> UserSchema:
        return await self.users_repo.get_by_email(email)
    
    async def generate_reset_token(self, email: str) -> str:
        payload = {
            "sub": email,
            "exp": datetime.utcnow() + timedelta(hours=2)
        }
        token = jwt.encode(payload, self.users_repo.SECRET_KEY, algorithm=self.users_repo.ALGORITHM)
        return token
    
    async def reset_password(self, token: str, password: str) -> UserSchema:
        user = await self.get_current_user(token)
        hashed_password = PasswordHandler.hash(password)
        password_dict = {
            "password": hashed_password
        }
        return await self.users_repo.update(user.id, password_dict)
        

    
    
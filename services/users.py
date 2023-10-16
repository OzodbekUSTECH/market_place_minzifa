from schemas.users import CreateUserSchema, UpdateUserSchema,  TokenSchema, ResetPasswordSchema
from security.password import PasswordHandler
from repositories import paginate
from datetime import timedelta
from jose import JWTError
from schemas.users import TokenData
from datetime import datetime
import models
from security.jwthandler import JWTHandler
from database import UnitOfWork, email_sender
from utils.exceptions import CustomExceptions
from utils.locale_handler import LocaleHandler


class UsersService:
    

    async def send_email_message_to_welcome_user(self, user: models.User, locale: LocaleHandler) -> None:
        await email_sender.send_welcome_email_message(
            user=user, 
            locale=locale.get_language,
            subject = "Welcome to MARKET PLACE MINZIFATRAVEL",
            template_name="registration.html"
        )
            

    async def register_user(self, uow: UnitOfWork, user_data: CreateUserSchema, locale: LocaleHandler) -> models.User:
        async with uow:
            existing_user = await uow.users.get_by_email(user_data.email)
            if existing_user:
                raise CustomExceptions.conflict("Already exists user with this email")

            hashed_password = PasswordHandler.hash(user_data.password)

            user_dict = user_data.model_dump()
            user_dict["password"] = hashed_password
            user = await uow.users.create(user_dict)
            await uow.commit()
            await self.send_email_message_to_welcome_user(
                user=user, locale=locale)
            return user
        
    async def get_list_of_users(
            self, 
            uow: UnitOfWork,
            role_id: int | None,
        ) -> list[models.User]:
        async with uow:
            if role_id:
                return paginate(await uow.users.get_all_by(role_id=role_id))
            return await uow.users.get_all()
        
    

    async def get_user_by_id(self, uow: UnitOfWork, id: int) -> models.User:
        async with uow:
            user = await uow.users.get_by_id(id)
            return user
        
    
    async def update_user(self, uow: UnitOfWork, id: int, user_data: UpdateUserSchema) -> models.User:
        user_dict = user_data.model_dump()
        async with uow:
            updated_user = await uow.users.update(id, user_dict)
            await uow.commit()
            return updated_user


    async def ban_or_unban_user(self, uow: UnitOfWork, id: int, ban: bool) -> models.User:
        async with uow:
            user: models.User = await uow.users.get_by_id(id)
            user.is_banned = ban
            await uow.commit()
            return user
        
    async def delete_user(self, uow: UnitOfWork, id: int) -> models.User:
        async with uow:
            user: models.User = await uow.users.delete(id)
            await uow.commit()
            return user

    async def authenticate_user(self, uow: UnitOfWork, email: str, password: str) -> TokenSchema:
        async with uow:
            user: models.User = await uow.users.get_by_email(email)
                
            if not user or not PasswordHandler.verify(password, user.password):
                raise CustomExceptions.unauthorized("Incorrect email or password")
            if user and user.is_banned:
                raise CustomExceptions.forbidden("The user is banned")

            access_token_expires = timedelta(minutes=JWTHandler.ACCESS_TOKEN_EXPIRE_MINUTES)

            access_token = await JWTHandler.create_access_token(
                data={"email": user.email}, expires_delta=access_token_expires
            )
            return TokenSchema(access_token=access_token, token_type="Bearer")

    
    
    async def get_current_user(self, uow: UnitOfWork, token: str) -> models.User:
        credentials_exception = CustomExceptions.unauthorized("Could not validate credentials")
        try:
            payload = await JWTHandler.decode(token)
            email: str = payload.get("email") 
            if email is None:
                raise credentials_exception
            token_data = TokenData(email=email)
        except JWTError:
            raise credentials_exception
        
        async with uow:
        
            user = await uow.users.get_by_email(token_data.email)
            
            if user is None:
                raise credentials_exception

            return user

    async def send_reset_password_link(self, uow: UnitOfWork, locale: str, email: str) -> dict:
        async with uow:
            user: models.User = await uow.users.get_by_email(email)
            if not user:
                raise CustomExceptions.not_found("Email not found")
            token = await self._generate_reset_token(email)
            await email_sender.send_reset_password_link(locale, email, token)   
                 
            return {"message": "Reset Password sent successfully"}
    
    async def _generate_reset_token(self, email: str) -> str:
        payload = {
            "email": email,
            "exp": datetime.utcnow() + timedelta(hours=2)
        }
        token = await JWTHandler.encode(payload)
        return token
    
    async def reset_password(self, uow: UnitOfWork, token: str, password_data: ResetPasswordSchema) -> models.User:
        #сессия создается внутри функции get_currenct_user
        user = await self.get_current_user(uow, token)
        hashed_password = PasswordHandler.hash(password_data.password)
        password_dict = {
            "password": hashed_password
        }
        updated_user = await uow.users.update(user.id, password_dict)
        await uow.commit()
        return updated_user

    
    
    

users_service = UsersService()
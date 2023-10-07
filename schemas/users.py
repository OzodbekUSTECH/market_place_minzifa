import re
from pydantic import BaseModel, EmailStr, field_validator, Field
from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema


class BaseUserSchema(CreateBaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    company_name: str | None
    phone_number: str | None
    link: str | None
    about: str | None
    role_id: int


class CreateUserSchema(BaseUserSchema):
    password: str = Field(min_length=8, max_length=64)

    # @field_validator("password")
    # def password_must_contain_special_characters(cls, v):
    #     if not re.search(r"[^a-zA-Z0-9]", v):
    #         raise ValueError("Password must contain special characters")
    #     return v

    # @field_validator("password")
    # def password_must_contain_numbers(cls, v):
    #     if not re.search(r"[0-9]", v):
    #         raise ValueError("Password must contain numbers")
    #     return v

    # @field_validator("password")
    # def password_must_contain_uppercase(cls, v):
    #     if not re.search(r"[A-Z]", v):
    #         raise ValueError("Password must contain uppercase characters")
    #     return v

    # @field_validator("password")
    # def password_must_contain_lowercase(cls, v):
    #     if not re.search(r"[a-z]", v):
    #         raise ValueError("Password must contain lowercase characters")
    #     return v


class UpdateUserSchema(UpdateBaseModel, BaseUserSchema):
    pass

class UserSchema(IdResponseSchema, UpdateUserSchema):
    rating: int | float



class UserSchemaWithTravelExpertAndEmployees(UserSchema):
    travel_expert: UserSchema | None
    employees: list[UserSchema]
    # @validator('rating')
    # def round_rating(cls, value):
    #     return round(value, 2)


class TokenSchema(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str


class ResetPasswordSchema(BaseModel):
    password: str = Field(min_length=8, max_length=64)

    @field_validator("password")
    def password_must_contain_special_characters(cls, v):
        if not re.search(r"[^a-zA-Z0-9]", v):
            raise ValueError("Password must contain special characters")
        return v

    @field_validator("password")
    def password_must_contain_numbers(cls, v):
        if not re.search(r"[0-9]", v):
            raise ValueError("Password must contain numbers")
        return v

    @field_validator("password")
    def password_must_contain_uppercase(cls, v):
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain uppercase characters")
        return v

    @field_validator("password")
    def password_must_contain_lowercase(cls, v):
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain lowercase characters")
        return v

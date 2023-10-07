from pydantic import field_validator, Field, ConfigDict, BaseModel
from typing import Union
from schemas import CreateBaseModel, UpdateBaseModel, IdResponseSchema
from schemas.tour_media_group import TourMediaSchema
from schemas.categories import CategorySchema
from schemas.types import TypeSchema
from schemas.tour_statuses import TourStatusSchema
from schemas.tour_children_ages import TourChildrenAgeSchema
from schemas.tour_activity_levels import TourActivityLevelSchema
from schemas.languages import LanguageSchema
from schemas.activities import ActivitySchema
from schemas.accommodations import AccommodationSchema
from schemas.countries import CountrySchema
from schemas.regions import RegionSchema
from schemas.users import UserSchema



class CustomTourPriceSchema(BaseModel):
    currency_id: int
    name: Union[dict[str, str], str]
    symbol: str
    exchange_rate: float | None
    price: int
    price_for_day: int
    discount_percentage: float | None
    new_price: float | None
    discount_start_date: str | None
    discount_end_date: str | None




class CreateTourSchema(CreateBaseModel):
    title: Union[dict[str, str], str]
    description: Union[dict[str, str], str]
    user_id: int
    status_id: int
    
    age_group_from: int = Field(ge=18, le=100)
    age_group_to: int = Field(ge=18, le=100)

    children_age_id: int
    activity_level_id: int

    start_date: str
    end_date: str

    total_places: int
    free_places: int

    is_guaranteed: bool

    category_ids: list[int] = Field(exclude=True)

    main_type_id: int
    
    additional_type_ids: list[int] = Field(exclude=True)

    language_ids: list[int] = Field(exclude=True)

    activity_ids: list[int] = Field(exclude=True)

    accommodation_ids: list[int] = Field(exclude=True)

    country_ids: list[int] = Field(exclude=True)

    region_ids: list[int] = Field(exclude=True)

    currency_id: int = Field(exclude=True)
    price: int = Field(exclude=True)
    discount_percentage: float | None = Field(None, exclude=True)
    new_price: float | None = Field(None, exclude=True)
    discount_start_date: str | None = Field(None, exclude=True)
    discount_end_date: str | None = Field(None, exclude=True)

    
    

class UpdateTourSchema(UpdateBaseModel, CreateTourSchema):
    pass

class TourSchema(IdResponseSchema, UpdateTourSchema):
    duration: int
    is_guaranteed: bool
    is_one_day_tour: bool
    user: UserSchema
    status: TourStatusSchema
    children_age: TourChildrenAgeSchema
    activity_level: TourActivityLevelSchema
    photos: list[TourMediaSchema]
    categories: list[CategorySchema]
    main_type: TypeSchema
    additional_types: list[TypeSchema]
    languages: list[LanguageSchema]
    activities: list[ActivitySchema]
    accommodations: list[AccommodationSchema]
    countries: list[CountrySchema]
    regions: list[RegionSchema]
    prices: list[CustomTourPriceSchema]

    total_free_places: int
    


    ######################################
    user_id: int = Field(exclude=True)
    free_places: int = Field(exclude=True)
    status_id: int = Field(exclude=True)
    children_age_id: int = Field(exclude=True)
    activity_level_id: int = Field(exclude=True)
    main_type_id: int = Field(exclude=True)
    start_month: int = Field(exclude=True)
    
   
    currency_id: int = Field(None, exclude=True)
    price: int | None = Field(None, exclude=True)
    discount_percentage: float | None = Field(None, exclude=True)
    new_price: float | None = Field(None, exclude=True)
    discount_start_date: str | None = Field(None, exclude=True)
    discount_end_date: str | None = Field(None, exclude=True)
    
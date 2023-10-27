from pydantic import Field, BaseModel
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
from schemas.accommodation_types import AccommodationTypeSchema
from schemas.countries import CountrySchema
from schemas.regions import RegionSchema
from schemas.users import UserSchema
from schemas.tour_days import TourDaySchema
from schemas.tour_hotels import TourHotelSchema
from schemas.tour_importants import TourImportantSchema
from schemas.tours_package.includes import IncludeInPriceSchema
from schemas.tours_package.excludes import ExcludeInPriceSchema
from schemas.roles import RoleSchema


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
##################################
class CustomCountrySchema(BaseModel):
    id: int
    name: Union[dict[str, str], str]

class CustomTypeSchema(CustomCountrySchema):
    pass
    

    



class CreateTourSchema(CreateBaseModel):
    title: Union[dict[str, str], str]
    description: Union[dict[str, str], str]
    user_id: int
    tour_leader_id: int
    status_id: int
    age_group_from: int = Field(le=100)
    age_group_to: int = Field(le=100)

    children_age_id: int
    activity_level_id: int

    start_date: str | None
    end_date: str | None

    total_places: int
    free_places: int

    is_guaranteed: bool

    # category_ids: list[int] = Field(exclude=True)
    category_id: int

    main_type_id: int

    is_allowed_individually: bool

    # included_in_price: Union[list[dict[str, str]], list[str]]
    # not_included_in_price: Union[list[dict[str, str]], list[str]]


    additional_type_ids: list[int] | None = Field(None, exclude=True)

    language_ids: list[int] = Field(exclude=True)

    activity_ids: list[int] | None = Field(None, exclude=True)

    accommodation_ids: list[int] | None = Field(None, exclude=True)

    accommodation_type_ids: list[int] | None = Field(None, exclude=True)


    country_ids: list[int] | None = Field(None, exclude=True)

    region_ids: list[int] | None = Field(None, exclude=True)

    currency_id: int = Field(exclude=True)
    price: int = Field(exclude=True)
    discount_percentage: float | None = Field(None, exclude=True)
    new_price: float | None = Field(None, exclude=True)
    discount_start_date: str | None = Field(None, exclude=True)
    discount_end_date: str | None = Field(None, exclude=True)

    
    

class UpdateTourSchema(UpdateBaseModel, CreateTourSchema):
    pass

class TourSchema(IdResponseSchema, UpdateTourSchema):
    url: str
    user_rating: int | float
    duration: int | None
    photos: list[TourMediaSchema]
    main_type: CustomTypeSchema
    additional_type_ids: list[int]
    language_ids: list[int]
    activity_ids: list[int]
    accommodation_ids: list[int]
    accommodation_type_ids: list[int]
    countries: list[CustomCountrySchema]
    region_ids: list[int]
    prices: list[CustomTourPriceSchema]

    total_free_places: int
    
    amount_reviews: int
    amount_countries: int
    amount_regions: int
    
    free_places: int = Field(exclude=True)
    main_type_id: int = Field(exclude=True)
    start_month: int = Field(exclude=True)
    category_id: int = Field(exclude=True)   
    currency_id: int = Field(None, exclude=True)
    price: int | None = Field(None, exclude=True)
    discount_percentage: float | None = Field(None, exclude=True)
    new_price: float | None = Field(None, exclude=True)
    discount_start_date: str | None = Field(None, exclude=True)
    discount_end_date: str | None = Field(None, exclude=True)
    
    

class OneTourSchema(TourSchema):
    children_age: TourChildrenAgeSchema
    activity_level: TourActivityLevelSchema

    additional_type_ids: list[int]
    languages: list[LanguageSchema]
    activities: list[ActivitySchema]
    accommodations: list[AccommodationSchema]
    accommodation_types: list[AccommodationTypeSchema]
    countries: list[CountrySchema]
    regions: list[RegionSchema]

    days: list[TourDaySchema]
    hotels: list[TourHotelSchema]
    importants: list[TourImportantSchema]
    includes_in_price: list[IncludeInPriceSchema]
    excludes_in_price: list[ExcludeInPriceSchema]

    
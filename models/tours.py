from models import BaseTable
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import (
        User,
        TourStatus,
        TourChildrenAge,
        TourActivityLevel,
        TourMedia,
        Category,
        Type,
        Language,
        Activity,
        Accommodation,
        Country,
        Region,
        Currency,
        TourComment,
        TourDay,
        TourHotel,
        TourImportant,
        AccommodationType,
        IncludeInPrice,
        ExcludeInPrice
    )


class Tour(BaseTable):
    __tablename__ = "tours"

    title: Mapped[dict] = mapped_column(type_=JSONB)
    description: Mapped[dict] = mapped_column(type_=JSONB)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("tour_statuses.id"))

    age_group_from: Mapped[int]
    age_group_to: Mapped[int]

    children_age_id: Mapped[int] = mapped_column(ForeignKey("tour_children_ages.id"))

    activity_level_id: Mapped[int] = mapped_column(
        ForeignKey("tour_activity_levels.id")
    )

    start_date: Mapped[str]
    end_date: Mapped[str]

    total_places: Mapped[int]
    free_places: Mapped[int]

    is_guaranteed: Mapped[bool] = mapped_column(default=False, server_default="false")

    main_type_id: Mapped[int] = mapped_column(ForeignKey("types.id"))

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    is_allowed_individually: Mapped[bool] = mapped_column(default=False, server_default="false")

    # included_in_price: Mapped[list[dict]] = mapped_column(JSONB)
    # not_included_in_price: Mapped[list[dict]] = mapped_column(JSONB)
    
    @hybrid_property
    def total_free_places(self) -> int:
        return self.free_places
    
    @hybrid_property
    def start_month(self) -> int:
        # Преобразование строки start_date в объект даты
        start_date_obj = datetime.strptime(self.start_date, "%d.%m.%Y")
        # Извлечение месяца в виде числа (1-12)
        return start_date_obj.month

    @hybrid_property
    def duration(self) -> int:
        start_date = datetime.strptime(self.start_date, "%d.%m.%Y")
        end_date = datetime.strptime(self.end_date, "%d.%m.%Y")
        delta = end_date - start_date
        return delta.days

    @hybrid_property
    def is_one_day_tour(self) -> bool:
        return self.duration == 1

    # @hybrid_property
    # def category_ids(self) -> list[int]:
    #     return [category.id for category in self.categories]
    
    @hybrid_property
    def additional_type_ids(self) -> list[int]:
        return [additional_type.id for additional_type in self.additional_types]
    
    @hybrid_property
    def language_ids(self) -> list[int]:
        return [language.id for language in self.languages]

    @hybrid_property
    def activity_ids(self) -> list[int]:
        return [activity.id for activity in self.activities]
    
    @hybrid_property
    def accommodation_ids(self) -> list[int]:
        return [accommodation.id for accommodation in self.accommodations]
    
    @hybrid_property
    def accommodation_type_ids(self) -> list[int]:
        return [accommodation_type.id for accommodation_type in self.accommodation_types]

    @hybrid_property
    def country_ids(self) -> list[int]:
        return [country.id for country in self.countries]
    
    @hybrid_property
    def region_ids(self) -> list[int]:
        return [region.id for region in self.regions]
    


    @hybrid_property
    def rating(self) -> int | float:
        default = 0
        if self.comments:
            for comment in self.comments:
                if comment.rating:
                    default += comment.rating

        return default
    
    @hybrid_property
    def amount_reviews(self) -> int:
        default = 0
        if self.comments:
            for comment in self.comments:
                if comment.rating:
                    default += 1
        return default
    
    @hybrid_property
    def amount_countries(self) -> int:
        return len(self.countries)
    
    @hybrid_property
    def amount_regions(self) -> int:
        return len(self.regions)
    
    @hybrid_property
    def has_discount(self) -> bool:
        if self.prices[0].discount_percentage:
            return True
        return False

    user: Mapped["User"] = relationship(back_populates="tours", lazy="subquery")
    status: Mapped["TourStatus"] = relationship(lazy="subquery")
    children_age: Mapped["TourChildrenAge"] = relationship(lazy="subquery")
    activity_level: Mapped["TourActivityLevel"] = relationship(lazy="subquery")
    photos: Mapped[list["TourMedia"]] = relationship(cascade="all, delete-orphan", lazy="subquery")

    category: Mapped["Category"] = relationship(lazy="subquery")
    # categories: Mapped[list["Category"]] = relationship(secondary="tour_categories", lazy="subquery", cascade='all,delete')
    main_type: Mapped["Type"] = relationship(lazy="subquery")
    additional_types: Mapped[list["Type"]] = relationship(secondary="tour_additional_types", lazy="subquery",cascade="all, delete") 
    languages: Mapped[list["Language"]] = relationship(secondary="tour_languages", lazy="subquery",cascade="all, delete")
    activities: Mapped[list["Activity"]] = relationship(secondary="tour_activities", lazy="subquery",cascade="all, delete")
    accommodations: Mapped[list["Accommodation"]] = relationship(secondary="tour_accommodations", lazy="subquery",cascade="all, delete")
    accommodation_types: Mapped[list["AccommodationType"]] = relationship(secondary="tour_accommodation_types", lazy="subquery", cascade="all, delete")
    countries: Mapped[list["Country"]] = relationship(secondary="tour_countries", lazy="subquery",cascade="all, delete")
    regions: Mapped[list["Region"]] = relationship(secondary="tour_regions", lazy="subquery",cascade="all, delete")
    prices: Mapped[list["Currency"]] = relationship(
            secondary="tour_prices",
            lazy="subquery",
            cascade="all, delete",
            overlaps="price_instance"  # Add this parameter
        )
    comments: Mapped[list["TourComment"]] = relationship(lazy="immediate", cascade="all, delete-orphan")
    days: Mapped[list["TourDay"]] = relationship(lazy="subquery", cascade="all, delete-orphan")
    hotels: Mapped[list["TourHotel"]] = relationship(lazy="subquery", cascade="all, delete-orphan")
    importants: Mapped[list["TourImportant"]] = relationship(lazy="subquery", cascade="all, delete-orphan")
    includes_in_price: Mapped[list["IncludeInPrice"]] = relationship(lazy="subquery", cascade="all, delete-orphan")
    excludes_in_price: Mapped[list["ExcludeInPrice"]] = relationship(lazy="subquery", cascade="all, delete-orphan")
    

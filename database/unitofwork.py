from typing import Type, Union
from utils.locale_handler import LocaleHandler
from sqlalchemy.ext.declarative import DeclarativeMeta

import models

from database.db import session_maker
import repositories






class UnitOfWork:
    users: Type[repositories.UsersRepository]
    roles: Type[repositories.RolesRepository]
    user_employees: Type[repositories.UserEmployeesRepository]
    emails: Type[repositories.EmailsRepository]
    currencies: Type[repositories.CurrenciesRepository]
    activities: Type[repositories.ActivitiesRepository]
    languages = Type[repositories.LanguagesRepository]
    accommodations: Type[repositories.AccommodationsRepository]
    categories: Type[repositories.CategoriesRepository]
    types: Type[repositories.TypesRepository]
    countries: Type[repositories.CountriesRepository]
    regions: Type[repositories.RegionsRepository]

    tour_statuses: Type[repositories.TourStatusesRepository]
    tour_children_ages: Type[repositories.TourChildrenAgesRepository]
    tour_activity_levels: Type[repositories.TourActivityLevelsRepository]
    tours: Type[repositories.ToursRepository]
    tour_media_group: Type[repositories.TourMediaGroupRepository]
    tour_categories: Type[repositories.TourCategoriesRepository]
    tour_additional_types: Type[repositories.TourAdditionalTypesRepository]
    tour_languages: Type[repositories.TourLanguagesRepository]
    tour_activities: Type[repositories.TourActivitiesRepository]
    tour_accommodations: Type[repositories.TourAccommodationsRepository]
    tour_countries: Type[repositories.TourCountriesRepository]
    tour_regions: Type[repositories.TourRegionsRepository]
    tour_prices: Type[repositories.TourPricesRepository]

    tour_comments: Type[repositories.TourCommentsRepository]
    tour_comments_media: Type[repositories.TourCommentsMediaRepository]

    blogs: Type[repositories.BlogsRepository]
    blog_media: Type[repositories.BlogMediaRepository]
    blog_countries: Type[repositories.BlogCountriesRepository]

    support_questions: Type[repositories.SupportQuestionsRepository]
    question_docs: Type[repositories.QuestionDocsRepository]

    sold_tours: Type[repositories.SoldToursRepository]

    
    # tour_prices: Type[TourPricesRepository]
    # TourActivitiesRepository: Type[TourActivitiesRepository]
    # favorite_tours: Type[FavoriteToursRepository]
    # tour_comments: Type[TourCommentsRepository]
    # tour_comments_media: Type[TourCommentsMediaRepository]
    # ip_tour_view: Type[IPTourViewRepository]
    # ip_and_tours_view: Type[IPAndToursViewRepository]
    # tour_lagnuages = Type[TourLanguagesRepository]


    def __init__(self):
        self.session_factory = session_maker

    async def __aenter__(self):
        self.session = self.session_factory()
        self.users = repositories.UsersRepository(self.session, model=models.User)
        self.roles = repositories.RolesRepository(self.session, model=models.Role)
        self.user_employees = repositories.UserEmployeesRepository(self.session, model=models.UserEmployee)
        self.emails = repositories.EmailsRepository(self.session, model=models.Email)
        self.currencies = repositories.CurrenciesRepository(self.session, model=models.Currency)
        self.activities = repositories.ActivitiesRepository(self.session, model=models.Activity)
        self.languages = repositories.LanguagesRepository(self.session, model=models.Language)
        self.accommodations = repositories.AccommodationsRepository(self.session, model=models.Accommodation)
        self.categories = repositories.CategoriesRepository(self.session, model=models.Category)
        self.types = repositories.TypesRepository(self.session, model=models.Type)
        self.countries = repositories.CountriesRepository(self.session, model= models.Country)
        self.regions = repositories.RegionsRepository(self.session, model=models.Region)


        self.tour_statuses = repositories.TourStatusesRepository(self.session, model=models.TourStatus)
        self.tour_children_ages = repositories.TourChildrenAgesRepository(self.session, model=models.TourChildrenAge)
        self.tour_activity_levels = repositories.TourActivityLevelsRepository(self.session, model=models.TourActivityLevel)
        self.tours = repositories.ToursRepository(self.session, model=models.Tour)
        self.tour_media_group = repositories.TourMediaGroupRepository(self.session, model=models.TourMedia)
        self.tour_categories = repositories.TourCategoriesRepository(self.session, model=models.TourCategory)
        self.tour_additional_types = repositories.TourAdditionalTypesRepository(self.session, model=models.TourAdditionalType)
        self.tour_languages = repositories.TourLanguagesRepository(self.session, model=models.TourLanguage)
        self.tour_activities = repositories.TourActivitiesRepository(self.session, model=models.TourActivity)
        self.tour_accommodations = repositories.TourAccommodationsRepository(self.session, model=models.TourAccommodation)
        self.tour_countries = repositories.TourCountriesRepository(self.session, model=models.TourCountry)
        self.tour_regions = repositories.TourRegionsRepository(self.session, model=models.TourRegion)
        self.tour_prices = repositories.TourPricesRepository(self.session, model=models.TourPrice)


        self.tour_comments = repositories.TourCommentsRepository(self.session, model=models.TourComment)
        self.tour_comments_media = repositories.TourCommentsMediaRepository(self.session, model=models.TourCommentMedia)

        self.blogs = repositories.BlogsRepository(self.session, model=models.Blog)
        self.blog_media =  repositories.BlogMediaRepository(self.session, model=models.BlogMedia)
        self.blog_countries = repositories.BlogCountriesRepository(self.session, model=models.BlogCountry)

        self.support_questions = repositories.SupportQuestionsRepository(self.session, model=models.SupportQuestion)
        self.question_docs = repositories.QuestionDocsRepository(self.session, model=models.QuestionDoc)

        self.sold_tours = repositories.SoldToursRepository(self.session, model=models.SoldTour)

        # self.tour_prices = TourPricesRepository(self.session, model=TourPrice)
        # self.tour_activities = TourActivitiesRepository(self.session, model=TourActivity)
        # self.favorite_tours = FavoriteToursRepository(self.session, model=FavoriteTours)
        # self.tour_comments = TourCommentsRepository(self.session, model=TourComment)
        # self.tour_comments_media = TourCommentsMediaRepository(self.session, model=TourCommentMedia)
        # self.ip_tour_view = IPTourViewRepository(self.session, model=IPTourView)
        # self.ip_and_tours_view = IPAndToursViewRepository(self.session, model=IPAndToursView)
        # self.languages = LanguagesRepository(self.session, model=Language)
        # self.tour_lagnuages = TourLanguagesRepository(self.session, model=TourLanguage)

    async def __aexit__(self, *args):
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
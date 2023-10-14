from models.mixins.tours import TourMixin
from models.base import BaseTable
from models.user_employees import UserEmployee
from models.users import User
from models.roles import Role
from models.emails import Email
from models.currencies import Currency
from models.activities import Activity
from models.languages import Language
from models.accommodations import Accommodation
from models.categories import Category
from models.types import Type
from models.countries import Country
from models.regions import Region
from models.accommodation_types import AccommodationType


from models.tour_statuses import TourStatus
from models.tour_children_ages import TourChildrenAge
from models.tour_activity_levels import TourActivityLevel
from models.tours import Tour
from models.tour_media_group import TourMedia
# from models.tour_categories import TourCategory
from models.tour_additional_types import TourAdditionalType
from models.tour_languages import TourLanguage
from models.tour_activities import TourActivity
from models.tour_accommodations import TourAccommodation
from models.tour_accommodation_types import TourAccommodationType
from models.tour_countries import TourCountry
from models.tour_regions import TourRegion
from models.tour_prices import TourPrice

from models.tour_days import TourDay, TourDayMediaGroup
from models.tour_hotels import TourHotel, TourHotelMediaGroup
from models.tour_imporants import TourImportant


from models.tour_comments import TourComment, TourCommentMedia

from models.blogs import Blog, BlogMedia
from models.blog_countries import BlogCountry

from models.support_questions import QuestionDoc, SupportQuestion

from models.sold_tours import SoldTour

from models.statistics_of_views import StatisticOfViews

# from models.tours import Tour, IPTourView, IPAndToursView
# from models.tourprices import TourPrice
# from models.tour_activities import TourActivity
# from models.favorite_tours import FavoriteTours
# from models.tour_comments import TourComment
# from models.tour_comments_media import TourCommentMedia
# from models.tour_languages import TourLanguage
from api.routers.auth import router as auth_router
from api.routers.users import router as users_router
from api.routers.roles import router as roles_router
from api.routers.user_employees import router as user_employees_router
from api.routers.emails import router as emails_router
from api.routers.currencies import router as currencies_router
from api.routers.activities import router as activities_router
from api.routers.languages import router as languages_router
from api.routers.accommodations import router as accommodations_router
from api.routers.categories import router as categories_router
from api.routers.types import router as types_router
from api.routers.countries import router as countries_router
from api.routers.regions import router as regions_router


from api.routers.tour_statuses import router as tour_statuses_router
from api.routers.tour_children_ages import router as tour_children_ages_router
from api.routers.tour_activity_levels import router as tour_activity_levels_router
from api.routers.tours import router as tours_router
from api.routers.tour_media_group import router as tour_media_group_router
from api.routers.tour_comments import router as tour_comments_router

from api.routers.blogs import router as blogs_router

from api.routers.support_questions import router as support_questions_router

from api.routers.sold_tours import router as sold_tours_router

from api.routers.statistics_of_views import router as statistics_of_views_router

# from api.routers.tours import router as tour_router
# from api.routers.tourprices import router as tour_prices_router
# from api.routers.tour_activities import router as tour_activities_router
# from api.routers.favorite_tours import router as tour_favorites_router
# from api.routers.tour_comments import router as tour_comments_router
# from api.routers.tour_comments_media import router as tour_comments_media_router
# from api.routers.tour_languages import router as tour_languages_router
all_routers = [
    auth_router,
    users_router,
    roles_router,
    user_employees_router,
    emails_router,
    currencies_router,
    activities_router,
    languages_router,
    accommodations_router,
    categories_router,
    types_router,
    countries_router,
    regions_router,


    tour_statuses_router,
    tour_children_ages_router,
    tour_activity_levels_router,
    tours_router,
    tour_media_group_router,
    tour_comments_router,

    blogs_router,

    support_questions_router,

    sold_tours_router,

    statistics_of_views_router,
    # maillist_router,
    # roles_router,
    # travelermanagers_router,
    # currency_router,
    # languages_router,
    # tour_router,
    # tour_prices_router,
    # tour_activities_router,
    # tour_favorites_router,
    # tour_comments_router,
    # tour_comments_media_router,
    # statuses_router,
    # activities_router,
    # tour_languages_router
]
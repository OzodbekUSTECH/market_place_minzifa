from schemas.tours import CreateTourSchema
from schemas.tour_media_group import CreateTourMediaSchema
from schemas.tour_hotels import CreateTourHotelMediaGroup, CreateTourHotelSchema
from schemas.countries import CreateCountrySchema
from schemas.regions import CreateRegionSchema
from schemas.types import CreateTypeSchema
from schemas.tours import CreateTourSchema
from schemas.tour_days import CreateTourDaySchema, CreateTourDayMediaGroup
from schemas.tour_hotels import CreateTourHotelSchema, CreateTourHotelMediaGroup
from schemas.tours_package.includes import CreateIncludeInPriceSchema
from schemas.tours_package.excludes import CreateExcludeInPriceSchema
from schemas.tour_importants import CreateTourImportantSchema
from utils.locale_handler import LocaleHandler
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models
from utils.media_handler import MediaHandler
from json_data.parser.parse_handler import ParseHandler
from services import tours_service

class ParsersService:
    ...

    async def parse_countries_and_regions(self):
        uow = UnitOfWork()
        async with uow:
            countries = ParseHandler.get_countries()
            for country in countries:
                filename = None
                if country["photo"]:
                    photo_obj = ParseHandler.countries_media_url + country["photo"]
                    filename = await MediaHandler.save_media_from_url([photo_obj], MediaHandler.countries_media_dir)
                name = {
                    "ru": country["name"],
                    "en": country["name"],
                }
                title = {
                    "ru": country["title"],
                    "en": country["title"],
                }
                description = {
                    "ru": country["description"],
                    "en": country["description"],
                }
                meta_description = {
                    "ru": country["metadescription"],
                    "en": country["metadescription"],
                }
                country_dict = CreateCountrySchema(
                    name = name,
                    title=title,
                    description=description,
                    meta_description=meta_description,
                    filename=filename
                ).model_dump()
                created_country = await uow.countries.create(country_dict)
                regions = ParseHandler.get_regions_by_country_id(country["id"])
                if regions:
                    regions_data = []
                
                    for region in regions:
                        region_name = {
                            "ru": region["name"],
                            "en": region["name"],
                        }
                        region_description = {
                            "ru": region["body"],
                            "en": region["body"],
                        }
                        region_meta_description = {
                            "ru": region["metadescription"],
                            "en": region["metadescription"],
                        }


                        region_dict = CreateRegionSchema(
                            name=region_name,
                            country_id=created_country.id,
                            description=region_description,
                            meta_description=region_meta_description
                        ).model_dump()
                        regions_data.append(region_dict)
                    await uow.regions.bulk_create(regions_data)
                
            await uow.commit()

    async def parse_types(self):
        uow = UnitOfWork()
        async with uow:
            types = ParseHandler.get_types()
            for type in types:
                name = {
                    "ru": type["name"],
                    "en": type["name"]
                }
                description = {
                    "ru": type["description"],
                    "en": type["description"]
                }
                meta_description = {
                    "ru": type["metadescription"],
                    "en": type["metadescription"]

                }
                filename = None
                if type["photo_name"]:
                    photo_obj = ParseHandler.types_media_url + type["photo_name"] + "." + type["photo_ext"]
                    filename = await MediaHandler.save_media_from_url(photo_obj, MediaHandler.types_media_dir)

                type_dict = CreateTypeSchema(
                    name=name,
                    filename=filename,
                    description=description,
                    meta_description=meta_description
                ).model_dump()
                await uow.types.create(type_dict)

            await uow.commit()

    async def parse_tours(self):
        uow = UnitOfWork()
        async with uow:
            tours = ParseHandler.get_tours()
            for tour in tours:
                
                title = {
                    "ru": tour["name"],
                    "en": tour["name"],
                }
                description = {
                    "ru": tour["body"],
                    "en": tour["body"],
                }
                country_ids = []
                tour_country = ParseHandler.get_country_by_tour_id(tour["id"])
                if tour_country:
                    country = ParseHandler.get_country_by_id(tour_country["country_id"])
                    our_country_id: models.Country = await uow.countries.get_one_by(name={"ru": country["name"], "en": country["name"]})
                    country_ids.append(our_country_id.id)
                
                regions_ids = []

                tour_regions = ParseHandler.get_tour_regions_by_tour_id(tour["id"])
                if tour_regions:
                    for tour_region in tour_regions:
                        region = ParseHandler.get_region_by_id(tour_region["cityid"])
                        our_region: models.Region = await uow.regions.get_one_by(name={"ru": region["name"], "en": region["name"]})
                        regions_ids.append(our_region.id)


                
                tour_data = CreateTourSchema(
                    title=title,
                    description=description,
                    user_id = 2,
                    status_id = 1,
                    map_link = tour["map"],
                    age_group_from=8,
                    age_group_to=100,
                    children_age_id=1,
                    activity_level_id=1,
                    start_date=tour.get("start_date", None),
                    end_date=tour.get("end_date", None),
                    total_places = tour["travellers"],
                    free_places=tour["travellers"],
                    is_guaranteed=True,
                    category_id=1,
                    main_type_id=5,
                    is_allowed_individually=True,
                    additional_type_ids=None,
                    language_ids=[1],
                    activity_ids=None,
                    accommodation_ids=None,
                    country_ids=country_ids,
                    region_ids = regions_ids,
                    currency_id=2,
                    price = tour["solo_price"],
                    discount_percentage=None,
                    new_price=None,
                    discount_start_date=None,
                    discount_end_date=None,
                )
                
                created_tour: models.Tour = await tours_service.create_tour(uow, tour_data)

                
                tour_photos = ParseHandler.get_tour_photos(tour["id"])
                if tour_photos:
                    data_photos = []
                    for tour_photo in tour_photos:
                        photo_obj = ParseHandler.tours_media_url + tour_photo["photo"] + "." + tour_photo["photoext"]
                        filename = await MediaHandler.save_media_from_url(photo_obj, MediaHandler.tours_media_dir)
                        if filename:
                            tour_photo_dict = CreateTourMediaSchema(
                                tour_id=created_tour.id,
                                filename=filename
                            ).model_dump()
                            data_photos.append(tour_photo_dict)
                        
                    await uow.tour_media_group.bulk_create(data_photos)

            await uow.commit()

    async def parse_tour_days(self):
        uow = UnitOfWork()
        async with uow:
            tours = ParseHandler.get_tours()
            for tour in tours:
                our_tour = await uow.tours.get_one_by(title={"en": tour["name"], "ru": tour["name"]})
                tour_days = ParseHandler.get_tour_days_by_tour_id(tour["id"])
                if tour_days:
                    for tour_day in tour_days:
                        name = {
                            "ru": tour_day["name"],
                            "en": tour_day["name"]
                        }
                        description = {
                            "ru": tour_day["body"],
                            "en": tour_day["body"],
                        }
                        day_dict = CreateTourDaySchema(
                            tour_id=our_tour.id,
                            day=tour_day["day"],
                            name=name,
                            description=description,
                            region_id=None,
                        ).model_dump()
                        created_day: models.TourDay = await uow.tour_days.create(day_dict)
                        day_photos = ParseHandler.get_day_photos_by_day_id(tour_day["id"])
                        if day_photos:
                            data_photo_list = []
                            for day_photo in day_photos:
                                photo_obj = ParseHandler.days_media_url + day_photo["foto"] + "." + day_photo["fotoext"]
                                filename = await MediaHandler.save_media_from_url(photo_obj, MediaHandler.tour_days_media_dir)
                                day_photo_dict = CreateTourDayMediaGroup(
                                    tour_day_id=created_day.id,
                                    filename=filename
                                ).model_dump()
                                data_photo_list.append(day_photo_dict)
                            await uow.tour_day_media_groups.bulk_create(data_photo_list)

            await uow.commit()

    async def parse_hotels(self):
        uow = UnitOfWork()
        async with uow:
            tours = ParseHandler.get_tours()
            for tour in tours:
                our_tour = await uow.tours.get_one_by(title={"en": tour["name"], "ru": tour["name"]})
                tour_hotels = ParseHandler.get_tour_hotels_by_tour_id(tour["id"])
                if tour_hotels:
                    for tour_hotel in tour_hotels:
                        hotel_data = ParseHandler.get_hotel_by_id(tour_hotel["hotelid"])

                        name = {
                            "en": hotel_data["name"],
                            "ru": hotel_data["name"]
                        }
                        description = {
                            "en": hotel_data["body"],
                            "ru": hotel_data["body"]
                        }
                        hotel_dict = CreateTourHotelSchema(
                            tour_id=our_tour.id,
                            name=name,
                            description=description,
                            stars=None
                        ).model_dump()
                        created_hotel = await uow.tour_hotels.create(hotel_dict)
                        hotel_photos = ParseHandler.get_hotel_photos_by_hotel_id(hotel_data["id"])
                        if hotel_photos:
                            hotel_photo_list = []
                            for hotel_photo in hotel_photos:
                                photo_obj = ParseHandler.hotels_media_url + hotel_photo["photo"]
                                
                                filename = await MediaHandler.save_media_from_url(photo_obj, MediaHandler.tour_hotels_media_dir)
                                if filename:
                                    hotel_photo_dict = CreateTourHotelMediaGroup(
                                        tour_hotel_id=created_hotel.id,
                                        filename=filename
                                    ).model_dump()
                                    hotel_photo_list.append(hotel_photo_dict)
                            if hotel_photo_list:
                                await uow.tour_hotel_media_groups.bulk_create(hotel_photo_list)

                        await uow.commit()

    async def parse_includes_and_excludes(self):
        uow = UnitOfWork()
        async with uow:
            tours = ParseHandler.get_not_fixed_tours()
            for tour in tours:
                our_tour = await uow.tours.get_one_by(title={"en": tour["name"], "ru": tour["name"]})
                includes = tour.get("include", None)
                if includes:
                    include_data_list = []
                    for include in includes:
                        if include.isdigit():
                            data_instance = ParseHandler.get_service_by_id(include)
                            if data_instance:
                                name = {
                                    "ru": data_instance["title"],
                                    "en": data_instance["title"]
                                }
                                include_dict = CreateIncludeInPriceSchema(
                                    tour_id=our_tour.id,
                                    name=name
                                ).model_dump()
                                include_data_list.append(include_dict)
                    if include_data_list:
                        await uow.tour_includes.bulk_create(include_data_list)

                excludes = tour.get("exclude", None)
                if excludes:
                    exclude_data_list = []
                    for exclude in excludes:
                        if exclude.isdigit():
                            data_instance = ParseHandler.get_service_by_id(exclude)
                            if data_instance:
                                name = {
                                    "ru": data_instance["title"],
                                    "en": data_instance["title"]
                                }
                                exlude_dict = CreateExcludeInPriceSchema(
                                    tour_id=our_tour.id,
                                    name=name
                                ).model_dump()
                                exclude_data_list.append(exlude_dict)
                    if exclude_data_list:
                        await uow.tour_excludes.bulk_create(exclude_data_list)

            await uow.commit()

    async def parse_importants(self):
        uow = UnitOfWork()
        async with uow:
            tours = ParseHandler.get_tours()
            for tour in tours:
                our_tour = await uow.tours.get_one_by(title={"en": tour["name"], "ru": tour["name"]})
                tour_importants = ParseHandler.get_tour_imporants_by_tour_id(tour["id"])
                if tour_importants:
                    importants_data_list = []
                    for tour_important in tour_importants:
                        data_instance = ParseHandler.get_important_by_id(tour_important["faqid"])
                        if data_instance:
                            question = {
                                "ru": data_instance["name"],
                                "en":data_instance["name"]
                            }
                            answer = {
                                "ru": data_instance["description"],
                                "en": data_instance["description"]
                            }
                            important_dict = CreateTourImportantSchema(
                                tour_id=our_tour.id,
                                question=question,
                                answer=answer
                            ).model_dump()
                            importants_data_list.append(important_dict)

                    if importants_data_list:
                        await uow.tour_importants.bulk_create(importants_data_list)


            await uow.commit()


                            

    



            
    

parser_service = ParsersService()
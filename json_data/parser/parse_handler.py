import json


class ParseHandler:
    types_media_url = "https://turi-uzbekistana.ru/images/tourtypes/"
    hotels_media_url = "https://turi-uzbekistana.ru/images/hotel/"
    tours_media_url = "https://turi-uzbekistana.ru/images/tour/"
    days_media_url = "https://turi-uzbekistana.ru/images/day/"
    countries_media_url = "https://turi-uzbekistana.ru/images/country/"

    main = "./json_data/"

    tours = "t_tour_fixed.json"
    tour_photos = "t_tourfoto.json"
    tour_prices = "t_tour_day_price.json"

    tour_countries = "t_tour_country.json"
    tour_cities = "t_tourcity.json"
    
    tour_days = "t_tour_day.json"
    tour_day_photos = "t_tourdayfoto.json"

    tour_hotels = "t_tourhotel.json"

    not_fixed_tours = "t_tour.json"
    in_excludes = "t_tour_services.json"





    countries  = "t_country.json"
    cities = "t_city.json"
    hotels = "t_hotel.json"
    hotel_photos = "t_hotel_photo.json"

    types = "t_tour_type.json"

    tour_imporants = "t_tour_faqs.json"
    importants = "t_faq.json"



    @staticmethod
    def parse_json_file(file_name):
        try:
            file_name = ParseHandler.main + file_name
            with open(file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"Файл {file_name} не найден.")
            return None
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {file_name}.")
            return None
        
    @staticmethod
    def get_tours():
        tours = ParseHandler.parse_json_file(ParseHandler.tours)
        return tours
    
    @staticmethod
    def get_tour_photos(tour_id: str):
        tour_photos = ParseHandler.parse_json_file(ParseHandler.tour_photos)
        one_tour_photos = list(filter(lambda item: item["tourid"] == tour_id, tour_photos))
        return one_tour_photos
    
    
    @staticmethod
    def get_types():
        types = ParseHandler.parse_json_file(ParseHandler.types)
        return types
    
   


    @staticmethod
    def get_countries():
        countries = ParseHandler.parse_json_file(ParseHandler.countries)
        return countries
    
    @staticmethod
    def get_regions_by_country_id(country_id:str):
        regions = ParseHandler.parse_json_file(ParseHandler.cities)
        regions_of_country = list(filter(lambda region: region["country_id"] == country_id, regions))
        return regions_of_country
    
    @staticmethod
    def get_country_by_tour_id(tour_id:str):
        tours_countries = ParseHandler.parse_json_file(ParseHandler.tour_countries)
        tour_country = list(filter(lambda item: item["tour_id"] == tour_id, tours_countries))
        if tour_country:
            return tour_country[0]

    @staticmethod
    def get_country_by_id(id:str):
        countries = ParseHandler.parse_json_file(ParseHandler.countries)
        filtered_country = list(filter(lambda country: country["id"] == id, countries))
        return filtered_country[0]
    
    @staticmethod
    def get_tour_regions_by_tour_id(tour_id:str):
        tours_regions = ParseHandler.parse_json_file(ParseHandler.tour_cities)
        filtered_regions = list(filter(lambda region: region["tourid"] == tour_id, tours_regions))
        return filtered_regions
    
    @staticmethod
    def get_region_by_id(id:str):
        regions = ParseHandler.parse_json_file(ParseHandler.cities)
        filtered_region = list(filter(lambda item: item["id"] == id, regions))
        return filtered_region[0]
    
    @staticmethod
    def get_tour_days_by_tour_id(tour_id:str):
        days = ParseHandler.parse_json_file(ParseHandler.tour_days)
        filtered_days = list(filter(lambda item: item["tourid"] == tour_id, days))
        return filtered_days
    
    @staticmethod
    def get_day_photos_by_day_id(day_id: str):
        photos = ParseHandler.parse_json_file(ParseHandler.tour_day_photos)
        filtered_photos = list(filter(lambda item: item["day_id"] == day_id, photos))
        return filtered_photos
    
    @staticmethod
    def get_tour_hotels_by_tour_id(tour_id:str):
        hotels = ParseHandler.parse_json_file(ParseHandler.tour_hotels)
        tour_hotels = list(filter(lambda item: item["tourid"] == tour_id, hotels))
        return tour_hotels
    
    @staticmethod
    def get_hotel_by_id(id: str):
        hotels = ParseHandler.parse_json_file(ParseHandler.hotels)
        hotel = list(filter(lambda item: item["id"] == id, hotels))
        return hotel[0]
    
    @staticmethod
    def get_hotel_photos_by_hotel_id(hotel_id: str):
        photos = ParseHandler.parse_json_file(ParseHandler.hotel_photos)
        hotel_photos = list(filter(lambda item: item["hotelid"] == hotel_id, photos))
        return hotel_photos[:3]
    

    @staticmethod
    def get_not_fixed_tours():
        tours = ParseHandler.parse_json_file(ParseHandler.not_fixed_tours)
        return tours
    
    @staticmethod
    def get_service_by_id(id: str):
        services = ParseHandler.parse_json_file(ParseHandler.in_excludes)
        fitlered_service = list(filter(lambda item: item["id"] == id, services))
        if fitlered_service:
            return fitlered_service[0]
        
    
    @staticmethod
    def get_tour_imporants_by_tour_id(tour_id: str):
        imporants = ParseHandler.parse_json_file(ParseHandler.tour_imporants)
        tour_imporants = list(filter(lambda item: item["tourid"] == tour_id, imporants))
        return tour_imporants
    
    @staticmethod
    def get_important_by_id(id: str):
        imporants = ParseHandler.parse_json_file(ParseHandler.importants)
        important = list(filter(lambda item: item["id"] == id, imporants))
        if important:
            return important[0] 
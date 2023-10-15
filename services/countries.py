from schemas.countries import CreateCountrySchema, UpdateCountrySchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
from utils.media_handler import MediaHandler
import models


class CountriesService:
    

    async def create_country(self, uow: UnitOfWork, country_data: CreateCountrySchema) -> models.Country:
        country_dict = country_data.model_dump()
        filename = await MediaHandler.save_media(country_data.filename, MediaHandler.countries_media_dir)
        country_dict["filename"] = filename
        async with uow:
            country = await uow.countries.create(country_dict)
            await uow.commit()
            return country
        
    async def get_list_of_countries(self, uow: UnitOfWork,) -> list[models.Country]:
        async with uow:
            return await uow.countries.get_all()
        
    async def get_country_by_id(self, uow: UnitOfWork, id: int) -> models.Country:
        async with uow:
            return await uow.countries.get_by_id(id)
        
    async def update_country(self, uow: UnitOfWork, id: int, country_data: UpdateCountrySchema) -> models.Country:
        country_dict = country_data.model_dump(exclude={"filename"})
        if country_data.filename:
            filename = await MediaHandler.save_media(country_data.filename, MediaHandler.countries_media_dir)
            country_dict["filename"] = filename
        async with uow:
            country = await uow.countries.update(id, country_dict)
            await uow.commit()
            return country
        
    async def delete_country(self, uow: UnitOfWork, id: int) -> models.Country:
        async with uow:
            country = await uow.countries.delete(id)
            await uow.commit()
            return country
        
    async def parse_all_countries(self, uow: UnitOfWork):
        async with uow:
            countries = [
                {"ru": "Алжир", "en": "Algeria"},
                {"ru": "Андорра", "en": "Andorra"},
                {"ru": "Албания", "en": "Albania"},
                {"ru": "Афганистан", "en": "Afghanistan"},
                {"ru": "Ангола", "en": "Angola"},
                {"ru": "Ангилья", "en": "Anguilla"},
                {"ru": "Антарктида", "en": "Antarctica"},
                {"ru": "Антигуа и Барбуда", "en": "Antigua and Barbuda"},
                {"ru": "Аргентина", "en": "Argentina"},
                {"ru": "Армения", "en": "Armenia"},
                {"ru": "Аруба", "en": "Aruba"},
                {"ru": "Австралия", "en": "Australia"},
                {"ru": "Австрия", "en": "Austria"},
                {"ru": "Азербайджан", "en": "Azerbaijan"},
                {"ru": "Багамы", "en": "Bahamas"},
                {"ru": "Бахрейн", "en": "Bahrain"},
                {"ru": "Бангладеш", "en": "Bangladesh"},
                {"ru": "Барбадос", "en": "Barbados"},
                {"ru": "Беларусь", "en": "Belarus"},
                {"ru": "Бельгия", "en": "Belgium"},
                {"ru": "Белиз", "en": "Belize"},
                {"ru": "Бенин", "en": "Benin"},
                {"ru": "Бермуды", "en": "Bermuda"},
                {"ru": "Бутан", "en": "Bhutan"},
                {"ru": "Боливия", "en": "Bolivia"},
                {"ru": "Босния и Герцеговина", "en": "Bosnia and Herzegovina"},
                {"ru": "Ботсвана", "en": "Botswana"},
                {"ru": "Бразилия", "en": "Brazil"},
                {"ru": "Британская территория в Индийском океане", "en": "British Indian Ocean Territory"},
                {"ru": "Бруней", "en": "Brunei Darussalam"},
                {"ru": "Болгария", "en": "Bulgaria"},
                {"ru": "Буркина-Фасо", "en": "Burkina Faso"},
                {"ru": "Бурунди", "en": "Burundi"},
                {"ru": "Камбоджа", "en": "Cambodia"},
                {"ru": "Камерун", "en": "Cameroon"},
                {"ru": "Канада", "en": "Canada"},
                {"ru": "Кабо-Верде", "en": "Cape Verde"},
                {"ru": "Каймановы острова", "en": "Cayman Islands"},
                {"ru": "Центральноафриканская Республика", "en": "Central African Republic"},
                {"ru": "Чад", "en": "Chad"},
                {"ru": "Чили", "en": "Chile"},
                {"ru": "Китай", "en": "China"},
                {"ru": "Колумбия", "en": "Colombia"},
                {"ru": "Коморские острова", "en": "Comoros"},
                {"ru": "Конго", "en": "Congo"},
                {"ru": "Конго, Демократическая Республика", "en": "Congo, Democratic Republic of the"},
                {"ru": "Кука острова", "en": "Cook Islands"},
                {"ru": "Коста-Рика", "en": "Costa Rica"},
                {"ru": "Хорватия", "en": "Croatia"},
                {"ru": "Куба", "en": "Cuba"},
                {"ru": "Кипр", "en": "Cyprus"},
                {"ru": "Чехия", "en": "Czech Republic"},
                {"ru": "Дания", "en": "Denmark"},
                {"ru": "Джибути", "en": "Djibouti"},
                {"ru": "Доминика", "en": "Dominica"},
                {"ru": "Доминиканская Республика", "en": "Dominican Republic"},
                {"ru": "Эквадор", "en": "Ecuador"},
                {"ru": "Египет", "en": "Egypt"},
                {"ru": "Эль Сальвадор", "en": "El Salvador"},
                {"ru": "Экваториальная Гвинея", "en": "Equatorial Guinea"},
                {"ru": "Эритрея", "en": "Eritrea"},
                {"ru": "Эстония", "en": "Estonia"},
                {"ru": "Эфиопия", "en": "Ethiopia"},
                {"ru": "Фарерские острова", "en": "Faroe Islands"},
                {"ru": "Фиджи", "en": "Fiji"},
                {"ru": "Финляндия", "en": "Finland"},
                {"ru": "Франция", "en": "France"},
                {"ru": "Французская Гвиана", "en": "French Guiana"},
                {"ru": "Французская Полинезия", "en": "French Polynesia"},
                {"ru": "Габон", "en": "Gabon"},
                {"ru": "Гамбия", "en": "Gambia"},
                {"ru": "Грузия", "en": "Georgia"},
                {"ru": "Германия", "en": "Germany"},
                {"ru": "Гана", "en": "Ghana"},
                {"ru": "Гибралтар", "en": "Gibraltar"},
                {"ru": "Греция", "en": "Greece"},
                {"ru": "Гренландия", "en": "Greenland"},
                {"ru": "Гренада", "en": "Grenada"},
                {"ru": "Гваделупа", "en": "Guadeloupe"},
                {"ru": "Гуам", "en": "Guam"},
                {"ru": "Гватемала", "en": "Guatemala"},
                {"ru": "Гвинея", "en": "Guinea"},
                {"ru": "Гвинея-Бисау", "en": "Guinea-Bissau"},
                {"ru": "Гайана", "en": "Guyana"},
                {"ru": "Гаити", "en": "Haiti"},
                {"ru": "Гондурас", "en": "Honduras"},
                {"ru": "Гонконг", "en": "Hong Kong"},
                {"ru": "Венгрия", "en": "Hungary"},
                {"ru": "Исландия", "en": "Iceland"},
                {"ru": "Индия", "en": "India"},
                {"ru": "Индонезия", "en": "Indonesia"},
                {"ru": "Иран", "en": "Iran, Islamic Republic of"},
                {"ru": "Ирак", "en": "Iraq"},
                {"ru": "Ирландия", "en": "Ireland"},
                {"ru": "Израиль", "en": "Israel"},
                {"ru": "Италия", "en": "Italy"},
                {"ru": "Кот д'Ивуар", "en": "Côte d'Ivoire"},
                {"ru": "Ямайка", "en": "Jamaica"},
                {"ru": "Япония", "en": "Japan"},
                {"ru": "Иордания", "en": "Jordan"},
                {"ru": "Казахстан", "en": "Kazakhstan"},
                {"ru": "Кения", "en": "Kenya"},
                {"ru": "Кирибати", "en": "Kiribati"},
                {"ru": "Корейская Народно-Демократическая Республика", "en": "Korea, Democratic People's Republic of"},
                {"ru": "Корейская Республика", "en": "Korea, Republic of"},
                {"ru": "Кувейт", "en": "Kuwait"},
                {"ru": "Киргизия", "en": "Kyrgyzstan"},
                {"ru": "Лаос", "en": "Lao People's Democratic Republic"},
                {"ru": "Латвия", "en": "Latvia"},
                {"ru": "Ливан", "en": "Lebanon"},
                {"ru": "Лесото", "en": "Lesotho"},
                {"ru": "Либерия", "en": "Liberia"},
                {"ru": "Ливийская Арабская Джамахирия", "en": "Libyan Arab Jamahiriya"},
                {"ru": "Лихтенштейн", "en": "Liechtenstein"},
                {"ru": "Литва", "en": "Lithuania"},
                {"ru": "Люксембург", "en": "Luxembourg"},
                {"ru": "Макао", "en": "Macao"},
                {"ru": "Македония, бывшая Югославская Республика", "en": "Macedonia, the former Yugoslav Republic of"},
                {"ru": "Мадагаскар", "en": "Madagascar"},
                {"ru": "Малави", "en": "Malawi"},
                {"ru": "Малайзия", "en": "Malaysia"},
                {"ru": "Мальдивы", "en": "Maldives"},
                {"ru": "Мали", "en": "Mali"},
                {"ru": "Мальта", "en": "Malta"},
                {"ru": "Маршалловы острова", "en": "Marshall Islands"},
                {"ru": "Мартиника", "en": "Martinique"},
                {"ru": "Мавритания", "en": "Mauritania"},
                {"ru": "Маврикий", "en": "Mauritius"},
                {"ru": "Майотта", "en": "Mayotte"},
                {"ru": "Мексика", "en": "Mexico"},
                {"ru": "Микронезия, Федеративные Штаты", "en": "Micronesia, Federated States of"},
                {"ru": "Молдова", "en": "Moldova, Republic of"},
                {"ru": "Монако", "en": "Monaco"},
                {"ru": "Монголия", "en": "Mongolia"},
                {"ru": "Монтсеррат", "en": "Montserrat"},
                {"ru": "Марокко", "en": "Morocco"},
                {"ru": "Мозамбик", "en": "Mozambique"},
                {"ru": "Мьянма", "en": "Myanmar"},
                {"ru": "Намибия", "en": "Namibia"},
                {"ru": "Науру", "en": "Nauru"},
                {"ru": "Непал", "en": "Nepal"},
                {"ru": "Нидерланды", "en": "Netherlands"},
                {"ru": "Нидерландские Антильские острова", "en": "Netherlands Antilles"},
                {"ru": "Новая Каледония", "en": "New Caledonia"},
                {"ru": "Новая Зеландия", "en": "New Zealand"},
                {"ru": "Никарагуа", "en": "Nicaragua"},
                {"ru": "Нигер", "en": "Niger"},
                {"ru": "Нигерия", "en": "Nigeria"},
                {"ru": "Ниуэ", "en": "Niue"},
                {"ru": "Норфолк остров", "en": "Norfolk Island"},
                {"ru": "Северные Марианские острова", "en": "Northern Mariana Islands"},
                {"ru": "Норвегия", "en": "Norway"},
                {"ru": "Оман", "en": "Oman"},
                {"ru": "Пакистан", "en": "Pakistan"},
                {"ru": "Палау", "en": "Palau"},
                {"ru": "Палестинская территория, оккупированная", "en": "Palestinian Territory, Occupied"},
                {"ru": "Панама", "en": "Panama"},
                {"ru": "Папуа-Новая Гвинея", "en": "Papua New Guinea"},
                {"ru": "Парагвай", "en": "Paraguay"},
                {"ru": "Перу", "en": "Peru"},
                {"ru": "Филиппины", "en": "Philippines"},
                {"ru": "Питкэрн", "en": "Pitcairn"},
                {"ru": "Польша", "en": "Poland"},
                {"ru": "Португалия", "en": "Portugal"},
                {"ru": "Пуэрто-Рико", "en": "Puerto Rico"},
                {"ru": "Катар", "en": "Qatar"},
                {"ru": "Реюньон", "en": "Réunion"},
                {"ru": "Румыния", "en": "Romania"},
                {"ru": "Россия", "en": "Russia"},
                {"ru": "Руанда", "en": "Rwanda"},
                {"ru": "Сент-Китс и Невис", "en": "Saint Kitts and Nevis"},
                {"ru": "Сент-Люсия", "en": "Saint Lucia"},
                {"ru": "Сент-Пьер и Микелон", "en": "Saint Pierre and Miquelon"},
                {"ru": "Сент-Винсент и Гренадины", "en": "Saint Vincent and the Grenadines"},
                {"ru": "Самоа", "en": "Samoa"},
                {"ru": "Сан-Марино", "en": "San Marino"},
                {"ru": "Сан-Томе и Принсипи", "en": "Sao Tome and Principe"},
                {"ru": "Саудовская Аравия", "en": "Saudi Arabia"},
                {"ru": "Сенегал", "en": "Senegal"},
                {"ru": "Сербия и Черногория", "en": "Serbia and Montenegro"},
                {"ru": "Сейшелы", "en": "Seychelles"},
                {"ru": "Сьерра-Леоне", "en": "Sierra Leone"},
                {"ru": "Сингапур", "en": "Singapore"},
                {"ru": "Словакия", "en": "Slovakia"},
                {"ru": "Словения", "en": "Slovenia"},
                {"ru": "Соломоновы острова", "en": "Solomon Islands"},
                {"ru": "Сомали", "en": "Somalia"},
                {"ru": "Южная Африка", "en": "South Africa"},
                {"ru": "Южная Джорджия и Южные Сандвичевы острова", "en": "South Georgia and the South Sandwich Islands"},
                {"ru": "Испания", "en": "Spain"},
                {"ru": "Шри-Ланка", "en": "Sri Lanka"},
                {"ru": "Судан", "en": "Sudan"},
                {"ru": "Суринам", "en": "Suriname"},
                {"ru": "Свазиленд", "en": "Swaziland"},
                {"ru": "Швеция", "en": "Sweden"},
                {"ru": "Швейцария", "en": "Switzerland"},
                {"ru": "Сирийская Арабская Республика", "en": "Syrian Arab Republic"},
                {"ru": "Тайвань, провинция Китая", "en": "Taiwan, Province of China"},
                {"ru": "Таджикистан", "en": "Tajikistan"},
                {"ru": "Танзания, Объединенная Республика", "en": "Tanzania, United Republic of"},
                {"ru": "Таиланд", "en": "Thailand"},
                {"ru": "Тимор-Лесте", "en": "Timor-Leste"},
                {"ru": "Того", "en": "Togo"},
                {"ru": "Токелау", "en": "Tokelau"},
                {"ru": "Тонга", "en": "Tonga"},
                {"ru": "Тринидад и Тобаго", "en": "Trinidad and Tobago"},
                {"ru": "Тунис", "en": "Tunisia"},
                {"ru": "Турция", "en": "Turkey"},
                {"ru": "Туркменистан", "en": "Turkmenistan"},
                {"ru": "Теркс и Кайкос", "en": "Turks and Caicos Islands"},
                {"ru": "Тувалу", "en": "Tuvalu"},
                {"ru": "Уганда", "en": "Uganda"},
                {"ru": "Украина", "en": "Ukraine"},
                {"ru": "Объединенные Арабские Эмираты", "en": "United Arab Emirates"},
                {"ru": "Великобритания", "en": "United Kingdom"},
                {"ru": "Соединенные Штаты", "en": "United States"},
                {"ru": "Малые Тихоокеанские отдаленные острова Соединенных Штатов", "en": "United States Minor Outlying Islands"},
                {"ru": "Уругвай", "en": "Uruguay"},
                {"ru": "Узбекистан", "en": "Uzbekistan"},
                {"ru": "Вануату", "en": "Vanuatu"},
                {"ru": "Венесуэла", "en": "Venezuela"},
                {"ru": "Вьетнам", "en": "Vietnam"},
                {"ru": "Виргинские острова, Британские", "en": "Virgin Islands, British"},
                {"ru": "Виргинские острова, США", "en": "Virgin Islands, U.S."},
                {"ru": "Уоллис и Футуна", "en": "Wallis and Futuna"},
                {"ru": "Западная Сахара", "en": "Western Sahara"},
                {"ru": "Йемен", "en": "Yemen"},
                {"ru": "Замбия", "en": "Zambia"},
                {"ru": "Зимбабве", "en": "Zimbabwe"}
            ]
            for country in countries:
                c_dict = {
                    "name": country
                }
                await uow.countries.create(c_dict)    

            await uow.commit()

    

        
countries_service = CountriesService()
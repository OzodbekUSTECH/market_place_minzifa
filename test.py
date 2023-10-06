import pycountry
import json

regions = {}

for country in pycountry.countries:
    country_name = country.name
    country_alpha2 = country.alpha_2

    # Получаем регионы для страны, если они доступны
    try:
        subdivisions = pycountry.subdivisions.get(country_code=country_alpha2)
        region_list = [{"ru": sub.name, "en": sub.name} for sub in subdivisions]
        regions[country_name] = region_list
    except KeyError:
        # Если регионы для страны не доступны, пропускаем ее
        pass

# Сохраняем результат в JSON файл
with open('regions.json', 'w', encoding='utf-8') as json_file:
    json.dump(regions, json_file, ensure_ascii=False, indent=4)

# Пример вывода регионов для России
print(regions["Russia"])

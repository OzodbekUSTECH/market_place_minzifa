# # import json
# # from datetime import datetime

# # # Открываем исходный файл t_tour_fixed.json для чтения
# # with open("t_tour_fixed.json", "r", encoding="utf-8") as file:
# #     tour_data = json.load(file)

# # # Открываем файл t_tour_day_price.json для чтения
# # with open("./json_data/t_tour_day_price.json", "r", encoding="utf-8") as file:
# #     tour_day_data = json.load(file)

# # # Создаем словарь, в котором ключи - это tour_id, а значения - это соответствующие даты начала и окончания
# # tour_dates = {}

# # # Проходим по всем объектам в t_tour_day_price.json и находим даты начала и окончания для каждого tour_id
# # for day_obj in tour_day_data:
# #     tour_id = day_obj.get("tourid")
# #     date_start = day_obj.get("date_start")
# #     date_end = day_obj.get("date_end")

# #     if tour_id in tour_dates:
# #         # Если ключ (tour_id) уже существует, обновляем значение (дату окончания)
# #         tour_dates[tour_id]["end_date"] = date_end
# #     else:
# #         # Если ключ (tour_id) новый, создаем новую запись с датой начала
# #         tour_dates[tour_id] = {"start_date": date_start, "end_date": date_end}

# # # Обновляем каждый tour объект в tour_data с соответствующими датами начала и окончания
# # for tour_obj in tour_data:
# #     tour_id = tour_obj.get("id")
# #     dates = tour_dates.get(tour_id)

# #     if dates:
# #         # Изменяем формат даты
# #         start_date = datetime.strptime(dates["start_date"], "%Y-%m-%d").strftime("%d.%m.%Y")
# #         end_date = datetime.strptime(dates["end_date"], "%Y-%m-%d").strftime("%d.%m.%Y")

# #         tour_obj["start_date"] = start_date
# #         tour_obj["end_date"] = end_date

# # # Перезаписываем обновленный файл t_tour_fixed.json
# # with open("t_tour_fixed.json", "w", encoding="utf-8") as file:
# #     json.dump(tour_data, file, ensure_ascii=False, indent=4)

# # print("Файл 't_tour_fixed.json' был успешно перезаписан с обновленными датами начала и окончания.")

# import asyncio

# from services import parser_service

# asyncio.run(parser_service.parse_importants())

# # import json

# # # Открываем исходный файл t_tour_day.json для чтения
# # with open("./json_data/t_tourday.json", "r", encoding="utf-8") as file:
# #     t_tour_day_data = json.load(file)

# # # Создаем словарь, который будет содержать информацию о текущем номере дня для каждого tourid
# # day_count = {}

# # # Обновляем данные с правильной нумерацией дней
# # for item in t_tour_day_data:
# #     tour_id = item.get("tourid")

# #     # Получаем текущий номер дня для данного tourid
# #     current_day = day_count.get(tour_id, 1)

# #     # Добавляем ключ "day" с текущим номером дня
# #     item["day"] = current_day

# #     # Увеличиваем номер дня для данного tourid
# #     day_count[tour_id] = current_day + 1

# # # Сохраняем обновленные данные в виде массива с запятыми между объектами
# # with open("t_tour_day.json", "w", encoding="utf-8") as file:
# #     json.dump(t_tour_day_data, file, ensure_ascii=False, indent=4)

# # print("Файл 't_tour_day.json' был успешно переписан с правильной нумерацией дней и в виде массива с запятыми между объектами.")

import asyncio
from services import parser_service

asyncio.run(parser_service.set_tour_leader_for_all_tours())
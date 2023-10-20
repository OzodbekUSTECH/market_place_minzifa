from fastapi import UploadFile
import os
from config import settings
from typing import Union
import requests

def generate_filename(base_name, extension, counter, directory):
    new_filename = f"{base_name}_{counter}{extension}"
    generated_name = directory + new_filename

    if os.path.exists(generated_name):
        return generate_filename(base_name, extension, counter + 1, directory)
    
    return generated_name

class MediaHandler:
    media_dir = f"./{settings.media_filename}/"
    tour_comments_media_dir = settings.tour_comments_media_dir
    tours_media_dir = settings.tours_media_dir
    blogs_media_dir = settings.blogs_media_dir
    countries_media_dir = settings.countries_media_dir
    tour_days_media_dir = settings.tour_days_media_dir
    tour_hotels_media_dir = settings.tour_hotels_media_dir
    types_media_dir = settings.types_media_dir


    @staticmethod
    async def save_media(
        media: Union[list[UploadFile], UploadFile],
        directory: str,
    ) -> Union[list[str], str]:
        directory = MediaHandler.media_dir + directory

        if isinstance(media, list):
            # Если передан список файлов (media_group), обработаем его аналогично save_media_group.
            filenames = []
            for item in media:
                media_name = item.filename
                base_name, extension = os.path.splitext(media_name)
                generated_name = generate_filename(base_name, extension, 1, directory)                
                
                file_content = await item.read()
                with open(generated_name, 'wb') as media_file:
                    media_file.write(file_content)
                media_file.close()
                filename = generated_name[len(directory):] 
                filenames.append(filename)
            
            return filenames
        else:
            # Если передан одиночный файл (media), обработаем его аналогично update_media.
            media_name = media.filename
            base_name, extension = os.path.splitext(media_name)
            generated_name = generate_filename(base_name, extension, 1, directory)                
            
            file_content = await media.read()
            with open(generated_name, 'wb') as media_file:
                media_file.write(file_content)
            media_file.close()
            filename = generated_name[len(directory):] 

            return filename

        
    @staticmethod
    async def save_media_from_url(photo_objs, directory):
        saved_filenames = []
        directory = MediaHandler.media_dir + directory
        

        if isinstance(photo_objs, str):
            # Если передан только один URL, обернуть его в список
            photo_objs = [photo_objs]

        for photo_obj in photo_objs:
            url = photo_obj

            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                # Обработать ошибку и продолжить цикл
                print(f"Ошибка при получении медиафайла из URL: {str(e)}")
                continue  # Пропустить текущий URL и продолжить с следующим

            media_name = os.path.basename(url)
            base_name, extension = os.path.splitext(media_name)
            generated_name = generate_filename(base_name, extension, 1, directory)

            with open(generated_name, 'wb') as media_file:
                media_file.write(response.content)

            saved_filenames.append(os.path.basename(generated_name))

        # if len(saved_filenames) == 1:
            # Если сохранено только одно изображение, вернуть его имя, а не список
        if saved_filenames:
            return saved_filenames[0]
        # else:
        #     return saved_filenames
        
        


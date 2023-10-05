from fastapi import UploadFile
import os
from config import settings
from typing import Union

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

        
        
        


from fastapi import UploadFile, File, HTTPException, status, Request

import os


def generate_filename(base_name, extension, counter):
    new_filename = f"{base_name}_{counter}{extension}"
    generated_name = MediaHandler.comment_photos_dir + new_filename

    if os.path.exists(generated_name):
        return generate_filename(base_name, extension, counter + 1)
    
    return generated_name

class MediaHandler:
    media_url = "https://minzifatravel.ru"
    comment_photos_dir = "./static/"
    ALLOWED_PHOTO_CONTENT_TYPES = ["image/jpeg", "image/png"]
    @staticmethod
    async def save_media(
        media_group: list[UploadFile],
    ) -> list:
        urls = []
        for media in media_group:
            if media.content_type not in MediaHandler.ALLOWED_PHOTO_CONTENT_TYPES:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid file format. Only photos (JPEG/PNG)  are allowed.")
            media_name = media.filename
            base_name, extension = os.path.splitext(media_name)
            #recursive func
            generated_name = generate_filename(base_name, extension, 1)                
            
            file_content = await media.read()
            with open(generated_name, 'wb') as media:
                media.write(file_content)
            media.close()
            url = MediaHandler.media_url + generated_name[1:]
            urls.append(url)
        return urls
    
    @staticmethod
    async def update_media(
        photo: UploadFile,
    ):
        if photo.content_type not in MediaHandler.ALLOWED_PHOTO_CONTENT_TYPES:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid file format. Only photo (JPEG/PNG)  is allowed.")
        photo_name = photo.filename
        base_name, extension = os.path.splitext(photo_name)
        #recursive func
        generated_name = generate_filename(base_name, extension, 1)                
        
        file_content = await photo.read()
        with open(generated_name, 'wb') as photo:
            photo.write(file_content)
        photo.close()
        photo_url = MediaHandler.media_url + generated_name[1:]

        return photo_url
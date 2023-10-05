from schemas.blogs import CreateBlogSchema, UpdateBlogSchema, CreateBlogMediaSchema
from schemas.blog_countries import CreateBlogCountrySchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models
from utils.media_handler import MediaHandler
from fastapi import UploadFile

class BlogsService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_blog(self, blog_data: CreateBlogSchema) -> models.Blog:
        blog_dict = blog_data.model_dump()
        filenames = await MediaHandler.save_media(blog_data.media, MediaHandler.blogs_media_dir)
        async with self.uow:
            blog: models.Blog = await self.uow.blogs.create(blog_dict)
            await self.uow.blog_media.bulk_create(
                data_list=[CreateBlogMediaSchema(
                    blog_id=blog.id,
                    filename=filename
                ).model_dump() for filename in filenames]
            )

            await self.uow.blog_countries.bulk_create(
                data_list=[CreateBlogCountrySchema(
                    blog_id=blog.id,
                    country_id=country_id
                ).model_dump() for country_id in blog_data.country_ids]
            )
            await self.uow.commit()
            return blog
        
    async def create_media(self, id: int, media: list[UploadFile]) -> None:
        filenames = await MediaHandler.save_media(media, MediaHandler.blogs_media_dir)
        async with self.uow:
            blog: models.Blog = await self.uow.blogs.get_by_id(id)
            if not blog:
                raise CustomExceptions.not_found("Blog id not found")
             
            await self.uow.blog_media.bulk_create(
                data_list=[CreateBlogMediaSchema(
                    blog_id=blog.id,
                    filename=filename
                ).model_dump() for filename in filenames]
            )
        
    async def get_list_of_blogs(self) -> list[models.Blog]:
        async with self.uow:
            return await self.uow.blogs.get_all()

    async def get_blog_by_id(self, id: int) -> models.Blog:
        async with self.uow:
            blog: models.Blog = await self.uow.blogs.get_by_id(id)
            await blog.increase_view_count()
            await self.uow.commit()
            return blog
    
    async def _update_items(
        self, 
        current_items: set[int], 
        new_items: set[int], 
        add_item_func: callable, 
        remove_item_func: callable, 
    ):
        items_to_add = new_items - current_items
        items_to_remove = current_items - new_items
        
        for item_id in items_to_add:
            await add_item_func(item_id)
        
        for item_id in items_to_remove:
            await remove_item_func(item_id)


    async def update_blog(self, id: int, blog_data: UpdateBlogSchema) -> models.Blog:
        async with self.uow:
            existing_blog: models.Blog = await self.uow.blogs.get_by_id(id)
            if not existing_blog:
                raise CustomExceptions.not_found("Blog id not found")
            
            await self._update_items(
                set(existing_blog.country_ids), 
                set(blog_data.country_ids), 
                lambda country_id: self.uow.blog_countries.create(
                    CreateBlogCountrySchema(
                        blog_id=existing_blog.id,
                        country_id=country_id
                    ).model_dump()
                ),
                lambda country_id: self.uow.blog_countries.delete_by(
                    blog_id=existing_blog.id,
                    country_id = country_id
                )
            )


            blog_dict = blog_data.model_dump()

            blog = await self.uow.blogs.update(id, blog_dict)
            await self.uow.commit()
            return blog        

    async def delete_blog(self, id: int) -> models.Blog:
        async with self.uow:
            blog = await self.uow.blogs.delete(id)
            await self.uow.commit()
            return blog
        
    async def delete_media(self, id: int) -> models.BlogMedia:
        async with self.uow:
            blog_media = await self.uow.blog_media.delete(id)
            await self.uow.commit()
            return blog_media
        
blogs_service = BlogsService()
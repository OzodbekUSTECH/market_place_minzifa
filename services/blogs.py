from schemas.blogs import CreateBlogSchema, UpdateBlogSchema, CreateBlogMediaSchema
from schemas.blog_countries import CreateBlogCountrySchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
import models
from utils.media_handler import MediaHandler
from fastapi import UploadFile

class BlogsService:
    

    async def create_blog(self, uow: UnitOfWork, blog_data: CreateBlogSchema) -> models.Blog:
        blog_dict = blog_data.model_dump()
        filenames = await MediaHandler.save_media(blog_data.media, MediaHandler.blogs_media_dir)
        async with uow:
            blog: models.Blog = await uow.blogs.create(blog_dict)
            await uow.blog_media.bulk_create(
                data_list=[CreateBlogMediaSchema(
                    blog_id=blog.id,
                    filename=filename
                ).model_dump() for filename in filenames]
            )

            await uow.blog_countries.bulk_create(
                data_list=[CreateBlogCountrySchema(
                    blog_id=blog.id,
                    country_id=country_id
                ).model_dump() for country_id in blog_data.country_ids]
            )
            await uow.commit()
            return blog
        
    async def create_media(self, uow: UnitOfWork, id: int, media: list[UploadFile]) -> None:
        filenames = await MediaHandler.save_media(media, MediaHandler.blogs_media_dir)
        async with uow:
            blog: models.Blog = await uow.blogs.get_by_id(id)
            if not blog:
                raise CustomExceptions.not_found("Blog id not found")
             
            await uow.blog_media.bulk_create(
                data_list=[CreateBlogMediaSchema(
                    blog_id=blog.id,
                    filename=filename
                ).model_dump() for filename in filenames]
            )
        
    async def get_list_of_blogs(self, uow: UnitOfWork) -> list[models.Blog]:
        async with uow:
            return await uow.blogs.get_all()

    async def get_blog_by_id(self, uow: UnitOfWork, id: int) -> models.Blog:
        async with uow:
            blog: models.Blog = await uow.blogs.get_by_id(id)
            await blog.increase_view_count()
            await uow.commit()
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


    async def update_blog(self, uow: UnitOfWork, id: int, blog_data: UpdateBlogSchema) -> models.Blog:
        async with uow:
            existing_blog: models.Blog = await uow.blogs.get_by_id(id)
            if not existing_blog:
                raise CustomExceptions.not_found("Blog id not found")
            
            await self._update_items(
                set(existing_blog.country_ids), 
                set(blog_data.country_ids), 
                lambda country_id: uow.blog_countries.create(
                    CreateBlogCountrySchema(
                        blog_id=existing_blog.id,
                        country_id=country_id
                    ).model_dump()
                ),
                lambda country_id: uow.blog_countries.delete_by(
                    blog_id=existing_blog.id,
                    country_id = country_id
                )
            )


            blog_dict = blog_data.model_dump()

            blog = await uow.blogs.update(id, blog_dict)
            await uow.commit()
            return blog        

    async def delete_blog(self, uow: UnitOfWork, id: int) -> models.Blog:
        async with uow:
            blog = await uow.blogs.delete(id)
            await uow.commit()
            return blog
        
    async def delete_media(self, uow: UnitOfWork, id: int) -> models.BlogMedia:
        async with uow:
            blog_media = await uow.blog_media.delete(id)
            await uow.commit()
            return blog_media
        
blogs_service = BlogsService()
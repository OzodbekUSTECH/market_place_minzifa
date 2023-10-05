from schemas import CreateBaseModel

class CreateBlogCountrySchema(CreateBaseModel):
    blog_id: int
    country_id: int
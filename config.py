from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict




class DbSettings(BaseModel):
    alembic_url: str = f"postgresql+asyncpg://postgres:77girado@165.232.118.125:5432/postgres"
        


class Settings(BaseSettings):
    MEDIA_URL: str
    DB_HOST: str
    DB_PORT:str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    ECHO: bool

    
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str

    REDIS_URL: str

    RESET_LINK: str

    @property
    def DATABASE_URL(self): 
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}/{self.DB_NAME}"
    

    media_filename: str = "media"
    tour_comments_media_dir: str = "tour_comments/"
    tours_media_dir: str = "tours/"
    blogs_media_dir: str = "blogs/"
    countries_media_dir: str = "countries/"
    tour_days_media_dir: str = "tour_days/"
    tour_hotels_media_dir: str = "tour_hotels/"

    @property
    def TOURS_MEDIA_URL(self):
        return f"{settings.MEDIA_URL}{self.tours_media_dir}"
    
    @property
    def TOUR_COMMENTS_MEDIA_URL(self):
        return f"{settings.MEDIA_URL}{self.tour_comments_media_dir}"

    @property
    def BLOG_MEDIA_URL(self):
        return f"{settings.MEDIA_URL}{self.blogs_media_dir}"

    @property
    def COUNTRY_MEDIA_URL(self):
        return f"{settings.MEDIA_URL}{self.countries_media_dir}"
    
    @property
    def TOUR_DAY_MEDIA_URL(self):
        return f"{settings.MEDIA_URL}{self.tour_days_media_dir}"
    
    @property
    def TOUR_HOTEL_MEDIA_URL(self):
        return f"{settings.MEDIA_URL}{self.tour_hotels_media_dir}"


    api_v1_prefix: str = "/v1"
    development: bool = False
    db: DbSettings = DbSettings()
    
    

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()




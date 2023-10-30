from functools import wraps
from typing import Callable
from typing import Union
from utils.exceptions import CustomExceptions
import models as md
from pydantic import BaseModel
class LocaleHandler:
    def __init__(self, locale: str):
        self.locale = locale

    @property
    def get_language(self) -> str:
        return self.locale    
    
    @staticmethod
    async def get_model_fields_by_locale(models: Union[list[BaseModel], BaseModel], locale):
        async def process_attribute(attr_value):
            # Process a single attribute (dictionary)
            if isinstance(attr_value, dict):
                localized_value = attr_value.get(locale.get_language, None)
                if localized_value is not None:
                    return localized_value
                else:
                    raise ValueError(f"Key not found for locale {locale.get_language}")

            # Process a list of dictionaries
            if isinstance(attr_value, list) and all(isinstance(item, dict) for item in attr_value):
                localized_values = [item.get(locale.get_language) for item in attr_value if item.get(locale.get_language)]
                return localized_values

            # Process a BaseModel
            if isinstance(attr_value, BaseModel) or isinstance(attr_value, md.BaseTable):
                for key, value in attr_value.__dict__.items():
                    if isinstance(value, dict):
                        localized_value = value.get(locale.get_language, None)
                        if localized_value is not None:
                            setattr(attr_value, key, localized_value)
                    elif isinstance(value, BaseModel) or isinstance(value, md.BaseTable):
                        for sub_key, sub_value in value.__dict__.items():
                            if isinstance(sub_value, dict):
                                sub_localized_value = sub_value.get(locale.get_language, None)
                                if sub_localized_value is not None:
                                    setattr(value, sub_key, sub_localized_value)
                    elif isinstance(value, list):
                        await process_attribute(value)

            # Process a list of models
            if isinstance(attr_value, list):
                for sub_model in attr_value:
                    if not isinstance(sub_model, int):
                        for sub_attr_name, sub_attr_value in sub_model.__dict__.items():
                            if isinstance(sub_attr_value, dict):
                                sub_localized_value = sub_attr_value.get(locale.get_language, None)
                                if sub_localized_value is not None:
                                    setattr(sub_model, sub_attr_name, sub_localized_value)
                            elif isinstance(sub_attr_value, BaseModel):
                                for sub_key, sub_value in sub_attr_value.__dict__.items():
                                    if isinstance(sub_value, dict):
                                        sub_localized_value = sub_value.get(locale.get_language, None)
                                        if sub_localized_value is not None:
                                            setattr(sub_attr_value, sub_key, sub_localized_value)
            return attr_value


        # Ensure models is a list
        if not isinstance(models, list):
            models = [models]

        for model in models:
            if hasattr(model, 'items') and isinstance(model.items, list):
                for item in model.items:
                    for attr_name, attr_value in item.__dict__.items():
                        localized_value = await process_attribute(attr_value)
                        if localized_value is not None:
                            setattr(item, attr_name, localized_value)
            else:
                for attr_name, attr_value in model.__dict__.items():
                    print(attr_name)
                    localized_value = await process_attribute(attr_value)
                    if localized_value is not None:
                        setattr(model, attr_name, localized_value)
                    else:
                        if isinstance(attr_value, md.BaseTable):
                            for key, value in attr_value.__dict__.items():
                                localized_value = await process_attribute(value)
                                if localized_value is not None:
                                    setattr(attr_value, key, localized_value)


                            
    @staticmethod
    def serialize_one_all_models_by_locale(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            locale = kwargs.get('locale')  # Получаем locale из kwargs
            models = await func(*args, **kwargs)  # Передаем locale в декорируемую функцию
            try:
                await LocaleHandler.get_model_fields_by_locale(models, locale)
            except:
                raise CustomExceptions.conflict("Locale not found")
            return models

        return wrapper

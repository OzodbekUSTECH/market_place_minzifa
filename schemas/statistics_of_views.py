from schemas import  CreateBaseModel, UpdateBaseModel, IdResponseSchema
from typing import Union

class CreateStatisticView(CreateBaseModel):
    date: str
    




class StatisticOfViewsSchema(IdResponseSchema, CreateStatisticView):
    pass
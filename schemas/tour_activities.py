from schemas import CreateBaseModel, TourMixinBaseModel

class CreateTourActivitySchema(TourMixinBaseModel, CreateBaseModel):

    activity_id: int


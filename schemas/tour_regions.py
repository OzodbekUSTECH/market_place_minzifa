from schemas import CreateBaseModel, TourMixinBaseModel


class CreateTourRegionSchema(TourMixinBaseModel, CreateBaseModel):
    region_id: int

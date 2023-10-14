from models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSONB

################################
class AccommodationType(BaseTable):
    __tablename__ = 'accommodation_types'

    name: Mapped[dict] = mapped_column(JSONB)

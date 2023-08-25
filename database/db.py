from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
# DATABASE_URL = "postgresql://postgres:77girado@localhost:5432/marketplacedb"

#production
DATABASE_URL = "postgresql://postgres:77girado@db/postgres"

engine = create_engine(DATABASE_URL, echo=True)
session_maker = sessionmaker(bind=engine, autoflush=False)


Base = declarative_base()   


def get_db():
    db = session_maker()
    try:
        yield db
    finally:
        db.close()
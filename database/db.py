from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
# DATABASE_URL = "postgresql://postgres:77girado@db:5432/marketplacedb" develop

DATABASE_URL = "postgresql://postgres:77girado@db/postgres"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
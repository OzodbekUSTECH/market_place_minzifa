from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
# DATABASE_URL = "postgresql://postgres:77girado@localhost:5432/marketplacedb"

#production
DATABASE_URL = "postgresql://postgres:77girado@localhost:5432/postgres"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
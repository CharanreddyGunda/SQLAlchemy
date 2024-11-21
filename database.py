from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import settings

# DATABASE_URL = "postgresql://postgres:root@localhost:5433/postgres"

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#creates the tables in database
def create_db():
    Base.metadata.create_all(bind = engine)
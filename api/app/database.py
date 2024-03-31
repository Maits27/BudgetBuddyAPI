from os import environ
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Variables de entorno
POSTGRES_USER = environ['POSTGRES_USER']
POSTGRES_PASSWORD = environ['POSTGRES_PASSWORD']
POSTGRES_IP = environ['POSTGRES_IP']
POSTGRES_DB = environ['POSTGRES_DB']

# Configuración de la base de datos
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_IP}/{POSTGRES_DB}"
# SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:1234@postgres/budgetBuddyDB2"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
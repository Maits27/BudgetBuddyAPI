from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class User(Base):
    __tablename__ = "user"
    email = Column(String, primary_key=True, index=True)
    nombre = Column(String, index=True)
    password = Column(String)

class Gasto(Base):
    __tablename__ = "gasto"
    id = Column(String, primary_key=True, index=True)
    nombre = Column(String, index=True)
    cantidad = Column(Integer)
    fecha = Column(Integer)
    tipo = Column(String)
    userId = Column(Integer, ForeignKey("user.id"))
    
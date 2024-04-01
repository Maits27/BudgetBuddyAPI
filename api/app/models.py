
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    nombre = Column(String, primary_key=True, index=True)
    email = Column(String, index=True)
    password = Column(String)

    gastos = relationship("Gasto", back_populates="owner")

class Gasto(Base):
    __tablename__ = "gastos"
    nombre = Column(String, index=True)
    cantidad = Column(Float)
    fecha = Column(Integer)
    tipo = Column(String)
    userId = Column(String, ForeignKey("users.nombre"))
    id = Column(String, primary_key=True, index=True)

    owner = relationship("User", back_populates="gastos")
    
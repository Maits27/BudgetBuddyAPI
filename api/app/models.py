
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    nombre = Column(String, index=True)
    email = Column(String, primary_key=True, index=True)
    password = Column(String)

    gastos = relationship("Gasto", back_populates="user")

class Gasto(Base):
    __tablename__ = "gastos"
    nombre = Column(String, index=True)
    cantidad = Column(Float)
    fecha = Column(Integer)
    tipo = Column(String)
    user_id = Column(String, ForeignKey("users.email"))
    id = Column(String, primary_key=True, index=True)

    user = relationship("User", back_populates="gastos")
    
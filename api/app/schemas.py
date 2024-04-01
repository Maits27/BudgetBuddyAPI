from pydantic import BaseModel

class UserBase(BaseModel):
    nombre: str
    password: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    email: str
    
    class Config:
        orm_mode = True

class GastoBase(BaseModel):
    nombre: str
    cantidad: float
    fecha: int
    tipo: str

class GastoCreate(GastoBase):
    pass

class Gasto(GastoBase):
    userId: str
    id: str

    class Config:
        orm_mode = True


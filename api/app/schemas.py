from pydantic import BaseModel

class UserBase(BaseModel):
    nombre: str
    email: str
    password: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    
    class Config:
        orm_mode = True

class GastoBase(BaseModel):
    nombre: str
    cantidad: float
    fecha: int
    tipo: str
    latitud: float
    longitud: float
    user_id: str
    id: str

class GastoCreate(GastoBase):
    pass

class Gasto(GastoBase):

    class Config:
        orm_mode = True


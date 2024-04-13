from sqlalchemy.orm import Session
from .models import User, Gasto
from .schemas import UserCreate, GastoCreate
from typing import Optional

##################################################################################
##################################    USERS    ###################################
##################################################################################
def login_user(db: Session, email: str):
    db.query(User).filter(User.email == email).update({User.login: True})
    
def logout_user(db: Session, email: str):
    db.query(User).filter(User.email == email).update({User.login: False})

def is_user_logged(db: Session, email: str):
    user = db.query(User.login).filter(User.email == email).first()
    return user[0] if user else user


def get_user(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(email=user.email, nombre=user.nombre, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, email: str):
    db_user = db.query(User).filter(User.email == email).first()
    db.delete(db_user)
    db.commit()
    return db_user

def update_user(db: Session, email: str, user: UserCreate):
    db_user = db.query(User).filter(User.email == email).first()
    db_user.nombre = user.nombre
    if user.password !="":
        db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user

##################################    PERFIL    ##################################

def get_profile_image(db: Session, email: str) -> bool:
    result = db.query(User.profile_image).filter(User.email == email).first()
    return result.profile_image if result else result


def set_profile_image(db: Session, email: str, path: str) -> bool:
    if user := get_user(db, email):
        user.profile_image = path
        db.commit()
        db.refresh(user)
        return True
    return False

##################################################################################

##################################################################################
##################################    GASTOS    ##################################
##################################################################################

def get_gasto(db: Session, id: str):
    return db.query(Gasto).filter(Gasto.id == id).first()

def get_gastos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Gasto).offset(skip).limit(limit).all()

def create_gastos(db: Session, gastos: list[GastoCreate]):
    delete_all_gastos_by_user(db, gastos[0].user_id)
    db_gastos = [Gasto(
        id=gasto.id, 
        nombre=gasto.nombre, 
        cantidad=gasto.cantidad, 
        fecha=gasto.fecha, 
        tipo=gasto.tipo, 
        longitud=gasto.longitud,
        latitud=gasto.latitud,
        user_id=gasto.user_id
    ) for gasto in gastos]
    db.add_all(db_gastos)
    db.commit()
    return db_gastos

def create_gasto(db: Session, gasto: GastoCreate):
    db_gasto = Gasto(
        id=gasto.id, 
        nombre=gasto.nombre, 
        cantidad=gasto.cantidad, 
        fecha=gasto.fecha, 
        tipo=gasto.tipo, 
        longitud=gasto.longitud,
        latitud=gasto.latitud,
        user_id=gasto.user_id
    )
    db.add(db_gasto)
    db.commit()
    db.refresh(db_gasto)
    return db_gasto

def update_gasto(db: Session, id: str, gasto: GastoCreate):
    db_gasto = db.query(Gasto).filter(Gasto.id == id).first()
    db_gasto.nombre = gasto.nombre
    db_gasto.cantidad = gasto.cantidad
    db_gasto.fecha = gasto.fecha
    db_gasto.tipo = gasto.tipo
    db_gasto.longitud = gasto.longitud
    db_gasto.latitud = gasto.latitud
    db_gasto.user_id = gasto.user_id
    db.commit()
    db.refresh(db_gasto)
    return db_gasto

def delete_gasto(db: Session, id: str):
    db_gasto = db.query(Gasto).filter(Gasto.id == id).first()
    db.delete(db_gasto)
    db.commit()
    return db_gasto

def get_gastos_by_user(db: Session, user_id: Optional[str] = None, skip: int = 0, limit: int = 100):
    if user_id:
        return db.query(Gasto).filter(Gasto.user_id == user_id).offset(skip).limit(limit).all()
    else:
        return db.query(Gasto).offset(skip).limit(limit).all()

def delete_all_gastos_by_user(db: Session, user_id: str):
    db_gastos = db.query(Gasto).filter(Gasto.user_id == user_id).all()
    for gasto in db_gastos:
        db.delete(gasto)
    db.commit()
    return db_gastos
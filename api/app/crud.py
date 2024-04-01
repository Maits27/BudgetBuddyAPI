from sqlalchemy.orm import Session
from .models import User, Gasto
from .schemas import UserCreate, GastoCreate

##################################################################################
##################################    USERS    ###################################
##################################################################################

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
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user

##################################################################################
##################################    GASTOS    ##################################
##################################################################################

# def get_gasto(db: Session, id: str):
#     return db.query(Gasto).filter(Gasto.id == id).first()

def get_gastos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Gasto).offset(skip).limit(limit).all()

def create_gasto(db: Session, gasto: GastoCreate):
    db_gasto = Gasto(id=gasto.id, nombre=gasto.nombre, cantidad=gasto.cantidad, fecha=gasto.fecha, tipo=gasto.tipo, userId=gasto.userId)
    db.add(db_gasto)
    db.commit()
    db.refresh(db_gasto)
    return db_gasto

# def delete_gasto(db: Session, id: str):
#     db_gasto = db.query(Gasto).filter(Gasto.id == id).first()
#     db.delete(db_gasto)
#     db.commit()
#     return db_gasto

def get_gastos_by_user(db: Session, userId: str):
    return db.query(Gasto).filter(Gasto.userId == userId).all()

def delete_all_gastos_by_user(db: Session, userId: str):
    db_gastos = db.query(Gasto).filter(Gasto.userId == userId).all()
    for gasto in db_gastos:
        db.delete(gasto)
    db.commit()
    return db_gastos
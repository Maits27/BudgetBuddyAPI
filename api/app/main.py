from fastapi import FastAPI, Depends, HTTPException
from .database import get_db
from . import crud
from .schemas import *
from sqlalchemy.orm import Session

# Tutorial: https://www.youtube.com/watch?v=d_ugoWsvGLI
# Documentation: https://fastapi.tiangolo.com/tutorial/sql-databases/

##################################################################################
##################################    USERS    ###################################
##################################################################################

app = FastAPI()

# Rutas de la API
@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get('/users/', response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)

@app.get('/users/{email}', response_model=User)
def read_user(email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put('/users/{email}', response_model=User)
def update_user(email: str, user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db, email, user)

@app.delete('/users/{email}', response_model=User)
def delete_user(email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db, email)

##################################################################################
##################################    GASTOS    ##################################
##################################################################################

@app.post('{userid}/gastos/', response_model=list[Gasto])
def create_gasto(gasto: GastoCreate, db: Session = Depends(get_db)):
    return crud.create_gasto(db, gasto)

@app.get('{userid}/gastos/', response_model=list[Gasto])
def read_gastos_by_user(userId: str, db: Session = Depends(get_db)):
    return crud.get_gastos_by_user(db, userId)

@app.delete('{userid}/gastos/', response_model=list[Gasto])
def delete_all_gastos_by_user(userId: str, db: Session = Depends(get_db)):
    return crud.delete_all_gastos_by_user(db, userId)
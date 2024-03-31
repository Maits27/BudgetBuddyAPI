from fastapi import FastAPI, HTTPException, Depends
from .database import engine, get_db
from . import crud
from .schemas import *
from models import User, Gasto, Base
from sqlalchemy.orm import Session
from typing import List

# Tutorial: https://www.youtube.com/watch?v=d_ugoWsvGLI
# Documentation: https://fastapi.tiangolo.com/tutorial/sql-databases/

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def Home():
    return {"message": "BudgetBuddyAPI is running!"}

##################################################################################
##################################    USERS    ###################################
##################################################################################

@app.post('/users/', response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get('/users/', response_model=List[User])
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

@app.post('{userid}/gastos/', response_model=List[Gasto])
def create_gasto(gasto: GastoCreate, db: Session = Depends(get_db)):
    return crud.create_gasto(db, gasto)

@app.get('{userid}/gastos/', response_model=List[Gasto])
def read_gastos_by_user(userId: str, db: Session = Depends(get_db)):
    return crud.get_gastos_by_user(db, userId)

@app.delete('{userid}/gastos/', response_model=List[Gasto])
def delete_all_gastos_by_user(userId: str, db: Session = Depends(get_db)):
    return crud.delete_all_gastos_by_user(db, userId)
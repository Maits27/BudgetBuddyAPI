from os import environ
from fastapi import FastAPI, Depends, HTTPException, UploadFile, status
from fastapi.responses import FileResponse
from pathlib import Path
from mimetypes import guess_extension
from .database import get_db
from . import crud
from .models import User, Gasto
from .schemas import *
from sqlalchemy.orm import Session
import firebase_admin
from firebase_admin import credentials, messaging
from unidecode import unidecode
from typing import List

VALID_IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/webp']

# Tutorial: https://www.youtube.com/watch?v=d_ugoWsvGLI
# Documentation: https://fastapi.tiangolo.com/tutorial/sql-databases/

##################################################################################
##################################    USERS    ###################################
##################################################################################
cred = credentials.Certificate(environ['FIREBASE_CREDENTIALS'])
firebase_admin.initialize_app(cred)
app = FastAPI()

@app.post('/notifications/subscribe/', status_code=status.HTTP_202_ACCEPTED, tags=["Notifications"])
def suscribe_user_to_alert(token: FirebaseClientToken):
    # Procesamos el nombre de la provincia quitando espacios y tíldes y se suscribe al usuario
    messaging.subscribe_to_topic([token.fcm_client_token], 'all')
async def send_notification(message: Message, topic: str = 'all'):
    messaging.send(
        messaging.Message(
            data={k: f'{v}' for k, v in dict(message).items()},
            topic=unidecode(topic.replace(' ', '_'))
        )
    )

    messaging.send(
        messaging.Message(
            notification=messaging.Notification(
                **dict(message)
            ),
            topic=unidecode(topic.replace(' ', '_'))
        )
    )

@app.post("/notifications", tags=["Notifications"])
async def send_broadcast_notification(message: Message):
    await send_notification(message)

@app.get('/login/{email}', response_model=bool)
def login_user(email: str, db: Session = Depends(get_db)):
    logedUser = crud.is_user_logged(db, email)
    if logedUser:
        return logedUser
    else:
        return False

@app.post('/login/{email}', response_model=User)
def login_user(email: str, login:bool, db: Session = Depends(get_db)):
    if not (crud.get_user(db, email)):
        raise HTTPException(status_code=404, detail="User doesn't exist")
    if login==True: 
        crud.login_user(db, email)
    else: 
        crud.logout_user(db, email)
    return crud.get_user(db, email)

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

##################################    PERFIL    ##################################
@app.get('/profile/{email}', response_class=FileResponse)
def get_profile_image(email: str, db: Session = Depends(get_db)):
    if not (crud.get_user(db, email)):
        raise HTTPException(status_code=404, detail="User doesn't exist")
    image = crud.get_profile_image(db, email)
    if image!= None and Path(image).exists():
        return FileResponse(image, filename=Path(image).name)
    else:
        return FileResponse("/budgetbuddy_api/images/start_icon.png", filename="start_icon.png")

@app.put("/profile/{email}", tags=["Users"],
         status_code=status.HTTP_204_NO_CONTENT,
         responses={404: {"description": "User doesn't exists."}, 400: {"description": f"File is not a valid image file. Valid types: {', '.join(VALID_IMAGE_TYPES)}"}})
async def set_user_profile_image(file: UploadFile, email: str, db: Session = Depends(get_db)):
    if not (user := crud.get_user(db, email)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User doesn't exists.")

    if file.content_type not in VALID_IMAGE_TYPES:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"File is not a valid image file. Valid types: {', '.join(VALID_IMAGE_TYPES)}")

    file_extension = guess_extension(file.content_type)
    path = f'/budgetbuddy_api/images/{email}{file_extension}'

    if crud.set_profile_image(db, email, path):
        contents = await file.read()
        with open(path, 'wb') as f:
            f.write(contents)


##################################################################################

##################################################################################
##################################    GASTOS    ##################################
##################################################################################

@app.post('/gastos/{user_id}/', response_model=Gasto)
def create_gasto(gasto: GastoCreate, db: Session = Depends(get_db)):
    return crud.create_gasto(db, gasto)

@app.post('/gastos_upload/{user_id}/', response_model=Gasto)
def create_gastos(gastos: List[GastoCreate], db: Session = Depends(get_db)):
    delete_all_gastos_by_user(gastos[0].user_id, db)
    for gasto in gastos:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(gasto)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        gasto = crud.create_gasto(db, gasto)
    return gasto

@app.get('/gastos/{user_id}/', response_model=list[Gasto])
def read_gastos_by_user(user_id: str, db: Session = Depends(get_db)):
    return crud.get_gastos_by_user(db, user_id)

@app.delete('/gastos/{user_id}/', response_model=list[Gasto])
def delete_all_gastos_by_user(user_id: str, db: Session = Depends(get_db)):
    return crud.delete_all_gastos_by_user(db, user_id)

@app.get('/gastos/', response_model=list[Gasto])
def read_gastos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_gastos(db, skip, limit)
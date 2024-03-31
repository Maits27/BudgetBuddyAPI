from fastapi import FastAPI
import model 
from database import engine

# Tutorial: https://www.youtube.com/watch?v=d_ugoWsvGLI
# Documentation: https://fastapi.tiangolo.com/tutorial/sql-databases/

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def Home():
    return {"message": "Hello World"}
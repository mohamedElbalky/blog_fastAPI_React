from fastapi import FastAPI


from database import models
from database.db_settings import engine, get_db



app = FastAPI()

models.Base.metadata.create_all(engine)

@app.get('/')
def index():
    return {"message": "Hello World"}
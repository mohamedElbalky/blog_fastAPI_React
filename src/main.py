from fastapi import FastAPI


from database import models
from database.db_settings import engine

from routers import post


app = FastAPI()


# database
models.Base.metadata.create_all(engine)




# routers
app.include_router(post.router)




@app.get('/')
def index():
    """Index page"""
    return {"message": "Hello World"}


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

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


# mounts folder to display images on site [static files mount]
app.mount('/media/images', StaticFiles(directory='media/images'), name='images')


# add middleware to make front end run on local machine with backend without errors
# run site on two ports on localhost
origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
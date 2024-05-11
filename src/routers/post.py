import os
import uuid
import shutil

from fastapi import APIRouter, Depends, UploadFile, File

from sqlalchemy.orm.session import Session


from database.db_settings import get_db
from database.crud import post
from schemas.post import PostDisplay, PostBase

from utils import generate_path


router = APIRouter(
    prefix = "/posts",
    tags = ["posts"],
    responses = {404: {"description": "Not found"}},
    # dependencies = [],
    include_in_schema = True,
)


@router.get('')
def read_all_posts(db: Session = Depends(get_db)):
    """get all posts"""
    return post.all(db)
    

@router.post('')
def add_new_post(request: PostBase, db: Session = Depends(get_db)):
    """add a new post"""
    return post.create(db, request)

@router.delete('/{id}')
def delete_post(id: int, db: Session=Depends(get_db)):
    """delete a post"""
    return post.delete(id, db)



@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    """Upload an image to the Post"""
    path = generate_path(image)
    
    # save image
    with open(path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
        
    # add image url to a post
    # post.update_image(id, db, image_url=path)
    
    return {"filename": path}
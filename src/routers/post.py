from fastapi import APIRouter, Depends

from sqlalchemy.orm.session import Session


from database.db_settings import get_db
from database.crud import post
from schemas.post import PostDisplay, PostBase


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
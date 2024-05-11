
from datetime import datetime

from fastapi import HTTPException, status

from sqlalchemy.orm.session import Session
from schemas.post import PostBase
from ..models import DbPost




def create(db: Session, request: PostBase):
    """Add a new post to database."""
    post_db = DbPost(
        image = request.image_url,
        title = request.title,
        content = request.content,
        creator = request.creator,
        timestamp = datetime.now()
    )
    
    db.add(post_db)
    db.commit()
    db.refresh(post_db)
    
    return post_db


def all(db: Session):
    """Get all posts from database."""
    return db.query(DbPost).all()


def delete(id: int, db: Session):
    """Delete a post from database"""
    post_db = db.query(DbPost).filter(DbPost.id == id).first()
    if not post_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ({id}) not found")
    db.delete(post_db)
    db.commit()
    
    return {"message": "Post deleted successfully"}


# def read_one_post(id: int, db: Session):
#     post_db = db.query(DbPost).filter(DbPost.id == id).first()
#     if not post_db:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ({id}) not found")
#     return post_db

def update_image(id: int, db: Session, image_url: str):
    """add an image to the post"""
    post_db = db.query(DbPost).filter(DbPost.id == id).first()
    if not post_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with #id({id}) not found")
    
    post_db.image = image_url
    db.commit()
    # db.refresh(post_db)
    
    return True

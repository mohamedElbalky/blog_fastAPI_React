from datetime import datetime

from pydantic import BaseModel



class PostBase(BaseModel):
    title: str
    content: str
    creator: str
    image_url: str
    


class PostDisplay(PostBase):
    id : int
    timestamp: datetime
    
    class Config():
        from_attributes = True
        


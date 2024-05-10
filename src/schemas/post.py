from datetime import datetime

from pydantic import BaseModel



class PostBase(BaseModel):
    image_url: str
    title: str
    content: str
    creator: str
    

    
class PostDisplay(PostBase):
    id : int
    timestamp: datetime
    
    class Config():
        from_attributes = True
        


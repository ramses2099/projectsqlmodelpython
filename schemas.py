import datetime
from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
   username: str 
   hashed_password: str 
   
class UserCreate(UserBase):
    email: str 
    
class User(UserBase):
   id: int
   update_at: Optional[datetime.datetime]
   create_at: datetime.datetime
   
   class Config:
       from_attributes = True
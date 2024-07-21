import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel
 

# other models 
class User(SQLModel, table=True):
   id: Optional[int] = Field(default=None, primary_key=True)
   username:str = Field(unique = True, index=True)
   email: str = Field(unique = True, index=True)
   hashed_password:str  
   update_at: Optional[datetime.datetime]
   create_at: datetime.datetime = Field(default=datetime.datetime.now())
   

    
  

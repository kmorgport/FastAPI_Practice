from datetime import datetime
from distutils.util import strtobool
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional
    
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
class UserBase(BaseModel):
    email: EmailStr
    password: str
    
class UserCreate(UserBase):
    pass

class PostCreate(PostBase):
    pass

class User(BaseModel):
    id: int
    created_at: datetime
    #converts orm models into schemas
    class Config:
        orm_mode= True
        
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Post(BaseModel):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    #converts orm models into schemas
    class Config:
        orm_mode= True
        
class PostOut(PostBase):
    #value references other class
    Post: Post
    votes: int
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
    
from typing import List
from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from contextlib import asynccontextmanager
from db import *
from models import *
from schemas import *
import services

@asynccontextmanager
async def lifespan(app: FastAPI):
    # create tables
    init_db()   
    yield
   
   
# fastapi object
app = FastAPI(lifespan=lifespan)


# routers

@app.post("/signup", status_code=status.HTTP_201_CREATED)
async def create_user(user:UserCreate, db:Session = Depends(get_db)):
    db_user = await services.existing_user(db, user.username, user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="username or email already in use")
    db_user = await services.create_user(db, user)
    access_token = await services.create_access_token(db_user.id, db_user.username)
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": db_user.username,
    }


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = await services.authenticate(db, form_data.username, form_data.password)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="incorrect user and password")
    access_token = await services.create_access_token(db_user.id, db_user.username)
    return {
        "access_token": access_token,
        "token_type": "bearer"        
    }


@app.get("/profile", response_model = User)
async def get_current_user(token: str, db: Session = Depends(get_db)):
    db_user = await services.get_current_user(db, token)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="you are not authenticate")
    return db_user
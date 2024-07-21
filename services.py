from datetime import datetime, timedelta, UTC
from jose import jwt,JWTError
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from typing import Optional
from sqlmodel import Session, select
from models import User as UserModel
from schemas import User as UserSchema, UserCreate

SECRET_KEY = "myscretkey"
EXPIRE_MINUTES = 60 * 24 # 1 days
ALGORITHM = "HS256"

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")
bcrypt_context = CryptContext(schemes=["bcrypt"])


# check existing user with same username or email
async def existing_user(db: Session, username: str, email: str) -> Optional[UserModel]:
    statement = select(UserModel).where(UserModel.username == username)
    db_user = db.exec(statement).one_or_none()
    if db_user:
        return db_user
    statement = select(UserModel).where(UserModel.email == email)
    db_user = db.exec(statement).one_or_none()
    if db_user:
        return db_user
    return None

# create token
# jwt = {"sub": username, "id": id}
async def create_access_token(id: int, username: str):
    encode = {"sub": username, "id": id}
    expires = datetime.now(UTC) + timedelta(minutes=EXPIRE_MINUTES)
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


# get current user from token
async def get_current_user(db: Session, token: str = Depends(oauth2_bearer)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        id: int = payload.get("id")
        expries = payload.get("exp")
        # if expries < datetime.now(UTC):
        #     return None
        if username is None or id is None:
           return None
        statement = select(UserModel).where(UserModel.username == username)
        db_user = db.exec(statement).one_or_none()
        return db_user        
    except JWTError:
        return None


# create user
async def create_user(db: Session, user: UserCreate):
    db_user = UserModel(
        username = user.username,
        email = user.email,
        hashed_password= bcrypt_context.hash(user.hashed_password)
    )
    db.add(db_user)
    db.commit()
    return db_user

# authenticate
async def authenticate(db: Session, username: str, password: str) -> Optional[UserModel]:
    statement = select(UserModel).where(UserModel.username == username)
    db_user = db.exec(statement).one_or_none()
    if not db_user:
        return None
    if not bcrypt_context.verify(password, db_user.hashed_password):
        return None
    return db_user

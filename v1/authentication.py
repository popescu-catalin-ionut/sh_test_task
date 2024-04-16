from datetime import datetime, timedelta
from typing import Optional

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy import select

from common.settings import (
    SECRET_KEY,
    ALGORITHM,
)
from v1.models import Users, session

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$1AnY8Gg8LVabQ8TrBqg.k.BnMNl3yXOZAhkT3Yg1mRk4g2jdSU5Zi",
    }
}

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Function to get a user from the database
def get_user(username: str):
    query = select(Users).where(Users.username == username)
    result = session.execute(query)
    get_result_list = [dict(r._mapping) for r in result]
    if len(get_result_list) == 1:
        return get_result_list[0]['Users']


# Function to authenticate a user
def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not password == user.password:
        return False
    return user


# Create access token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# OAuth2 scheme with password flow
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

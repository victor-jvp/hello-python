from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer,  OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "3ae590732bccc0963937b4e6800bba8048854cde52768a8615796b8505a66117"

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "vveliz": {
        "username": "vveliz",
        "full_name": "Victor Veliz",
        "email": "vvelizp@gmail.com",
        "disabled": False,
        "password": "$2y$10$dTgAVnKxyq6K2w5RHoh9FO8EOIza1yPL5XIaZVSBXdnmZ1OqoxkHW"
    },
    "vveliz2": {
        "username": "vveliz2",
        "full_name": "Victor Veliz 2",
        "email": "vvelizp2@gmail.com",
        "disabled": True,
        "password": "$2y$10$Ry..fGaYlwNBuXi8bh.wpeWHLY5YAqEDniziScBvLDZO4l63SCojG"
    }
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticacion invalidas",
        headers={"WWW-Authenticate": "Bearer"})

    try:
        username = jwt.decode(token, SECRET, algorithms=ALGORITHM).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception

    return search_user(username)


async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    access_token = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)
    }

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user

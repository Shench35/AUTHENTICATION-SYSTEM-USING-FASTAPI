from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.setting import settings

password_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expire_delta: timedelta) -> str:
    dict_encode = data.copy()
    expire = datetime.utcnow() + (expire_delta if expire_delta else timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    dict_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(dict_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None
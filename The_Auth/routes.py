from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.database import Session
from app.schemas import UserCreate, UserLogin
from app.models import UserSchema
from app.setting import settings
from The_Auth.utils import hash_password, verify_password, create_access_token, decode_access_token
from datetime import timedelta


app = FastAPI()
security = HTTPBearer()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def greeting():
    return {"message": "Good Morning and win today"}

@app.post("/register/")
def register_user(user: UserCreate, db=Depends(get_db)):
    hash_pw = hash_password(user.password)
    user = UserSchema(
        username=user.username,
        email=user.email,
        password=hash_pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {
        "username": user.username,
        "email": user.email,                
        "password": user.password
    }

@app.post("/login/")
def login_user(user: UserLogin, db=Depends(get_db)):
    user_db = db.query(UserSchema).filter(UserSchema.username == user.username).first()
    if not user_db or not verify_password(user.password, user_db.password):
        raise HTTPException(status_code=404, detail="Inncorrect username or Password")
    
    expire_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token({"sub": user_db.username}, expire_delta)
    return {"access_token": access_token, "token_type": "bearer"}
    

@app.get("/protected/")
def protected_route(cred: HTTPAuthorizationCredentials = Depends(security)):
    if not cred:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing credentials")
    token = cred.credentials
    payload = decode_access_token(token)
    print(payload)
    if not payload:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid or expired token")
    return {"message": "Protected route accessed", "user": payload["sub"]}



from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
SECRET = "SECRET_KEY"
users_db = {"user@example.com": "password"}

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    if form.username in users_db and users_db[form.username] == form.password:
        token = jwt.encode({"sub": form.username, "exp": datetime.utcnow() + timedelta(hours=2)}, SECRET)
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(400, "Invalid credentials")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(401, "Invalid token")
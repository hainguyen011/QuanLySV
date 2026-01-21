from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from ..core.security import create_access_token, get_password_hash, verify_password
from ..core.config import settings
from ..db.mongodb import db
from ..models.user import User
from ..schemas.user import UserCreate, UserResponse, Token

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register(user_in: UserCreate):
    # Kiểm tra user tồn tại
    existing_user = await db.db.users.find_one({"username": user_in.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username đã tồn tại")
    
    user_dict = user_in.dict()
    user_dict["hashed_password"] = get_password_hash(user_dict.pop("password"))
    user_dict["role"] = "student"
    
    result = await db.db.users.insert_one(user_dict)
    user_dict["id"] = str(result.inserted_id)
    return user_dict

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await db.db.users.find_one({"username": form_data.username})
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Tài khoản hoặc mật khẩu không chính xác",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from .models import User
from dependencies import get_db
from .schema import UserCreate,UserLogin,Token

user_router=APIRouter()

@user_router.post('/signup')
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")

    user = User(username=user_data.username, email=user_data.email, phone_number=user_data.phone_number)
    user.hash_password(user_data.password)
    db.add(user)
    db.commit()
    return {"message": "User has been created"}

@user_router.post('/login')
def login(user_data:UserLogin,db:Session = Depends(get_db)):
    user=db.query(User).filter(User.email==user_data.email).first()
    if user is None or not user.verify_password(user_data.password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    token=user.generate_token()
    return Token(access_token=token,token_type='bearer')
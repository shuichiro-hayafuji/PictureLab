from fastapi import Depends, FastAPI, APIRouter
from sqlalchemy.orm import Session, sessionmaker
from pydantic import BaseModel
from app.server.database.database import SessionLocal

router = APIRouter()


class User(BaseModel): # データの定義
    id: int
    name: str
    password: str

def get_db(): # リクエスト時にSessionLocalを作成し完了したら終了する
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/users/") # すべてのuserを取得する
def read_users():
    db: Session = Depends(get_db)
    return db.query(User).all()

@router.get("/users/{user_id}")# 単一のuserを取得する
def read_users_only(user_id: int):
    db: Session = Depends(get_db)
    return db.query(User).filter(User.id == user_id).first()

@router.post("/users/") # userを登録する
async def create_user(user_create: User):
    db: Session = Depends(get_db)
    db.add(user_create)
    db.commit()
    return db.query(User).filter(User.id == user_create.id).first()

@router.put("/users/{user_id}") # userを更新する
async def update_user(user_id: int, user_create: User):
    db: Session = Depends(get_db)
    user = db.query(User).filter(User.id == user_id).first()
    user.title = user_create.title
    db.commit()
    return db.query(User).filter(User.id == user_id).first()

@router.delete("/users/{user_id}") # userを更新する
async def delete_user(user_id: int):
    db: Session = Depends(get_db)
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()

from fastapi import APIRouter
from crud import read_user

router = APIRouter()

@router.get("/users/") # すべてのuserを取得する
def read_users():
    return read_user.read_users()

@router.get("/users/{user_id}")# 単一のuserを取得する
def read_users_only(user_id: int):
    return read_user.read_users_only(user_id)

@router.post("/users/") # userを登録する
async def create_user(user_create: read_user.User):
    return read_user.create_user(user_create)

@router.put("/users/{user_id}") # userを更新する
async def update_user(user_id: int, user_create: read_user.User):
    return read_user.update_user(user_id, user_create)

@router.delete("/users/{user_id}") # userを更新する
async def delete_user(user_id: int):
    read_user.delete_user(user_id)

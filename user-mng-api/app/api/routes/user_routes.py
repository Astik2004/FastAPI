from fastapi import APIRouter
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository


router = APIRouter(prefix="/users", tags=["Users"])

repository = UserRepository()
service = UserService(repository)


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):

    return service.create_user(user)


@router.get("/", response_model=list[UserResponse])
def get_all_users():

    return service.get_all_users()


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):

    return service.get_user_by_id(user_id)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate):

    return service.update_user(user_id, user)


@router.delete("/{user_id}")
def delete_user(user_id: int):

    return service.delete_user(user_id)
from app.repositories.user_repository_interface import IUserRepository
from app.models.user_model import User
from app.exceptions.custom_exception import UserNotFoundException


class UserService:

    def __init__(self, repository: IUserRepository):

        self.repository = repository

    def create_user(self, user_data):

        users = self.repository.get_all_users()

        new_id = len(users) + 1

        user = User(
            id=new_id,
            name=user_data.name,
            email=user_data.email
        )

        return self.repository.create_user(user)

    def get_all_users(self):

        return self.repository.get_all_users()

    def get_user_by_id(self, user_id: int):

        user = self.repository.get_user_by_id(user_id)

        if not user:
            raise UserNotFoundException("User not found")

        return user

    def update_user(self, user_id: int, user_data):

        existing_user = self.repository.get_user_by_id(user_id)

        if not existing_user:
            raise UserNotFoundException("User not found")

        updated_user = User(
            id=user_id,
            name=user_data.name,
            email=user_data.email
        )

        return self.repository.update_user(user_id, updated_user)

    def delete_user(self, user_id: int):

        deleted = self.repository.delete_user(user_id)

        if not deleted:
            raise UserNotFoundException("User not found")

        return {
            "message": "User deleted successfully"
        }
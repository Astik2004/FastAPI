from app.repositories.user_repository_interface import IUserRepository
from app.database.fake_db import users_db
from app.models.user_model import User


class UserRepository(IUserRepository):

    def create_user(self, user: User):

        users_db.append(user)

        return user

    def get_all_users(self):

        return users_db

    def get_user_by_id(self, user_id: int):

        for user in users_db:

            if user.id == user_id:
                return user

        return None

    def update_user(self, user_id: int, updated_user: User):

        for index, user in enumerate(users_db):

            if user.id == user_id:

                users_db[index] = updated_user

                return updated_user

        return None

    def delete_user(self, user_id: int):

        for user in users_db:

            if user.id == user_id:

                users_db.remove(user)

                return True

        return False
from abc import ABC, abstractmethod


class IUserRepository(ABC):

    @abstractmethod
    def create_user(self, user):
        pass

    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int):
        pass

    @abstractmethod
    def update_user(self, user_id: int, user):
        pass

    @abstractmethod
    def delete_user(self, user_id: int):
        pass
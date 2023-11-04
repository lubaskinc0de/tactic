from clean_architecture_app.domain.entities.user import User
from clean_architecture_app.domain.entities.user_id import UserId


class UserService:
    def create_user(self, user_id: UserId) -> User:
        return User(user_id=user_id)

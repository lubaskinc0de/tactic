from clean_architecture_app.domain.entities.user import User
from clean_architecture_app.domain.value_objects.user import UserId


class UserService:
    def create_user(self, user_id: UserId) -> User:
        return User(user_id=user_id)

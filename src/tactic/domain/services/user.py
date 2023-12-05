from tactic.domain.entities.user import User
from tactic.domain.value_objects.user import UserId


class UserService:
    # you can do some business logic here, e.g. check the business rules of your app
    # but value validation logic should be in VO

    def create(self, user_id: UserId) -> User:
        return User(user_id=user_id)

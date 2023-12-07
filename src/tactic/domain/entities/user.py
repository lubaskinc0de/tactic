from dataclasses import dataclass

from tactic.domain.value_objects.user import UserId


@dataclass
class User:
    # your business user model
    # you can split it to DBUser (database user with database id) and User (domain business model of user without id)
    # if you need
    user_id: UserId

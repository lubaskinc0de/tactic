from dataclasses import dataclass

from tactic.domain.value_objects.user import UserId


@dataclass
class User:  # you can split it to DBUser if you have some business data in User entity.
    # your domain business entities
    user_id: UserId

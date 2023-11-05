from dataclasses import dataclass

from clean_architecture_app.domain.value_objects.user import UserId


@dataclass
class User:
    user_id: UserId

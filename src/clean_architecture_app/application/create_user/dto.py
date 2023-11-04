from dataclasses import dataclass

from clean_architecture_app.domain.entities.user_id import UserId


@dataclass
class NewUserDTO:
    user_id: UserId

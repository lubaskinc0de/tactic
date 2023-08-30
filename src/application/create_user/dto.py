from dataclasses import dataclass

from domain.entities.user_id import UserId


@dataclass
class NewUserDTO:
    user_id: UserId

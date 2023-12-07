from dataclasses import dataclass

from tactic.domain.common.value_objects.base import ValueObject


@dataclass(frozen=True)
class UserId(ValueObject[int]):
    value: int

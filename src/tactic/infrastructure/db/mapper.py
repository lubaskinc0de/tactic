from sqlalchemy.orm import relationship, registry

from tactic.domain.entities.user import User
from tactic.infrastructure.db.orm import user_table


def start_mapper() -> None:
    mapper_registry = registry()
    mapper_registry.map_imperatively(User, user_table)

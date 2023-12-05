from aiogram import Dispatcher
from aiogram.filters import Command

from .new_user.dialog import new_user_dialog
from .new_user.dialog import user_start


def register_handlers(dp: Dispatcher) -> None:
    """Register all client-side handlers"""

    dp.message.register(user_start, Command(commands="start"))


def register_dialogs(dp: Dispatcher) -> None:
    dp.include_router(new_user_dialog)


__all__ = [
    "register_handlers",
    "register_dialogs",
]

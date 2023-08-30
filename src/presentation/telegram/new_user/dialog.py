from aiogram.types import Message
from aiogram_dialog import Dialog, Window, DialogManager

from aiogram_dialog.widgets.text import Format

from application.create_user.dto import NewUserDTO
from domain.entities.user_id import UserId

from presentation.interactor_factory import InteractorFactory
from presentation.telegram import states


async def user_start(message: Message, ioc: InteractorFactory):
    async with ioc.create_user() as create_user:
        create_user(NewUserDTO(
            user_id=UserId(message.from_user.id),
        ))


async def user_getter(manager: DialogManager):
    return {
        "user_id": manager.event.from_user.id,
    }


new_user_dialog = Dialog(
    Window(
        Format(
            "Привет! Твой айди:\n{user_id}"
        ),
        getter=user_getter,
        state=states.NewUser.user_id,
    ),
)

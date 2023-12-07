from typing import Any

from aiogram.enums import ContentType
from aiogram.types import Message

from aiogram_dialog import Dialog, Window, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Toggle
from aiogram_dialog.widgets.media import StaticMedia

from aiogram_dialog.widgets.text import Format

from tactic.application.create_user import UserInputDTO, UserOutputDTO
from tactic.domain.value_objects.user import UserId

from tactic.presentation.interactor_factory import InteractorFactory
from tactic.presentation.telegram import states

OPTIONS_KEY = "options"


async def user_start(
    message: Message, ioc: InteractorFactory, dialog_manager: DialogManager
) -> None:
    async with ioc.create_user() as create_user:
        user_data: UserOutputDTO = await create_user(
            UserInputDTO(
                user_id=UserId(message.from_user.id),  # type:ignore
            )
        )

    await dialog_manager.start(
        states.NewUser.user_id,
        mode=StartMode.RESET_STACK,
        data={
            "user_id": user_data.user_id.to_raw(),
        },
    )


async def window_getter(
    dialog_manager: DialogManager, **_kwargs: dict[str, Any]
) -> dict[str, UserId | str | Any]:
    return {
        "user_id": dialog_manager.start_data.get("user_id"),
        OPTIONS_KEY: ["Пинг!", "Понг!"]
    }


new_user_dialog = Dialog(
    Window(
        StaticMedia(
            path="/app/src/tactic/presentation/telegram/assets/start.gif",
            type=ContentType.ANIMATION,
        ),
        Format("👋 Привет! Твой айди:\n> <b>{user_id}</b>"),
        Toggle(
            text=Format("{item}"),
            id="ping_pong",
            items=OPTIONS_KEY,
            item_id_getter=lambda item: item,
        ),
        getter=window_getter,
        state=states.NewUser.user_id,
    ),
)

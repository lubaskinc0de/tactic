from aiogram.enums import ContentType
from aiogram.types import Message, CallbackQuery

from aiogram_dialog import Dialog, Window, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.media import StaticMedia

from aiogram_dialog.widgets.text import Format

from clean_architecture_app.application.create_user.use_case import NewUserDTO
from clean_architecture_app.domain.value_objects.user import UserId

from clean_architecture_app.presentation.interactor_factory import InteractorFactory
from clean_architecture_app.presentation.telegram import states

DEFAULT_STATE = "Пинг!"
DEFAULT_STATE_KEY = "example_state"


async def user_start(
    message: Message, ioc: InteractorFactory, dialog_manager: DialogManager
):
    async with ioc.create_user() as create_user:
        user_id: UserId = await create_user(
            NewUserDTO(
                user_id=UserId(message.from_user.id),
            )
        )

    await dialog_manager.start(
        states.NewUser.user_id,
        mode=StartMode.RESET_STACK,
        data={
            "user_id": user_id,
        },
    )


async def ping(_call: CallbackQuery, _widget: Button, dialog_manager: DialogManager):
    current_state: str = (
        dialog_manager.dialog_data.get(DEFAULT_STATE_KEY) or DEFAULT_STATE
    )

    if current_state == DEFAULT_STATE:
        dialog_manager.dialog_data[DEFAULT_STATE_KEY] = "Понг!"
    else:
        dialog_manager.dialog_data[DEFAULT_STATE_KEY] = DEFAULT_STATE


async def window_getter(dialog_manager: DialogManager, **_kwargs):
    return {
        "user_id": dialog_manager.start_data.get("user_id"),
        f"{DEFAULT_STATE_KEY}": dialog_manager.dialog_data.get(DEFAULT_STATE_KEY)
        or DEFAULT_STATE,
    }


new_user_dialog = Dialog(
    Window(
        StaticMedia(
            path="/app/src/clean_architecture_app/presentation/telegram/assets/start.gif",
            type=ContentType.ANIMATION,
        ),
        Format("👋 Привет! Твой айди:\n> <b>{user_id}</b>"),
        Button(Format("{example_state}"), id="ping", on_click=ping),
        getter=window_getter,
        state=states.NewUser.user_id,
    ),
)

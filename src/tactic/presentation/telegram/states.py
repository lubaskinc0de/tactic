from aiogram.fsm.state import StatesGroup, State


class NewUser(StatesGroup):
    user_id = State()

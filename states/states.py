from aiogram.fsm.state import StatesGroup, State


class StartSG(StatesGroup):
    start = State()
    result = State()


class DialogSG(StatesGroup):
    fill_name = State()
    fill_age = State()
    fill_gender = State()
    upload_photo = State()
    fill_education = State()
    fill_wish_news = State()
    save_result = State()

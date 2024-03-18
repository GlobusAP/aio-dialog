import asyncio

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.input import ManagedTextInput, MessageInput
from aiogram_dialog.widgets.kbd import Button

from states.states import StartSG, DialogSG

from pprint import pprint
from time import sleep

user_dict: dict[int, dict[str, str | int | bool]] = {}


async def go_start(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=DialogSG.fill_name)


async def correct_name_handler(
        message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str) -> None:
    dialog_manager.dialog_data.update(name=message.text)
    await dialog_manager.next()


async def error_name_handler(
        message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str):
    await message.answer(
        text='То, что вы отправили не похоже на имя. Попробуйте еще раз'
    )


async def error_type_handler(
        message: Message, widget: MessageInput, dialog_manager: DialogManager):
    await message.answer(
        text='То, что вы отправили не похоже на текст. Попробуйте еще раз'
    )


async def correct_age_handler(
        message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str) -> None:
    dialog_manager.dialog_data.update(age=message.text)
    await dialog_manager.next()


async def error_age_handler(
        message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, text: str):
    await message.answer(
        text='Возраст должен быть целым числом от 4 до 120. Попробуйте еще раз'
    )


async def gender(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(gender=button.widget_id)
    await dialog_manager.next()


async def photo_handler(message: Message, widget: MessageInput, dialog_manager: DialogManager):
    photo = message.photo[-1]
    dialog_manager.dialog_data.update(photo_unique_id=photo.file_unique_id,
                                      photo_id=photo.file_id)
    await dialog_manager.next()


async def education(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(education=button.widget_id)
    await dialog_manager.next()


async def news(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(news=button.widget_id == 'yes_news')
    await dialog_manager.next()


async def save_result(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    if button.widget_id == 'save_yes':
        user_dict[callback.from_user.id] = dialog_manager.dialog_data

    await dialog_manager.done()


# async def showdata(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
#     if callback.from_user.id in user_dict:
#         await callback.message.answer_photo(
#             photo=user_dict[callback.from_user.id]['photo_id'],
#             caption=f'Имя: {user_dict[callback.from_user.id]["name"]}\n'
#                     f'Возраст: {user_dict[callback.from_user.id]["age"]}\n'
#                     f'Пол: {user_dict[callback.from_user.id]["gender"]}\n'
#                     f'Образование: {user_dict[callback.from_user.id]["education"]}\n'
#                     f'Получать новости: {user_dict[callback.from_user.id]["news"]}')
#         await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)
#     else:
#         await callback.answer(
#             text='Вы еще не заполняли анкету.'
#         )


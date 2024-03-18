from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row, Back, Start, Cancel, Next
from aiogram_dialog.widgets.media import DynamicMedia, StaticMedia
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.input import TextInput, MessageInput

from handlers.dialog_handlers import (go_start, correct_name_handler, error_name_handler,
                                      correct_age_handler, error_age_handler, gender, photo_handler, education, news,
                                      error_type_handler, save_result, user_dict)
from states.states import StartSG, DialogSG
from getters.getter import username_getter, result_getter
from dialogs.checks import name_check, age_check

start_dialog = Dialog(
    Window(
        Format('<b>Привет, {username}!</b>\n', when='first_show'),
        Const('Этот бот демонстрирует работу диалогов'),
        Button(Const('Перейти к заполнению анкеты'), id='b_start', on_click=go_start),
        Next(Const('Посмотреть данные вашей анкеты'), id='showdata', when='user_id'),
        getter=username_getter,
        state=StartSG.start,
    ),
    Window(
        Format(
            'Имя: {name}\n'
            'Возраст: {age}\n'
            'Пол: {gender}\n'
            'Образование: {education}\n'
            'Получать новости: {news}'),
        DynamicMedia('photo'),
        Back(Const('◀️ К началу'), id='b_back'),
        getter=result_getter,
        state=StartSG.result
    )
)

form_dialog = Dialog(
    Window(
        Const('Введите ваше имя'),
        TextInput(
            id='name_input',
            type_factory=name_check,
            on_success=correct_name_handler,
            on_error=error_name_handler
        ),
        MessageInput(
            func=error_type_handler,
            content_types=ContentType.ANY
        ),
        state=DialogSG.fill_name
    ),
    Window(
        Const('Введите ваш возраст'),
        TextInput(
            id='age_input',
            type_factory=age_check,
            on_success=correct_age_handler,
            on_error=error_age_handler
        ),
        Back(Const('◀️ Назад'), id='b_back'),
        state=DialogSG.fill_age
    ),
    Window(
        Const('Укажите ваш пол'),
        Row(
            Button(Const('Мужской ♂'), id='male', on_click=gender),
            Button(Const('Женский ♀'), id='female', on_click=gender)
        ),
        Button(Const('🤷 Пока не ясно'), id='undefined_gender', on_click=gender),
        Back(Const('◀️ Назад'), id='b_back'),
        state=DialogSG.fill_gender
    ),
    Window(
        Const('А теперь загрузите, пожалуйста, ваше фото'),
        MessageInput(
            func=photo_handler,
            content_types=ContentType.PHOTO
        ),
        Back(Const('◀️ Назад'), id='b_back'),
        state=DialogSG.upload_photo
    ),
    Window(
        Const('Укажите ваше образование'),
        Row(
            Button(Const('Среднее'), id='secondary', on_click=education),
            Button(Const('Высшее'), id='higher', on_click=education)
        ),
        Button(Const('🤷 Нету'), id='no_edu', on_click=education),
        Back(Const('◀️ Назад'), id='b_back'),
        state=DialogSG.fill_education
    ),
    Window(
        Const('Спасибо!\n\nОстался последний шаг.\n'
              'Хотели бы вы получать новости?'),
        Row(
            Button(Const('Да'), id='yes_news', on_click=news),
            Button(Const('Нет'), id='no_news', on_click=news),
        ),
        Back(Const('◀️ Назад'), id='b_back'),
        state=DialogSG.fill_wish_news
    ),
    Window(
        Const('Спасибо! Сохранить Ваши данные?'),
        Row(
            Button(Const('Да'), id='save_yes', on_click=save_result),
            Button(Const('Нет'), id='save_no', on_click=save_result),
        ),
        state=DialogSG.save_result
    ),

)

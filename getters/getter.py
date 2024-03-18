from aiogram.enums import ContentType
from aiogram.types import User
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId

from handlers.dialog_handlers import user_dict


async def username_getter(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    if dialog_manager.start_data:
        getter_data = {'username': event_from_user.username or 'Stranger',
                       'first_show': True}
        dialog_manager.start_data.clear()
    else:
        getter_data = {'first_show': False, 'user_id': user_dict.get(event_from_user.id)}
    return getter_data


async def result_getter(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    image_id = user_dict[event_from_user.id]['photo_id']
    image = MediaAttachment(ContentType.PHOTO, file_id=MediaId(image_id))

    getter_data = {
        'photo': image,
        'name': user_dict[event_from_user.id]['name'],
        'age': user_dict[event_from_user.id]['age'],
        'gender': user_dict[event_from_user.id]['gender'],
        'education': user_dict[event_from_user.id]['education'],
        'news': user_dict[event_from_user.id]['news']}
    return getter_data

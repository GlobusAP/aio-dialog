from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager, StartMode

from states.states import StartSG

router = Router()


@router.message(CommandStart())
async def process_start_cmd(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK, data={'first_show': True})

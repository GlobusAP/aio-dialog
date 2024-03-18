import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram_dialog import setup_dialogs

from config.config import Config, loadd_config
from handlers.user import router
from dialogs.dialog import start_dialog, form_dialog


async def main() -> None:
    config: Config = loadd_config()

    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()

    dp.include_router(router)
    dp.include_routers(start_dialog, form_dialog)
    setup_dialogs(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

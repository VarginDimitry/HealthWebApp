import logging

from aiogram import executor, Dispatcher
from aiogram.types import BotCommand

from middleware import CallbackJsonalizer
from middleware.AlbomMiddleware import AlbumMiddleware
from utils.TextManager import TextManager


def main():
    logging.basicConfig(level=logging.DEBUG)
    TextManager()


async def on_startup(dp: Dispatcher):
    await bot.delete_my_commands()
    await bot.set_my_commands([
        BotCommand(command="/start", description="Click me"),
    ])

if __name__ == '__main__':
    main()

    from loader import dp, bot
    dp.middleware.setup(CallbackJsonalizer())
    dp.middleware.setup(AlbumMiddleware())
    from handlers import *
    executor.start_polling(dp, on_startup=on_startup)

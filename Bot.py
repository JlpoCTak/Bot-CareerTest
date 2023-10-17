import asyncio
import logging
import sys



from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



dp = Dispatcher()
router = Router(name=__name__)
TOKEN = '6680356595:AAGRMtLUHRBXUTXfJIv9qFhC3a53asrTmnY'
async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

builder = InlineKeyboardBuilder
for index in range(3, 3):
    builder.button(text=f"Set {index}", callback_data=f"set:{index}")


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer((f"Привет, {hbold(message.from_user.full_name)}"))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
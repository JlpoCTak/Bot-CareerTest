import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from handlers import router

async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcer(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__name__"
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе подобрать специальность, которая будет соответствовать твоим интересам, просто остваь мне любое сообщение")

@router.message()
async def message_handler(msg: Message):
    await msg.answer("Специально для тебя, я подготовил профориентационный тест, оствь мне сообщение, чтобы продолжить")

    


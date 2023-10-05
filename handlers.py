from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import Keyboard as kb

router = Router()

@router.message(Command("start"))
async def process_start_command (msg: Message):
    await msg.answer("Привет! Я помогу тебе подобрать специальность, которая будет соответствовать твоим интересам, просто остваь мне любое сообщение", reply_markup=kb.greet_kb)

@router.message()
async def message_handler(msg: Message):
    await msg.answer("Специально для тебя, я подготовил профориентационный тест, оствь мне сообщение, чтобы продолжить")
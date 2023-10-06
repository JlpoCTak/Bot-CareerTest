from aiogram import types, F, Router
from aiogram import Bot
from aiogram.types import Message
from aiogram.filters import Command
import Keyboard as kb

bot = Bot()
router = Router()

@router.message(Command("start"))
async def process_start_command (msg: Message):
    await msg.answer("Привет! Я помогу тебе подобрать специальность, которая будет соответствовать твоим интересам, просто остваь мне любое сообщение", reply_markup=kb.inline_kb1)


@router.callback_query_handlers(func=lambda c: c.data == 'button_hi')
async def process_callback_button_hi(callback_query: types.CallbackQuery.id):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Специально для тебя, я подготовил профориентационный тест, оствь мне сообщение, чтобы продолжить')
@router.messeage()
async def message_handler(msg: Message):
    await msg.answer("Специально для тебя, я подготовил профориентационный тест, оствь мне сообщение, чтобы продолжить")
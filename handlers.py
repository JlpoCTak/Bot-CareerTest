from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import hbold

from kb import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import text

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Пройти тест",
        callback_data="Test")
    )
    await msg.answer(f'Првиет, {msg.from_user.full_name}, я профориентационный бот, который поможет тебе с определением твоей будушей специальности',
                     reply_markup=builder.as_markup()
    )

# @router.message()
# async def Work_choice(msg: Message):
 #  builder.add(types.InlineKeyboardButton(
  #      text=""

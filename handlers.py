from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import kb
import text

router = Router(name=__name__)
router1 = Router()

@router.message(Command("/start"))
async def greet(msg: Message):
    await msg.answer(text.greet, reply_markup=kb.greet)
@router1.message(F.text == "Меню")
@router1.message(F.text == "Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)
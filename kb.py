import aiogram.types.inline_keyboard_markup
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
import text
from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="Пройти тест",callback="Test"),
     InlineKeyboardButton(text="Посмотреть результаты теста", callback_data="Test_result")],
]
greet = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Продолжить",callback_data="Меню")]])
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Выйти в меню")]], resize_keyboard=True)
eexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти в меню", callback_data="Меню")]])
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder

menu = [
    [InlineKeyboardButton(text="Пройти тест",callback="Test"),
     InlineKeyboardButton(text="Посмотреть результаты теста", callback_data="Test_result")],
    [InlineKeyboardButton(text="Города", callback_data="City"),
     InlineKeyboardButton(text="Пропустить", callback_data="Skip")],
]
greet = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Продолжить",callback_data="Меню")]])
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Выйти в меню")]], resize_keyboard=True)
eexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Выйти в меню", callback_data="Меню")]])

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('Привет!')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_key=True).add(button_hi)
greet_kb.add(button_hi)

button1 = KeyboardButton('1')
button2 = KeyboardButton('2')
button3 = KeyboardButton('3')
button4 = KeyboardButton('4')
button5 = KeyboardButton('5')

inline_btn_1 = InlineKeyboardButton('Привет', callback_data='Button_hi')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)
inline_kb_full.add(InlineKeyboardButton('1', callback_data='btn1'))
inline_btn_3 = InlineKeyboardButton('2', callback_data='btn2')
inline_btn_4 = InlineKeyboardButton('3', callback_data='btn3')
inline_btn_5 = InlineKeyboardButton('4', callback_data='btn4')
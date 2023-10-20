import time

from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
import aiogram.filters.callback_data as filters
from aiogram.utils.markdown import hbold
import json

from kb import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import text
# from prof_test import test_holland
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

@router.callback_query(F.data == 'Test')
async def Test(callback: types.CallbackQuery):
    with open('database/professions_for_text.json', 'r', encoding='utf-8') as profissions_text:
        with open('database/holland_table.json', 'r', encoding='utf-8') as holland_table:
            dict_prof = {'realistic': 0, 'intelligent': 0, 'social': 0, 'conventional': 0, 'enterprising': 0,
                         'artistic': 0}
            max_ball_group = []
            professions = json.load(profissions_text)
            hol_table = json.load(holland_table)
            list_prof = list(professions.keys())
            for i in range(42):
                builder = InlineKeyboardBuilder()
                builder.add(types.InlineKeyboardButton(
                    text=f"{list_prof[i*2]}",
                    callback_data="answer_a")
                )
                types.InlineKeyboardButton(text=f"{list_prof[i*2+1]}",callback_data='answer_b')
                await callback.message.answer(f"1){list_prof[i*2]} - {professions[f'{list_prof[i*2]}']}"
                                              f"\n2){list_prof[i*+1]} - {professions[f'{list_prof[i*2+1]}']}")
                
                # print(F.callback_data)
                # print(InlineKeyboardButton.callback_data)
            #     answer = f'{i + 1}'# + InlineKeyboardButton.callback_data
            #     for a in hol_table:
            #         if answer in hol_table[a]:
            #             dict_prof[a] += 1
            # for k, values in dict_prof.items():
            #     if values == max(dict_prof.values()):
            #         max_ball_group.append(k)
            #



import asyncio
import time

from aiogram import types, F, Router
from aiogram.handlers import message
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
import aiogram.filters.callback_data as filters
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State,StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import json
import sqlite3
from kb import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import text
# from prof_test import test_holland
router = Router()
storage = MemoryStorage()

class WaitList(StatesGroup):
    wait_answer = State()
    get_answer = State()
    answer = State()


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
async def Test(callback: types.CallbackQuery, state: FSMContext):
    with open('database/professions_for_text.json', 'r', encoding='utf-8') as professions_text:
        with open('database/holland_table.json', 'r', encoding='utf-8') as holland_table:
            with sqlite3.connect('database/users.db') as connection:
                dict_prof = {'realistic': 0, 'intelligent': 0, 'social': 0, 'conventional': 0, 'enterprising': 0,
                             'artistic': 0}
                max_ball_group = []
                professions = json.load(professions_text)
                hol_table = json.load(holland_table)
                list_prof = list(professions.keys())
                cursor = connection.cursor()
                for i in range(42):


                    btn1 = InlineKeyboardButton(
                        text=f'{list_prof[i * 2]}',
                        callback_data='answer_a'
                    )
                    btn2 = InlineKeyboardButton(
                        text=f'{list_prof[i * 2+1]}',
                        callback_data='answer_b'
                    )
                    keyboard = InlineKeyboardMarkup(
                        inline_keyboard=[[btn1],
                                         [btn2]]
                    )
                    await callback.message.answer(f"1){list_prof[i*2]} - {professions[f'{list_prof[i*2]}']} "
                                                  f"\n2){list_prof[i*+1]} - {professions[f'{list_prof[i*2+1]}']}", reply_markup=keyboard,)

                    await state.set_state(WaitList.wait_answer)


                    @router.callback_query(WaitList.wait_answer,F.data == 'answer_a')
                    async def answer_a():
                        answer = await state.get_data()
                        await state.set_data(answer)


                        await state.set_state(WaitList.get_answer)

                    @router.callback_query(WaitList.wait_answer, F.data == 'answer_b')
                    async def answer_b():
                        answer = await state.get_data()
                        await state.set_data(answer)

                        await state.set_state(WaitList.get_answer)



                    # while await state.get_data() == {}:
                    #     print('ждем')
                    #     await asyncio.sleep(1)
                    # answer = await state.get_data()
                    # print(answer)



                    # await State.set_state(Order_answer.choosing_option1.state)
                    # await State.set_state(Order_answer.choosing_option2.state)
                    #user_data = State.get_data()
                    #answer = f'{i + 1}' + InlineKeyboardButton.callback_data
                    #for a in hol_table:
                      #   if answer in hol_table[a]:
                     #        dict_prof[a] += 1,
                    #for k, values in dict_prof.items():
                    # if values == max(dict_prof.values()):
                    #     max_ball_group.append(k)
                   # await message.answer(
                    #    f"1){list_prof[i * 2]}{user_data['chosen_option2']} - {professions[f'{list_prof[i * 2]}']}"
                     #   f"\n2){list_prof[i * +1]}{user_data['chosen_option1']} - {professions[f'{list_prof[i * 2 + 1]}']}",
                  #      reply_markup=keyboard, )
                   # await State.update_data()
                  #  await State.reset_state(with_data=False)




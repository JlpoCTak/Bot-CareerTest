import asyncio
import time

from aiogram import types, F, Router, Bot, Dispatcher
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

TOKEN = '6680356595:AAGRMtLUHRBXUTXfJIv9qFhC3a53asrTmnY'
router = Router()
storage = MemoryStorage()
bot = Bot(token=TOKEN)


class WaitList(StatesGroup):
    start = State()
    passed_test = State()


@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Пройти тест",
        callback_data="Test")
    )
    await msg.answer(f'Привет, {msg.from_user.full_name}, я профориентационный бот, который поможет тебе с определением твоей будушей специальности',
                     reply_markup=builder.as_markup()
    )
    await state.set_state(WaitList.start)


@router.callback_query(F.data == 'Test')
async def ask_questions(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    tg_user_id = callback.from_user.id
    with sqlite3.connect('database/users.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'''INSERT INTO users_answer (tg_user_id) VALUES (?)''', (tg_user_id,))
        cursor.execute('COMMIT')
    for number_question in range(42):

        with open('database/professions_for_text.json', 'r', encoding='utf-8') as professions_text:
            professions = json.load(professions_text)
            list_prof = list(professions.keys())
            btn1 = InlineKeyboardButton(
                text=f'{list_prof[number_question * 2]}',
                callback_data='answer_a'
            )
            btn2 = InlineKeyboardButton(
                text=f'{list_prof[number_question * 2 + 1]}',
                callback_data='answer_b'
            )
            keyboard = InlineKeyboardMarkup(
                inline_keyboard=[[btn1],
                                 [btn2]]
            )
            await callback.message.answer(f"Вопрос №{number_question+1}\n"
                                          f"\n1){list_prof[number_question * 2]} - {professions[f'{list_prof[number_question * 2]}']} "
                                          f"\n2){list_prof[number_question * +1]} - {professions[f'{list_prof[number_question * 2 + 1]}']}",
                                          reply_markup=keyboard, )
            tg_user_id = callback.from_user.id

            flag = True

            @router.callback_query(F.data == 'answer_a')
            async def answer_a(callback: types.CallbackQuery):
                print(callback.data)
                nonlocal flag
                flag = False
                await callback.message.delete()
                with sqlite3.connect('database/users.db') as connection:
                    cursor = connection.cursor()
                    cursor.execute(f'''UPDATE users_answer SET answ_{number_question+1} = ? WHERE tg_user_id = ?''',
                                   ('a', tg_user_id))

            @router.callback_query(F.data == 'answer_b')
            async def answer_a(callback: types.CallbackQuery):

                nonlocal flag
                flag = False
                await callback.message.delete()
                with sqlite3.connect('database/users.db') as connection:

                    cursor = connection.cursor()
                    cursor.execute(f'''UPDATE users_answer SET answ_{number_question+1} = ? WHERE tg_user_id = ?''',
                                   ('b', tg_user_id))

            while flag:
                await asyncio.sleep(0.1)
    await callback.answer('Вы прошли тест, теперь введите город в котором вы хотите обучаться')
    await state.set_state(WaitList.passed_test)





@router.message( F.text =='Тест') #WaitList.passed_test,
async def final(msg: Message, state: FSMContext):
    with open('database/specs_for_test_holland.json', 'r', encoding='utf-8') as spec_group:
        with open('database/holland_table.json', 'r', encoding='utf-8') as holland_table:
            with sqlite3.connect('database/users.db') as connection:
                cursor = connection.cursor()

                dict_prof = {'realistic': 0, 'intelligent': 0, 'social': 0, 'conventional': 0, 'enterprising': 0,
                             'artistic': 0}
                max_ball_group = []
                hol_table = json.load(holland_table)
                tg_user_id = msg.from_user.id
                answer_list = []
                for i in range(42):
                    answer = cursor.execute(f'''SELECT answ_{i+1} FROM users_answer WHERE tg_user_id = ?''',(tg_user_id,))
                    for ans in answer:
                        answer_list.append(ans[0])
                # print(answer_list) #готовый список с ответами
                for i in range(42):
                    answ = str(i+1)+answer_list[i]
                    for group in hol_table:
                        if answ in hol_table[group]:
                            dict_prof[group] += 1
                print(dict_prof)

                for group in dict_prof:
                    if dict_prof[group]==max(dict_prof.values()):
                        max_ball_group.append(group)
                # print(max_ball_group) полученная(ые) группы с макс баллом



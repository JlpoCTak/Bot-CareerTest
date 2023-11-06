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
    answer_question = State()
    start = State()
    passed_test = State()


@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Пройти тест",
        callback_data="Test")
    )
    await msg.answer(f'Привет, {msg.from_user.full_name}, я профориентационный бот,'
                     f' который поможет тебе с определением твоей будушей специальности',
                     reply_markup=builder.as_markup()
    )
    tg_user_id = msg.from_user.id
    with sqlite3.connect('database/users.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'''INSERT INTO users_answer (tg_user_id) VALUES (?)''', (tg_user_id,))
        cursor.execute('COMMIT')
    await state.set_state(WaitList.start)
    dict_num_ques = {}
    dict_num_ques['number_question'] = 0
    await state.set_data(dict_num_ques)


@router.callback_query(F.data == 'Test')
async def ask_questions(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    number_question = (await state.get_data())['number_question']

    print(number_question)

    if number_question < 42:
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



            print(callback.data)
            print('number question', number_question+1)
    elif number_question>41:
        await callback.message.answer('Вы прошли тест, теперь введите город в котором вы хотите обучаться')
        await state.set_state(WaitList.passed_test)


@router.callback_query(F.data == 'answer_a')
async def answer_a(callback: types.CallbackQuery, state: FSMContext):

    tg_user_id = callback.from_user.id
    number_question = (await state.get_data())['number_question']
    with sqlite3.connect('database/users.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'''UPDATE users_answer SET answ_{number_question+1} = ? WHERE tg_user_id = ?''',
                       ('a', tg_user_id))
    await callback.message.delete()
    dict_num_ques = {}
    dict_num_ques[f'number_question'] = number_question+1
    await state.update_data(dict_num_ques)
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(
        text=f'>>>',
        callback_data='Test'
    ))
    await callback.message.answer('Перейти к следущему вопросу', reply_markup=keyboard.as_markup())


@router.callback_query(F.data == 'answer_b')
async def answer_b(callback: types.CallbackQuery, state: FSMContext):
    tg_user_id = callback.from_user.id

    number_question = (await state.get_data())['number_question']
    with sqlite3.connect('database/users.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f'''UPDATE users_answer SET answ_{number_question+1} = ? WHERE tg_user_id = ?''',
                       ('b', tg_user_id))

    await callback.message.delete()
    dict_num_ques = {}
    dict_num_ques[f'number_question'] = number_question + 1
    await state.update_data(dict_num_ques)
    await state.set_state(WaitList.answer_question)
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(
        text=f'>>>',
        callback_data='Test'
    ))
    await callback.message.answer('Перейти к следущему вопросу', reply_markup=keyboard.as_markup())


@router.message(F.text == 'Тест') #WaitList.passed_test,
async def final(msg: Message, state: FSMContext):
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
            if len(max_ball_group)==1:
                await msg.answer('По итогам теста мы определили 1 тип личности, с профессиями, которые могут вам подойти.')
            elif len(max_ball_group)>1:
                await msg.answer(f'По итогам теста мы определили {len(max_ball_group)} типов личности, с профессиями, '
                                 f'которые могут вам подойти.')
            await asyncio.sleep(5)
            await msg.answer('Вот названия групп и что они означают')
            await asyncio.sleep(3)
            # if 'social' in max_ball_group:
            #     print(';2561651d5f1dsf')
            if 'realistic' in max_ball_group:
                await msg.answer(f'<strong>Реалистический</strong> – предпочитает работать с вещами, а не с '
                                 f'людьми. Это несоциальный, эмоционально-стабильный тип.'
                                 f'. Занимается конкретными объектами и их использованием (вещи, инструменты, техника). Хорошо'
                                 f'приспосабливается к обстановке, пластичен, трудолюбив.'
                                 f' Люди,относящиеся к этому типу, предпочитают выполнять работу, требующую '
                                 f'силы, ловкости, подвижности, хорошей координации движений, навыков практической работы.')
                await asyncio.sleep(10)
            if 'intelligent' in max_ball_group:
                await msg.answer(f'<strong>Интеллектуальный (исследовательский)</strong> – ориентирован на труд '
                                 f'с идеями и с вещами (объектами). Присуща как пластичность, так и '
                                 f'ригидность в действиях. '
                                 f'Отличается целеустремленностью, настойчивостью, терпеливостью. '
                                 f'Людей, относящихся к этому типу, отличают аналитические способности, рационализм, '
                                 f'независимость и оригинальность мышления, умение точно формулировать '
                                 f'и излагать свои мысли, решать логические задачи, генерировать новые '
                                 f'идеи. Они часто выбирают научную и исследовательскую работу. Им '
                                 f'нужна свобода для творчества.')
            if 'social' in max_ball_group:
                await msg.answer(f' <strong>Социальный</strong> – ориентирован на общение, взаимодействие с другими людьми.'
                                 f'Предпочитает работать с людьми, а не с вещами. '
                                 f'Развитые вербальные способности, повышенная'
                                 f'приспособляемость «пластичность» к меняющейся обстановке. '
                                 f'Люди этого типа гуманны, чувствительны, активны, ориентированы на социальные нормы, способны '
                                 f'понять эмоциональное состояние другого человека. Для них характерно '
                                 f' прийти на помощь.')
                await asyncio.sleep(10)
            if 'conventional' in max_ball_group:
                await msg.answer(f'<strong>Конвенциальный</strong> – отдает предпочтение четко '
                                 f'структурированной деятельности. Выбирает такие цели и задачи, которые '
                                 f'четко подтверждаются обществом и обычаями. '
                                 f'Характерны консерватизм, '
                                 f'ригидность, но обладает хорошими навыками общения, а также '
                                 f'моторными навыками. Настойчив, практичен, дисциплинирован, '
                                 f'добросовестен. Преобладают невербальные способности, прекрасный '
                                 f'исполнитель. Люди этого типа обычно проявляют склонность к работе, '
                                 f'связанной с обработкой и систематизацией информации, предоставленной '
                                 f'в виде условных знаков, цифр, формул, текстов (ведение документации, '
                                 f'установление количественных соотношений между числами и условными '
                                 f'знаками).')
                await asyncio.sleep(10)
            if 'enterprising' in max_ball_group:
                await msg.answer(f' <strong>Предприимчивый</strong> – выбирает цели и задачи, которые позволяют '
                                 f'ему проявить энергию, энтузиазм. Сочетаются импульсивность и '
                                 f'холодный расчет. Наделен как вербальными, так и невербальными '
                                 f'способностями, обладает интуицией и навыками эффективного '
                                 f'межличностного взаимодействия. Интересуется различными сферами '
                                 f'жизни и деятельности. Предпочитает работать с людьми и идеями. '
                                 f'Люди этого типа находчивы, практичны, быстро ориентируются в сложной '
                                 f'обстановке, склонны к самостоятельному принятию решений, социально '
                                 f'активны, готовы рисковать, ищут острые ощущения. Любят и умеют общаться.')
                await asyncio.sleep(10)
            if 'artistic' in max_ball_group:
                await msg.answer(f'<strong>Артистический</strong> – сложный взгляд на жизнь, гибкость и '
                                 f'независимость в принятии решений.Предпочитает занятия творческого характера. '
                                 f'Преобладают вербальные способности. Для этого типа характерны '
                                 f'исключительные способности восприятия и моторики, высокая '
                                 f'чувствительность всех анализаторов. '
                                 f'Люди этого типа оригинальны, независимы в принятии '
                                 f'решений, редко ориентируются на социальные нормы и одобрение, '
                                 f'обладают необычным взглядом на жизнь, гибкостью мышления, '
                                 f'эмоциональной чувствительностью. ')
                await asyncio.sleep(10)

            keyboard = InlineKeyboardBuilder()
            for i in range(len(max_ball_group)):
                keyboard.row(InlineKeyboardButton(
                    text=f'{max_ball_group[i]}',
                    callback_data=f'group_{max_ball_group[i]}'
                ))
            await msg.answer('Выберите тип, который вам больше подходит',
                             reply_markup=keyboard.as_markup(resize_keyboard=True))


@router.callback_query(F.data.startswith('group_'))
async def proffesions_group(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Мы предоставим вам список специальностей, которые наиболее вам подходят')
    print(await state.get_data())
    profs_group = callback.data.split('_')[1]
    dict_prof = {}
    dict_prof[f'{profs_group}'] = profs_group
    await state.set_data(dict_prof)
    print(await state.get_data())
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(
        text=f'Выбрать профессию',
        callback_data='professions_0_5'
    ))

    await callback.message.answer(
                                  'Выберите наиболее интересующую вас профессию:',
                                  reply_markup=keyboard.as_markup(resize_keyboard=True))


@router.callback_query(F.data.startswith('professions_'))
async def list_profs(callback: types.CallbackQuery, state:FSMContext):
    profs_group = (await state.get_data()).keys()
    prof_group = 0
    for k in profs_group:
        prof_group = k
    print(prof_group)

    with open('database/specs_for_test_holland.json', 'r', encoding='utf-8') as spec_groups:
        spec_group = json.load(spec_groups)
        group = spec_group[prof_group]  # словарь "код":"название специальности"
    keys = []
    for key in group.keys():
        keys.append(key)
    print(keys)
    start_btns = int(callback.data.split('_')[1])
    end_btns = int(callback.data.split('_')[2])
    keyboard = InlineKeyboardBuilder()
    for key in range(start_btns, end_btns):
        keyboard.row(InlineKeyboardButton(
            text=f'{group[keys[key]]}',
            callback_data=None
        ))
    keyboard.add(InlineKeyboardButton(
        text='<<<',
        callback_data=f'professions_{start_btns-5}_{end_btns-5}'
    ),InlineKeyboardButton(
        text='>>>',
        callback_data=f'professions_{start_btns + 5}_{end_btns + 5}'
    ))
    await callback.message.answer(text='/', reply_markup=keyboard.as_markup(resize_keyboard=True))
    with open('specs_for_test_holland.json', 'r') as json_file:
        job_positions = json.load(json_file)

        response = "Список профессий:\n"
        count = 0
        for job_code, job_name in job_positions.items():
            response += f"{job_code}: {job_name}\n"
            count += 1
            if count == 5:
                await bot.send_message(chat_id=message.chat.id, text=response)
                response = ""
                count = 0
        if response != "":
            await bot.send_message(chat_id=message.chat.id, text=response)

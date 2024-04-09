import asyncio
import os
import time
import hashlib
from aiogram import types, F, Router, Bot, Dispatcher
from aiogram.handlers import message
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
import aiogram.filters.callback_data as filters
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State,StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import json
import sqlite3
from kb import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import work_with_db
# from prof_test import test_holland

TOKEN = os.getenv('TOKEN')
router = Router()
storage = MemoryStorage()
bot = Bot(token=TOKEN)


class WaitList(StatesGroup):
    answer_question = State()
    start = State()
    passed_test = State()
    change_city = State()
    menu = State()


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
                                          f"Выберите наиболее близкую для вас профессию: "
                                          f"\n1){list_prof[number_question * 2]} - {professions[f'{list_prof[number_question * 2]}']} "
                                          f"\n2){list_prof[number_question * 2+1]} - {professions[f'{list_prof[number_question * 2 + 1]}']}",
                                          reply_markup=keyboard, )

            print(callback.data)
            print('number question', number_question+1)
    elif number_question > 41:

        await callback.message.answer('Вы прошли тест, теперь введите город в котором вы хотите обучаться')
        await state.set_state(WaitList.change_city)


@router.message(WaitList.change_city)
async def take_city(msg: Message, state: FSMContext):
    city = msg.text
    user_id = msg.from_user.id
    with sqlite3.connect('database/users.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''UPDATE users_answer SET city = ? WHERE tg_user_id = ?''', (city, user_id))
    await state.set_state(WaitList.menu)
    await msg.answer(text=f'Вы выбрали город, теперь в городе {city}, вы можете выбрать спецальность ')
    await msg.answer('Теперь вам доступно меню')
    bot_commands = [
        types.BotCommand(command="/menu", description="меню действий"),

    ]
    await bot.set_my_commands(bot_commands)



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


@router.callback_query(F.data == 'result_test') #WaitList.passed_test,
async def final(callback: types.CallbackQuery, state: FSMContext):
    with open('database/holland_table.json', 'r', encoding='utf-8') as holland_table:
        with sqlite3.connect('database/users.db') as connection:
            cursor = connection.cursor()

            dict_prof = {'realistic': 0, 'intelligent': 0, 'social': 0, 'conventional': 0, 'enterprising': 0,
                         'artistic': 0}
            max_ball_group = []
            hol_table = json.load(holland_table)
            tg_user_id = callback.from_user.id
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


            for group in dict_prof:
                if dict_prof[group] == max(dict_prof.values()):
                    max_ball_group.append(group)
            # print(max_ball_group) полученная(ые) группы с макс баллом
            if len(max_ball_group)==1:
                await callback.message.answer('По итогам теста мы определили 1 тип личности, с профессиями, которые могут вам подойти.')
            elif len(max_ball_group)>1:
                await callback.message.answer(f'По итогам теста мы определили {len(max_ball_group)} типов личности, с профессиями, '
                                 f'которые могут вам подойти.')
            await asyncio.sleep(3)
            await callback.message.answer('Вот названия типов и что они означают')
            await asyncio.sleep(3)
            # if 'social' in max_ball_group:
            #     print(';2561651d5f1dsf')
            if 'realistic' in max_ball_group:
                await callback.message.answer(f'<strong>Реалистический</strong> – предпочитает работать с вещами, а не с '
                                 f'людьми. Это несоциальный, эмоционально-стабильный тип.'
                                 f'. Занимается конкретными объектами и их использованием (вещи, инструменты, техника). Хорошо'
                                 f'приспосабливается к обстановке, пластичен, трудолюбив.'
                                 f' Люди,относящиеся к этому типу, предпочитают выполнять работу, требующую '
                                 f'силы, ловкости, подвижности, хорошей координации движений, навыков практической работы.')
                await asyncio.sleep(3)
            if 'intelligent' in max_ball_group:
                await callback.message.answer(f'<strong>Интеллектуальный (исследовательский)</strong> – ориентирован на труд '
                                 f'с идеями и с вещами (объектами). Присуща как пластичность, так и '
                                 f'ригидность в действиях. '
                                 f'Отличается целеустремленностью, настойчивостью, терпеливостью. '
                                 f'Людей, относящихся к этому типу, отличают аналитические способности, рационализм, '
                                 f'независимость и оригинальность мышления, умение точно формулировать '
                                 f'и излагать свои мысли, решать логические задачи, генерировать новые '
                                 f'идеи. Они часто выбирают научную и исследовательскую работу. Им '
                                 f'нужна свобода для творчества.')
            if 'social' in max_ball_group:
                await callback.message.answer(f' <strong>Социальный</strong> – ориентирован на общение, взаимодействие с другими людьми.'
                                 f'Предпочитает работать с людьми, а не с вещами. '
                                 f'Развитые вербальные способности, повышенная'
                                 f'приспособляемость «пластичность» к меняющейся обстановке. '
                                 f'Люди этого типа гуманны, чувствительны, активны, ориентированы на социальные нормы, способны '
                                 f'понять эмоциональное состояние другого человека. Для них характерно '
                                 f' прийти на помощь.')
                await asyncio.sleep(3)
            if 'conventional' in max_ball_group:
                await callback.message.answer(f'<strong>Конвенциальный</strong> – отдает предпочтение четко '
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
                await asyncio.sleep(3)
            if 'enterprising' in max_ball_group:
                await callback.message.answer(f' <strong>Предприимчивый</strong> – выбирает цели и задачи, которые позволяют '
                                 f'ему проявить энергию, энтузиазм. Сочетаются импульсивность и '
                                 f'холодный расчет. Наделен как вербальными, так и невербальными '
                                 f'способностями, обладает интуицией и навыками эффективного '
                                 f'межличностного взаимодействия. Интересуется различными сферами '
                                 f'жизни и деятельности. Предпочитает работать с людьми и идеями. '
                                 f'Люди этого типа находчивы, практичны, быстро ориентируются в сложной '
                                 f'обстановке, склонны к самостоятельному принятию решений, социально '
                                 f'активны, готовы рисковать, ищут острые ощущения. Любят и умеют общаться.')
                await asyncio.sleep(3)
            if 'artistic' in max_ball_group:
                await callback.message.answer(f'<strong>Артистический</strong> – сложный взгляд на жизнь, гибкость и '
                                 f'независимость в принятии решений.Предпочитает занятия творческого характера. '
                                 f'Преобладают вербальные способности. Для этого типа характерны '
                                 f'исключительные способности восприятия и моторики, высокая '
                                 f'чувствительность всех анализаторов. '
                                 f'Люди этого типа оригинальны, независимы в принятии '
                                 f'решений, редко ориентируются на социальные нормы и одобрение, '
                                 f'обладают необычным взглядом на жизнь, гибкостью мышления, '
                                 f'эмоциональной чувствительностью. ')
                await asyncio.sleep(3)

            keyboard = InlineKeyboardBuilder()
            for i in range(len(max_ball_group)):
                keyboard.row(InlineKeyboardButton(
                    text=f'{max_ball_group[i]}',
                    callback_data=f'group_{max_ball_group[i]}'
                ))
            await callback.message.answer('Выберите тип, который вам больше подходит',
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

    with open('database/specs_for_test_holland.json', 'r', encoding='utf-8') as spec_groups:
        spec_group = json.load(spec_groups)
        group = spec_group[prof_group]  # словарь "код":"название специальности"
    keys = []
    len_group = len(group)-1
    max_pages = (len_group//5)+1

    for key in group.keys():
        keys.append(key)


    start_btns = int(callback.data.split('_')[1])
    end_btns = int(callback.data.split('_')[2])
    current_page = (end_btns//5)

    if end_btns <= len_group and start_btns >= 0:

        if current_page == 1:

            keyboard = InlineKeyboardBuilder()
            for key in range(start_btns, end_btns):
                with sqlite3.connect('database/users.db') as connection:
                    cursor = connection.cursor()
                    code_profs = cursor.execute('''SELECT code FROM specs WHERE name = ?''', (group[keys[key]],))

                    for code_prof in code_profs:
                        code_prof = code_prof[0]

                keyboard.row(InlineKeyboardButton(
                    text=f'{group[keys[key]]}',
                    callback_data=f'profname_{code_prof}'
                ))
            keyboard.row(InlineKeyboardButton(
                text='<<<',
                callback_data=f'professions_{len_group-(len_group-(len_group//5)*5)}_{len_group+1}'
            ), InlineKeyboardButton(
                text='>>>',
                callback_data=f'professions_{start_btns + 5}_{end_btns + 5}'
            ))
            await callback.message.answer(text=f'Страница: {current_page} из {max_pages}', reply_markup=keyboard.as_markup(resize_keyboards=False))
        elif current_page == max_pages:
            keyboard = InlineKeyboardBuilder()
            for key in range(start_btns, end_btns):
                with sqlite3.connect('database/users.db') as connection:
                    cursor = connection.cursor()
                    code_profs = cursor.execute('''SELECT code FROM specs WHERE name = ?''', (group[keys[key]],))

                    for code_prof in code_profs:
                        code_prof = code_prof[0]

                keyboard.row(InlineKeyboardButton(
                    text=f'{group[keys[key]]}',
                    callback_data=f'profname_{code_prof}'
                ))
            keyboard.row(InlineKeyboardButton(
                text='<<<',
                callback_data=f'professions_{start_btns - 5}_{end_btns - 5}'
            ), InlineKeyboardButton(
                text='>>>',
                callback_data=f'professions_0_5'
            ))
            await callback.message.answer(text=f'Страница: {current_page} из {max_pages}',
                                          reply_markup=keyboard.as_markup(resize_keyboards=False))
        else:
            keyboard = InlineKeyboardBuilder()
            for key in range(start_btns, end_btns):
                with sqlite3.connect('database/users.db') as connection:
                    cursor = connection.cursor()
                    code_profs = cursor.execute('''SELECT code FROM specs WHERE name = ?''', (group[keys[key]],))

                    for code_prof in code_profs:
                        code_prof = code_prof[0]

                keyboard.row(InlineKeyboardButton(
                    text=f'{group[keys[key]]}',
                    callback_data=f'profname_{code_prof}'
                ))
            keyboard.row(InlineKeyboardButton(
                text='<<<',
                callback_data=f'professions_{start_btns - 5}_{end_btns - 5}'
            ), InlineKeyboardButton(
                text='>>>',
                callback_data=f'professions_{start_btns + 5}_{end_btns + 5}'
            ))
            await callback.message.answer(text=f'Страница: {current_page} из {max_pages}',
                                          reply_markup=keyboard.as_markup(resize_keyboards=False))
    elif (current_page/max_pages) == 1:

        keyboard = InlineKeyboardBuilder()

        for key in range((end_btns-5), len_group+1):
            with sqlite3.connect('database/users.db') as connection:
                cursor = connection.cursor()
                code_profs = cursor.execute('''SELECT code FROM specs WHERE name = ?''', (group[keys[key]],))

                for code_prof in code_profs:
                    code_prof = code_prof[0]

            keyboard.row(InlineKeyboardButton(
                text=f'{group[keys[key]]}',
                callback_data=f'profname_{code_prof}'
            ))
        keyboard.row(InlineKeyboardButton(
            text='<<<',
            callback_data=f'professions_{start_btns - 5}_{end_btns - 5}'
        ), InlineKeyboardButton(
            text='>>>',
            callback_data=f'professions_{0}_{5}'
        ))
        await callback.message.answer(text=f'Страница: {current_page} из {max_pages}',
                                      reply_markup=keyboard.as_markup(resize_keyboards=False))

    await callback.message.delete()


@router.callback_query(F.data.startswith('profname_'))
async def print_college(callback: types.CallbackQuery, state: FSMContext):
    prof_code = callback.data.split('_')[1]
    # print(prof_code)
    user_id = callback.from_user.id
    with sqlite3.connect('database/users.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''UPDATE users_answer SET prof_code = ? WHERE tg_user_id = ?''', (prof_code, user_id))


    with sqlite3.connect('database/users.db') as connection:
        cursor = connection.cursor()
        data_user = cursor.execute('''SELECT city, prof_code FROM users_answer WHERE tg_user_id = ?''', (user_id,))
        for data in data_user:
            info_user = list(data)

    print(info_user)
    town_list = work_with_db.find_college(info_user[1], work_with_db.search_city(info_user[0]))
    if town_list is None:
        await callback.message.answer(text='В выбранном вами городе нету колледжей с данными профессий')
    else:
        keyboard = InlineKeyboardBuilder()
        for college in town_list:
            print(town_list)
            print(college)
            print(college.split(":")[1]+college.split(":")[2])
            keyboard.row(InlineKeyboardButton(
                text=f'{college.split(":")[0].split(".")[2]}',
                url=f'{college.split(":")[1]+":"+college.split(":")[2]}'
            ))
        await callback.message.answer(text=f'Вот список колледжей в выбранном городе по вашей професии:',
                                      reply_markup=keyboard.as_markup(resize_keyboards=False))
        # await callback.message.delete()


@router.message(WaitList.start, Command("menu"))
async def menu(msg: Message, state: FSMContext):
    await msg.answer('Вы только начали нажмите кнопку "Пройти тест", или допройдите тест')

@router.message(WaitList.menu, Command("menu"))
async def menu(msg: Message, state: FSMContext):
    with sqlite3.connect('database/users.db') as connection:
        cursor = connection.cursor()
        city_from_user_id = msg.from_user.id
        cursor.execute('''SELECT city FROM users_answer WHERE tg_user_id = ?''', (city_from_user_id,))
        city_result = cursor.fetchone()
        if city_result:
            city_from_user = city_result[0]
    keyboard = ReplyKeyboardBuilder()
    for i in range(1):
     keyboard.add(
types.KeyboardButton(text='Перепройти тест'),
        types.KeyboardButton(text='Посмотреть результат теста'),
        types.KeyboardButton(text='Показать город'),
        types.KeyboardButton(text=f'Посмотреть специальности в выбранном городе:')
        )
    keyboard.adjust(1)
    await msg.answer("Выберите действие", reply_markup=keyboard.as_markup(resize_keyboards=True))


@router.message(WaitList.menu, F.text == "Показать город")
async def city(msg: types.Message):
    with sqlite3.connect('database/users.db') as connection:
        cursor = connection.cursor()
        city_from_user_id = msg.from_user.id
        cursor.execute('''SELECT city FROM users_answer WHERE tg_user_id = ?''', (city_from_user_id,))
        city_result = cursor.fetchone()
        if city_result:
            city_from_user = city_result[0]
            await msg.answer(text=f'Выбранный вами город: {city_from_user}')

    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(
        text="Изменить город",
        callback_data="change_city_cb")
    )
    await msg.answer('Изменить город?', reply_markup=keyboard.as_markup(resize_keyboard=True))


@router.callback_query(WaitList.menu, F.data == 'change_city_cb')
async def change_city_callback(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Введите город')
    await state.set_state(WaitList.change_city)






@router.message(F.text == "Перепройти тест")
async def test_restart(msg: Message, state: FSMContext):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(
        text="Подтвердить",
        callback_data="Test")
    )
    await state.set_state(WaitList.start)
    dict_num_ques = {}
    dict_num_ques['number_question'] = 0
    await state.set_data(dict_num_ques)
    await msg.answer("Вы готовы перепройти тест", reply_markup=keyboard.as_markup(resize_keybiards=True))


@router.message(F.text == "Посмотреть результат теста")
async def test_restart(msg: Message,):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(
        text="Посмотреть",
        callback_data="result_test")
    )
    await msg.answer("Вы хотите посмотреть результаты теста", reply_markup=keyboard.as_markup(resize_keyboards=True))


@router.message(F.text == "Посмотреть психотипы:")
async def specs_list(msg: Message):
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
                answer = cursor.execute(f'''SELECT answ_{i + 1} FROM users_answer WHERE tg_user_id = ?''',
                                        (tg_user_id,))
                for ans in answer:
                    answer_list.append(ans[0])
            # print(answer_list) #готовый список с ответами
            for i in range(42):
                answ = str(i + 1) + answer_list[i]
                for group in hol_table:
                    if answ in hol_table[group]:
                        dict_prof[group] += 1

            for group in dict_prof:
                if dict_prof[group] == max(dict_prof.values()):
                    max_ball_group.append(group)
            # print(max_ball_group) полученная(ые) группы с макс баллом

        if 'realistic' in max_ball_group:
            await msg.answer(f'<strong>Реалистический</strong> – предпочитает работать с вещами, а не с '
                                          f'людьми. Это несоциальный, эмоционально-стабильный тип.'
                                          f'. Занимается конкретными объектами и их использованием (вещи, инструменты, техника). Хорошо'
                                          f'приспосабливается к обстановке, пластичен, трудолюбив.'
                                          f' Люди,относящиеся к этому типу, предпочитают выполнять работу, требующую '
                                          f'силы, ловкости, подвижности, хорошей координации движений, навыков практической работы.')
            await asyncio.sleep(1)
        if 'intelligent' in max_ball_group:
            await msg.answer(
                f'<strong>Интеллектуальный (исследовательский)</strong> – ориентирован на труд '
                f'с идеями и с вещами (объектами). Присуща как пластичность, так и '
                f'ригидность в действиях. '
                f'Отличается целеустремленностью, настойчивостью, терпеливостью. '
                f'Людей, относящихся к этому типу, отличают аналитические способности, рационализм, '
                f'независимость и оригинальность мышления, умение точно формулировать '
                f'и излагать свои мысли, решать логические задачи, генерировать новые '
                f'идеи. Они часто выбирают научную и исследовательскую работу. Им '
                f'нужна свобода для творчества.')
        if 'social' in max_ball_group:
            await msg.answer(
                f' <strong>Социальный</strong> – ориентирован на общение, взаимодействие с другими людьми.'
                f'Предпочитает работать с людьми, а не с вещами. '
                f'Развитые вербальные способности, повышенная'
                f'приспособляемость «пластичность» к меняющейся обстановке. '
                f'Люди этого типа гуманны, чувствительны, активны, ориентированы на социальные нормы, способны '
                f'понять эмоциональное состояние другого человека. Для них характерно '
                f' прийти на помощь.')
            await asyncio.sleep(1)
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
            await asyncio.sleep(1)
        if 'enterprising' in max_ball_group:
            await msg.answer(
                f' <strong>Предприимчивый</strong> – выбирает цели и задачи, которые позволяют '
                f'ему проявить энергию, энтузиазм. Сочетаются импульсивность и '
                f'холодный расчет. Наделен как вербальными, так и невербальными '
                f'способностями, обладает интуицией и навыками эффективного '
                f'межличностного взаимодействия. Интересуется различными сферами '
                f'жизни и деятельности. Предпочитает работать с людьми и идеями. '
                f'Люди этого типа находчивы, практичны, быстро ориентируются в сложной '
                f'обстановке, склонны к самостоятельному принятию решений, социально '
                f'активны, готовы рисковать, ищут острые ощущения. Любят и умеют общаться.')
            await asyncio.sleep(1)
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
            await asyncio.sleep(1)

        keyboard = InlineKeyboardBuilder()
        for i in range(len(max_ball_group)):
            keyboard.row(InlineKeyboardButton(
                text=f'{max_ball_group[i]}',
                callback_data=f'group_{max_ball_group[i]}'
            ))
        await msg.answer("Выберите психотип, который вам больше подходит", reply_markup=keyboard.as_markup(resize_keyboards=True))


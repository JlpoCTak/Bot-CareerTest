

def Choose_Place_Of_Work():
    erth_science = 0
    Inf_Technology = 0
    Energetic = 0
    Builder = 0
    industry = 0
    Build_Transport = 0
    Med_science = 0
    jobWithPeople = 0
    stick_stick_man = 0

    print("вы предпочтёте работать:")
    print("1. На улице")
    print("2. В офисе")
    print("3. В мастерской")

    choice = input("Введите номер ответа: ")
    if choice == "1":
         erth_science += 1
         Builder += 1
         erth_sciences()
    elif choice == "2":
         Inf_Technology+=1
         Energetic+=1
         jobWithPeople+=1
         Med_science += 1
         Builder += 1
         popal_v_office()
    elif choice == "3":
         stick_stick_man += 1
         industry += 1
         Energetic += 1
         Build_Transport +=1
         prosnulsia_na_rabote()

def erth_siences():
    print("Вы бы хотели изучать")
    print("1. Земные породы, архитуктуры")
    print("2. Преобразованием химчских элементов, ")
    choice = input("Введите номер ответа: ")

    if choice == "1":
        erth_sience += 1
        Gorlovka_vibrala_tebia()
    elif choice == "2":
        Builder += 1
        YouAreWalterWhite()

def Gorlovka_vibrala_tebia():
    print("Вы предпочтёте ")
    print("1. Обрабатывать землю")
    print("2. Изучать земные и горные породы и газы")
    choice = input("Введите номер ответа: ")
    if choice == "1":
        hoz()
    elif choice == "2":
        geology()

def geology():
    print("Вы предпочтете:")
    print("1. Составлять карты морей и суши, изучать движения, распеределение воды в природе")
    print("2. Изучать погодные явления на Земле, состав воздуха и составлять прогнозы погоды")
    choice = input("Введите номер ответа: ")

    if choice == "1":
        kartograf()
    elif choice == "2":
        meteorolog()

def kartograf():
    print("")

    choice = input("Введите номер ответа: ")

    if choice == "1":
        ()
    elif choice == "2":
        ()
# Картография
# --  05.02.02 - Гидрология

def meteorolog():
    print("")

    choice = input("Введите номер ответа: ")

    if choice == "1":
        ()
    elif choice == "2":
        ()
# Метеорология
# Гидрометнаблюдатель

def hoz():
    print("вы предпочтёте:")
    print("1.Проводить время в поле")
    print("2.Проводить время в лесу")
    print("3.Проводить вреия в море")
    choice = input("Введите номер ответа: ")

    if choice == "1":
        field()
    elif choice == "2":
        forest()
    elif choice == "3":
        ocean()

def field():
    print("")
    choice = input("Введите номер ответа: ")
    if choice == "1":
        ()
    elif choice == "2":
        ()
# Агрономия
# Мастер садово-паркового и ландшафтного строительства
# Пчеловод
# Оленевод-механизатор
# Охотник промысловый
# Хозяйка (ин) усадьбы
# Управляющий сельской усадьбой
# Мастер растениеводства
# Овощевод защищенного грунта
# Мастер сельскохозяйственного производства
# Заготовитель продуктов и сырья
# Тракторист-машинист сельскохозяйственного производства
# Мастер по ремонту и обслуживанию электрооборудования в сельском хозяйстве
# Мастер по техническому обслуживанию и ремонту машинно-тракторного парка
# Технология производства и переработки сельскохозяйственной продукции
# Механизация сельского хозяйства
# Электрификация и автоматизация сельского хозяйства
# Садово-парковое и ландшафтное строительство
# Пчеловодство
# Охотоведение и звероводство
# Кинология
# Эксплуатация и ремонт сельскохозяйственной техники и оборудования

def forest():
    print("")

    choice = input("Введите номер ответа: ")

    if choice == "1":
        ()
    elif choice == "2":
        ()

# Мастер по лесному хозяйству
# Станочник деревообрабатывающих станков
# Станочник-обработчик
# Оператор линий и установок в деревообработке
# Контролер качества материалов и продукции деревообрабатывающего производства
# Оператор машин по производству бумаги и картона
# Сушильщик в бумажном производстве
# Контролер целлюлозно-бумажного производства
# Лесное и лесопарковое хозяйство
# Технология лесозаготовок
# Технология деревообработки
# Технология комплексной переработки древесины

def ocean():
    master = 0
    fishman = 0
    ihteology = 0
    bio = 0
    industry = 0
    print("В этом отделе вам доступы данные специальности:")
    print("Мастер по водным биоресурсам и аквакультуре,\n Обработчик рыбы и морепродуктов,\n Рыбак прибрежного лова,\n Ихтиология и рыбоводство,\n Обработка водных биоресурсов,\n Промышленное рыболовство")
    print("В чем состоят основные обязанности мастера по водным биоресурсам и аквакультуре?")
    choice = input("Введите номер ответа: ")
    print("1. Изучает водные биоресурсы, занимается их сохранением и использованием, развивает аквакультуру, проектирует искусственные водоемы и обучает специалистов.")
    print("2. ")
    print("3. Мастер по водным биоресурсам и аквакультуре занимается исключительно научной деятельностью и не имеет никаких практических обязанностей.")
    if choice == "1":
        master +=1
        ocean2()
    elif choice == "2":
        ocean2()
    elif chjice == "3":                      #сделать систему которая за правильный ответ +1, за неправильный +0, если в неправильном ответе были задействлванны ответы свзанные с другой темой -1 по этой теме
        ocean2

def ocean2():
    print("")
# Мастер по водным биоресурсам и аквакультуре
# Обработчик рыбы и морепродуктов
# Рыбак прибрежного лова
# Ихтиология и рыбоводство
# Обработка водных биоресурсов
# Промышленное рыболовство

def YouAreWalterWhite():
    print("вы предпочтёте:")
    print("1.Проектировать здания")
    print("2.Управлять химическими технологиями")
    print("3.Производить пищевую продукцию")
    print("4.защищать человека и природу, и предотвращать ЧС ")
    choice = input("Введите номер ответа: ")
    if choice == "1":
        arhitec()
    elif choice == "2":
        chem_tech()
    elif choice == "3":
        povar()
    elif choice == "4":
        fireman()

def povar():
    print("")

    choice = input("Введите номер ответа: ")

    if choice == "1":
        ()
    elif choice == "2":
        ()

# Аппаратчик-оператор в биотехнологии
# --  19.01.02 - Лаборант-аналитик
# --  19.01.03 - Аппаратчик элеваторного, мукомольного, крупяного и комбикормового производства
# --  19.01.04 - Пекарь
# --  19.01.05 - Оператор поточно-автоматической линии (макаронное производство)
# --  19.01.06 - Аппаратчик производства сахара
# --  19.01.07 - Кондитер сахаристых изделий
# --  19.01.08 - Пивовар
# --  19.01.09 - Мастер по эксплуатации, механизации, автоматизации и роботизации технологического оборудования и процессов пищевой промышленности
# --  19.01.10 - Мастер производства молочной продукции
# --  19.01.11 - Изготовитель мороженого
# --  19.01.12 - Переработчик скота и мяса
# --  19.01.13 - Обработчик птицы и кроликов
# --  19.01.14 - Оператор процессов колбасного производства
# --  19.01.15 - Аппаратчик получения растительного масла
# --  19.01.16 - Оператор линии производства маргарина
# --  19.02.01 - Биохимическое производство
# --  19.02.02 - Технология хранения и переработки зерна
# --  19.02.03 - Технология хлеба, кондитерских и макаронных изделий
# --  19.02.04 - Технология сахаристых продуктов
# --  19.02.05 - Технология бродильных производств и виноделие
# --  19.02.06 - Технология консервов и пищеконцентратов
# --  19.02.07 - Технология молока и молочных продуктов
# --  19.02.08 - Технология мяса и мясных продуктов
# --  19.02.09 - Технология жиров и жирозаменителей
# --  19.02.10 - Технология продукции общественного питания

def chem_tech():
    print("")

    choice = input("Введите номер ответа: ")

    if choice == "1":
        ()
    elif choice == "2":
        ()
# Лаборант по физико-механическим испытаниям
# Лаборант-эколог
# Аппаратчик-оператор экологических установок
# Изготовитель изделий строительной керамики
# Аппаратчик-оператор производства неорганических веществ
# Оператор производства стекловолокна, стекловолокнистых материалов и изделий стеклопластиков
# Аппаратчик производства стекловолокнистых материалов и стеклопластиков
# Мастер-изготовитель деталей и изделий из стекла
# Мастер-обработчик стекла и стеклоизделий
# Отдельщик и резчик стекла
# Контролер стекольного производства
# Изготовитель фарфоровых и фаянсовых изделий
# Отделочник и комплектовщик фарфоровых и фаянсовых изделий
# Контролер-приемщик фарфоровых, фаянсовых и керамических изделий
# Изготовитель эмалированной посуды
# Аппаратчик в производстве химических волокон
# Оператор в производстве химических волокон
# Аппаратчик производства синтетических смол и пластических масс
# Машинист-оператор в производстве изделий из пластмасс
# Прессовщик изделий из пластмасс
# Машинист-аппаратчик подготовительных процессов в производстве резиновых смесей, резиновых технических изделий и шин
# Оператор в производстве шин
# Оператор процессов вулканизации
# Мастер шиномонтажной мастерской
# Оператор в производстве резиновых технических изделий и обуви
# Аппаратчик-оператор нефтехимического производства
# Машинист технологических насосов и компрессоров
# Оператор нефтепереработки
# Мастер по обслуживанию магистральных трубопроводов
# Аппаратчик-оператор коксохимического производства
# Машинист машин коксохимического производства
# Аппаратчик-оператор азотных производств и продуктов органического синтеза
# Лаборант по контролю качества сырья, реактивов, промежуточных продуктов, готовой продукции, отходов производства
# Аналитический контроль качества химических соединений
# Химическая технология отделочного производства и обработки изделий
# Химическая технология неорганических веществ
# Электрохимическое производство
# Производство тугоплавких неметаллических и силикатных материалов и изделий
# Химическая технология органических веществ
# Технология производства и переработки пластических масс и эластомеров
# Технология кинофотоматериалов и магнитных носителей
# Переработка нефти и газа
# Коксохимическое производство
# Технология пиротехнических составов и изделий
# Технология аналитического контроля химических соединений
# Технология производства изделий из полимерных композитов
def fireman():
    print("")

    choice = input("Введите номер ответа: ")

    if choice == "1":
        ()
    elif choice == "2":
        ()

# Пожарный
# --  20.02.01 - Рациональное использование природохозяйственных комплексов
# --  20.02.02 - Защита в чрезвычайных ситуациях
# --  20.02.03 - Природоохранное обустройство территорий
# --  20.02.04 - Пожарная безопасность
# Организация оперативного (экстренного) реагирования в чрезвычайных ситуациях
def popal_v_office():
    print("вы бы предпочли:")
    print("1.заниматься бумажной работой")
    print("2.Отслеживать изменения химических элементов, следить за качеством строй-химических материалов")

    choice = input("Введите номер ответа: ")

    if choice == "1":
        jobWithPeople += 1
        informationalTechnology += 1
        Energetic += 1
        bumaga()
    elif choice == "2":
        Med_science += 1
        Builder += 1
        Energetic += 1
        YouAreRealWalterWhite()


def bumaga():
    print("вы бы предпочли")
    print("1.Работать с социумом")
    print("2.Работать в информационной среде")
    print("3.Управлять техническими системами")
    choice = input("Введите номер ответа: ")

    if choice == "1":
        sociecity()
    elif choice == "2":
        information_environment()
    elif choice == "2":
        technical_systems()

# 28) Экономика и управление
# --  38.01.01 - Оператор диспетчерской (производственно-диспетчерской) службы
# --  38.01.02 - Продавец, контролер-кассир
# --  38.01.03 - Контролер банка
# --  38.02.01 - Экономика и бухгалтерский учет (по отраслям)
# --  38.02.02 - Страховое дело (по отраслям)
# --  38.02.03 - Операционная деятельность в логистике
# --  38.02.04 - Коммерция (по отраслям)
# --  38.02.05 - Товароведение и экспертиза качества потребительских товаров
# --  38.02.06 - Финансы
# --  38.02.07 - Банковское дело
# 29) Социология и социальная работа
# --  39.01.01 - Социальный работник
# --  39.02.01 - Социальная работа
# --  39.02.02 - Организация сурдокоммуникации
# 30) Юриспруденция
# --  40.02.01 - Право и организация социального обеспечения
# --  40.02.02 - Правоохранительная деятельность
# --  40.02.03 - Право и судебное администрирование
# 31) Средства массовой информации и информационно-библиотечное дело
# --  42.01.01 - Агент рекламный
# --  42.02.01 - Реклама
# --  42.02.02 - Издательское дело
# 32) Сервис и туризм
# --  43.01.01 - Официант, бармен
# --  43.01.02 - Парикмахер
# --  43.01.03 - Бортпроводник судовой
# --  43.01.04 - Повар судовой
# --  43.01.05 - Оператор по обработке перевозочных документов на железнодорожном транспорте
# --  43.01.06 - Проводник на железнодорожном транспорте
# --  43.01.07 - Слесарь по эксплуатации и ремонту газового оборудования
# --  43.01.08 - Аппаратчик химической чистки
# --  43.01.09 - Повар, кондитер
# --  43.02.01 - Организация обслуживания в общественном питании
# --  43.02.02 - Парикмахерское искусство
# --  43.02.03 - Стилистика и искусство визажа
# --  43.02.04 - Прикладная эстетика
# --  43.02.05 - Флористика
# --  43.02.06 - Сервис на транспорте (по видам транспорта)
# --  43.02.07 - Сервис по химической обработке изделий
# --  43.02.08 - Сервис домашнего и коммунального хозяйства
# --  43.02.09 - Ритуальный сервис
# --  43.02.10 - Туризм
# --  43.02.11 - Гостиничный сервис
# --  43.02.12 - Технология эстетических услуг
# --  43.02.13 - Технология парикмахерского искусства
# --  43.02.14 - Гостиничное дело
# --  43.02.15 - Поварское и кондитерское дело
# 33) Образование и педагогические науки
# --  44.02.01 - Дошкольное образование
# --  44.02.02 - Преподавание в начальных классах
# --  44.02.03 - Педагогика дополнительного образования
# --  44.02.04 - Специальное дошкольное образование
# --  44.02.05 - Коррекционная педагогика в начальном образовании
# --  44.02.06 - Профессиональное обучение (по отраслям)
# 34) История и археология
# --  46.01.01 - Секретарь
# --  46.01.02 - Архивариус
# --  46.01.03 - Делопроизводитель
# --  46.02.01 - Документационное обеспечение управления и архивоведение
# 35) Физическая культура и спорт
# --  49.02.01 - Физическая культура
# --  49.02.02 - Адаптивная физическая культура
# --  49.02.03 - Спорт
# 4) Информатика и вычислительная техника
# --  09.01.01 - Наладчик аппаратного и программного обеспечения
# --  09.01.02 - Наладчик компьютерных сетей
# --  09.01.03 - Оператор информационных систем и ресурсов
# --  09.02.01 - Компьютерные системы и комплексы
# --  09.02.02 - Компьютерные сети
# --  09.02.03 - Программирование в компьютерных системах
# --  09.02.04 - Информационные системы (по отраслям)
# --  09.02.05 - Прикладная информатика (по отраслям)
# --  09.02.06 - Сетевое и системное администрирование
# --  09.02.07 - Информационные системы и программирование
# 5) Информационная безопасность
# --  10.02.01 - Организация и технология защиты информации
# --  10.02.02 - Информационная безопасность телекоммуникационных систем
# --  10.02.03 - Информационная безопасность автоматизированных систем
# --  10.02.04 - Обеспечение информационной безопасности телекоммуникационных систем
# --  10.02.05 - Обеспечение информационной безопасности автоматизированных систем
# 6) Электроника, радиотехника и системы связи
# --  11.01.01 - Монтажник радиоэлектронной аппаратуры и приборов
# --  11.01.02 - Радиомеханик
# --  11.01.03 - Радиооператор
# --  11.01.04 - Монтажник оборудования радио- и телефонной связи
# --  11.01.05 - Монтажник связи
# --  11.01.06 - Электромонтер оборудования электросвязи и проводного вещания
# --  11.01.07 - Электромонтер по ремонту линейно-кабельных сооружений телефонной связи и проводного вещания
# --  11.01.08 - Оператор связи
# --  11.01.09 - Оператор микроэлектронного производства
# --  11.01.10 - Оператор оборудования элионных процессов
# --  11.01.11 - Наладчик технологического оборудования (электронная техника)
# --  11.01.12 - Сборщик изделий электронной техники
# --  11.01.13 - Сборщик приборов вакуумной электроники
# --  11.02.01 - Радиоаппаратостроение
# --  11.02.02 - Техническое обслуживание и ремонт радиоэлектронной техники (по отраслям)
# --  11.02.03 - Эксплуатация оборудования радиосвязи и электрорадионавигации судов
# --  11.02.04 - Радиотехнические комплексы и системы управления космических летательных аппаратов
# --  11.02.05 - Аудиовизуальная техника
# --  11.02.06 - Техническая эксплуатация транспортного радиоэлектронного оборудования (по видам транспорта)
# --  11.02.07 - Радиотехнические информационные системы
# --  11.02.08 - Средства связи с подвижными объектами
# --  11.02.09 - Многоканальные телекоммуникационные системы
# --  11.02.10 - Радиосвязь, радиовещание и телевидение
# --  11.02.11 - Сети связи и системы коммутации
# --  11.02.12 - Почтовая связь
# --  11.02.13 - Твердотельная электроника
# --  11.02.14 - Электронные приборы и устройства
# --  11.02.15 - Инфокоммуникационные сети и системы связи
# --  11.02.16 - Монтаж, техническое обслуживание и ремонт электронных приборов и устройств
# 7) Фотоника, приборостроение, оптические и биотехнические системы и технологии
# --  12.01.01 - Наладчик оборудования оптического производства
# --  12.01.02 - Оптик-механик
# --  12.01.03 - Сборщик очков
# --  12.01.04 - Электромеханик по ремонту и обслуживанию наркознодыхательной аппаратуры
# --  12.01.05 - Электромеханик по ремонту и обслуживанию медицинского оборудования
# --  12.01.06 - Электромеханик по ремонту и обслуживанию медицинских оптических приборов
# --  12.01.07 - Электромеханик по ремонту и обслуживанию электронной медицинской аппаратуры
# --  12.01.08 - Механик протезно-ортопедических изделий
# --  12.01.09 - Мастер по изготовлению и сборке деталей и узлов оптических и оптико-электронных приборов и систем
# --  12.02.01 - Авиационные приборы и комплексы
# --  12.02.02 - Акустические приборы и системы
# --  12.02.03 - Радиоэлектронные приборные устройства
# --  12.02.04 - Электромеханические приборные устройства
# --  12.02.05 - Оптические и оптико-электронные приборы и системы
# --  12.02.06 - Биотехнические и медицинские аппараты и системы
# --  12.02.07 - Монтаж, техническое обслуживание и ремонт медицинской техники
# --  12.02.08 - Протезно-ортопедическая и реабилитационная техника
# --  12.02.09 - Производство и эксплуатация оптических и оптико-электронных приборов и систем
# --  12.02.10 - Монтаж, техническое обслуживание и ремонт биотехнических и медицинских аппаратов и систем

# 20) Управление в технических системах
# --  27.02.01 - Метрология
# --  27.02.02 - Техническое регулирование и управление качеством
# --  27.02.03 - Автоматика и телемеханика на транспорте (железнодорожном транспорте)
# --  27.02.04 - Автоматические системы управления
# --  27.02.05 - Системы и средства диспетчерского управления
# --  27.02.06 - Контроль работы измерительных приборов
# --  27.02.07 - Управление качеством продукции, процессов и услуг

def YouAreRealWalterWhite():
    print("")

    choice = input("Введите номер ответа: ")

    if choice == "1":
        ()
    elif choice == "2":
        ()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        ()

# 22) Клиническая медицина
# --  31.02.01 - Лечебное дело
# --  31.02.02 - Акушерское дело
# --  31.02.03 - Лабораторная диагностика
# --  31.02.04 - Медицинская оптика
# --  31.02.05 - Стоматология ортопедическая
# --  31.02.06 - Стоматология профилактическая
# 23) Науки о здоровье и профилактическая медицина
# --  32.02.01 - Медико-профилактическое дело
# 24) Фармация
# --  33.02.01 - Фармация
# --  33.02.02 - Страховое дело (по отраслям)
# 25) Сестринское дело
# --  34.01.01 - Младшая медицинская сестра по уходу за больными
# --  34.02.01 - Сестринское дело
# --  34.02.02 - Медицинский массаж (для обучения лиц с ограниченными возможностями здоровья по зрению)
# 27) Ветеринария и зоотехния
# --  36.01.01 - Младший ветеринарный фельдшер
# --  36.01.02 - Мастер животноводства
# --  36.01.03 - Тренер-наездник лошадей
# --  36.02.01 - Ветеринария
# --  36.02.02 - Зоотехния

def prosnulsia_na_rabote():
    print("Вы предпочтёте :")
    print("1.Создавать мультимедийные,музыкальные, сценические произведения искусства")
    print("2.Заниматься созданием предметов одежды")
    print("3.Снабжать заводы и города энергией")
    print("4.Создавать и(или) управлять транспортными средствами")

    choice = input("Введите номер выбора: ")

    if choice == "1":
        art()
    elif choice == "2":
        industry()
    elif choice == "3":
        Energetic()
    elif choice == "4":
        Build_Transport()

def industry():
    print("вы бы предпочли:")
    print("1.изучать взаимосвязь между составом, строением и свойствами материалов")
    print("2.отвечать за технологию создания изделий лёгкой промышленности(одежда)")
    choice = input("Введите номер ответа: ")

    if choice == "1":
        tech_mater()
    elif choice == "2":
        easy_prom()

# 15) Технологии материалов
# --  22.01.01 - Доменщик
# --  22.01.02 - Сталеплавильщик (по типам производства)
# --  22.01.03 - Машинист крана металлургического производства
# --  22.01.04 - Контролер металлургического производства
# --  22.01.05 - Аппаратчик-оператор в производстве цветных металлов
# --  22.01.06 - Оператор-обработчик цветных металлов
# --  22.01.07 - Модельщик
# --  22.01.08 - Оператор прокатного производства
# --  22.01.09 - Оператор трубного производства
# --  22.01.10 - Оператор в производстве огнеупоров
# --  22.02.01 - Металлургия черных металлов
# --  22.02.02 - Металлургия цветных металлов
# --  22.02.03 - Литейное производство черных и цветных металлов
# --  22.02.04 - Металловедение и термическая обработка металлов
# --  22.02.05 - Обработка металлов давлением
# --  22.02.06 - Сварочное производство
# --  22.02.07 - Порошковая металлургия, композиционные материалы, покрытия
# 21) Технологии легкой промышленности
# --  29.01.01 - Скорняк
# --  29.01.02 - Обувщик (широкого профиля)
# --  29.01.03 - Сборщик обуви
# --  29.01.04 - Художник по костюму
# --  29.01.05 - Закройщик
# --  29.01.06 - Раскройщик материалов
# --  29.01.07 - Портной
# --  29.01.08 - Оператор швейного оборудования
# --  29.01.09 - Вышивальщица
# --  29.01.10 - Модистка головных уборов
# --  29.01.11 - Контролер качества текстильных изделий
# --  29.01.12 - Оператор крутильного оборудования (для всех видов производств)
# --  29.01.13 - Оператор оборудования чесального производства (для всех видов производств)
# --  29.01.14 - Оператор прядильного производства
# --  29.01.15 - Раклист
# --  29.01.16 - Ткач
# --  29.01.17 - Оператор вязально-швейного оборудования
# --  29.01.18 - Вязальщица текстильно-галантерейных изделий
# --  29.01.19 - Оператор производства нетканых материалов
# --  29.01.20 - Красильщик (общие профессии производства текстиля)
# --  29.01.21 - Оператор оборудования отделочного производства (общие профессии производства текстиля)
# --  29.01.22 - Аппаратчик отделочного производства (общие профессии производства текстиля)
# --  29.01.23 - Наладчик полиграфического оборудования
# --  29.01.24 - Оператор электронного набора и верстки
# --  29.01.25 - Переплетчик
# --  29.01.26 - Печатник плоской печати
# --  29.01.27 - Мастер печатного дела
# --  29.01.28 - Огранщик алмазов в бриллианты
# --  29.01.29 - Мастер столярного и мебельного производства
# --  29.01.30 - Обойщик мебели
# --  29.02.01 - Конструирование, моделирование и технология изделий из кожи
# --  29.02.02 - Технология кожи и меха
# --  29.02.03 - Конструирование, моделирование и технология изделий из меха
# --  29.02.04 - Конструирование, моделирование и технология швейных изделий
# --  29.02.05 - Технология текстильных изделий (по видам)
# --  29.02.06 - Полиграфическое производство
# --  29.02.07 - Производство изделий из бумаги и картона
# --  29.02.08 - Технология обработки алмазов
# --  29.02.09 - Печатное дело

def Energetic():
    print("вы предпочтёте заниматься:")
    print("1.Изучать ядерную энергетику и тхнологии")
    print("2.Изучать электро и теплоэнергетику")
    choice = input("Введите номер ответа: ")

    if choice == "1":
        electro()
    elif choice == "2":
        nuclear()

# 8) Электро и теплоэнергетика
# --  13.01.01 - Машинист котлов
# --  13.01.02 - Машинист паровых турбин
# --  13.01.03 - Электрослесарь по ремонту оборудования электростанций
# --  13.01.04 - Слесарь по ремонту оборудования электростанций
# --  13.01.05 - Электромонтер по техническому обслуживанию электростанций и сетей
# --  13.01.06 - Электромонтер-линейщик по монтажу воздушных линий высокого напряжения и контактной сети
# --  13.01.07 - Электромонтер по ремонту электросетей
# --  13.01.08 - Сборщик трансформаторов
# --  13.01.09 - Сборщик электрических машин и аппаратов
# --  13.01.10 - Электромонтер по ремонту и обслуживанию электрооборудования (по отраслям)
# --  13.01.11 - Электромеханик по испытанию и ремонту электрооборудования летательных аппаратов
# --  13.01.12 - Сборщик электроизмерительных приборов
# --  13.01.13 - Электромонтажник-схемщик
# --  13.01.14 - Электромеханик по лифтам
# --  13.02.01 - Тепловые электрические станции
# --  13.02.02 - Теплоснабжение и теплотехническое оборудование
# --  13.02.03 - Электрические станции, сети и системы
# --  13.02.04 - Гидроэлектроэнергетические установки
# --  13.02.05 - Технология воды, топлива и смазочных материалов на электрических станциях
# --  13.02.06 - Релейная защита и автоматизация электроэнергетических систем
# --  13.02.07 - Электроснабжение (по отраслям)
# --  13.02.08 - Электроизоляционная, кабельная и конденсаторная техника
# --  13.02.09 - Монтаж и эксплуатация линий электропередачи
# --  13.02.10 - Электрические машины и аппараты
# --  13.02.11 - Техническая эксплуатация и обслуживание электрического и электромеханического оборудования (по отраслям)
# 9) Ядерная энергетика и технологии
# --  14.02.01 - Атомные электрические станции и установки
# --  14.02.02 - Радиационная безопасность
# --  14.02.03 - Технология разделения изотопов

def Build_Transport():
    print("вы предпочтете: ")
    print("1.Изучать Технику, технологии наземного транспорта и машиностроения")
    print("2.Изучать авиационную ракетно-космическую технику")
    print("3.Изучать аэронавигацию и эксплуатацию авиационной и ракетно-космической техники")
    print("4.Изучать Технику и технологии кораблестроения и водного транспорта")
    choice = input("Введите номер ответа: ")

    if choice == "1":
        machine()
    elif choice == "2":
        avio()
    elif choice == "3":
        pilot()
    elif choice == "4":
        ship()

# 16) Техника и технологии наземного транспорта
# --  23.01.01 - Оператор транспортного терминала
# --  23.01.02 - Докер-механизатор
# --  23.01.03 - Автомеханик
# --  23.01.04 - Водитель городского электротранспорта
# --  23.01.05 - Слесарь по ремонту городского электротранспорта
# --  23.01.06 - Машинист дорожных и строительных машин
# --  23.01.07 - Машинист крана (крановщик)
# --  23.01.08 - Слесарь по ремонту строительных машин
# --  23.01.09 - Машинист локомотива
# --  23.01.10 - Слесарь по обслуживанию и ремонту подвижного состава
# --  23.01.11 - Слесарь-электрик по ремонту электрооборудования подвижного состава (электровозов, электропоездов)
# --  23.01.12 - Слесарь-электрик метрополитена
# --  23.01.13 - Электромонтер тяговой подстанции
# --  23.01.14 - Электромонтер устройств сигнализации, централизации, блокировки (СЦБ)
# --  23.01.15 - Оператор поста централизации
# --  23.01.16 - Составитель поездов
# --  23.01.17 - Мастер по ремонту и обслуживанию автомобилей
# --  23.02.01 - Организация перевозок и управление на транспорте (по видам)
# --  23.02.02 - Автомобиле- и тракторостроение
# --  23.02.03 - Техническое обслуживание и ремонт автомобильного транспорта
# --  23.02.04 - Техническая эксплуатация подъемно-транспортных, строительных, дорожных машин и оборудования (по отраслям)
# --  23.02.05 - Эксплуатация транспортного электрооборудования и автоматики (по видам транспорта, за исключением водного)
# --  23.02.06 - Техническая эксплуатация подвижного состава железных дорог
# --  23.02.07 - Техническое обслуживание и ремонт двигателей, систем и агрегатов автомобилей
# 17) Авиационная и ракетно-космическая техника
# --  24.01.01 - Слесарь-сборщик авиационной техники
# --  24.01.02 - Электромонтажник авиационной техники
# --  24.01.03 - Слесарь-механик авиационных приборов
# --  24.01.04 - Слесарь по ремонту авиационной техники
# --  24.02.01 - Производство летательных аппаратов
# --  24.02.02 - Производство авиационных двигателей
# --  24.02.03 - Испытание летательных аппаратов
# 18) Аэронавигация и эксплуатация авиационной и ракетно-космической техники
# --  25.02.01 - Техническая эксплуатация летательных аппаратов и двигателей
# --  25.02.02 - Обслуживание летательных аппаратов горючесмазочными материалами
# --  25.02.03 - Техническая эксплуатация электрифицированных и пилотажно-навигационных комплексов
# --  25.02.04 - Летная эксплуатация летательных аппаратов
# --  25.02.05 - Управление движением воздушного транспорта
# --  25.02.06 - Производство и обслуживание авиационной техники
# --  25.02.07 - Техническое обслуживание авиационных двигателей
# --  25.02.08 - Эксплуатация беспилотных авиационных систем
def art():
    print("вы предпочтёте:")
    print("1.Изучать мировую культуру")
    print("2.создавать сценарии фильмов и спецэффекты для них")
    print("3.")
    print("4.")
    choice = input("Введите номер ответа: ")
    if choice == "1":
        history()
    elif choice == "2":
        media()
    elif choice == "3":
        music()
    elif chjice == "4":
        picture()

def media():
    print("")

    choice = input("Введите номер ответа: ")

    if choice == "1":
        ()
    elif choice == "2":
        ()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        ()

def music():
    print("")

    choice = input("Введите номер ответа: ")

    if choice == "1":
        ()
    elif choice == "2":
        ()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        ()

def picture():
    print("")

    choice = input("Введите номер ответа: ")

    if choice == "1":
        ()
    elif choice == "2":
        ()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        ()

# 36) Искусствознание
# --  50.02.01 - Мировая художественная культура
# 37) Культуроведение и социокультурные проекты
# --  51.02.01 - Народное художественное творчество (по видам)
# --  51.02.02 - Социально-культурная деятельность (по видам)
# --  51.02.03 - Библиотековедение
# 38) Сценические искусства и литературное творчество
# --  52.02.01 - Искусство балета
# --  52.02.02 - Искусство танца (по видам)
# --  52.02.03 - Цирковое искусство
# --  52.02.04 - Актерское искусство
# --  52.02.05 - Искусство эстрады
# 39) Музыкальное искусство
# --  53.02.01 - Музыкальное образование
# --  53.02.02 - Музыкальное искусство эстрады (по видам)
# --  53.02.03 - Инструментальное исполнительство (по видам инструментов)
# --  53.02.04 - Вокальное искусство
# --  53.02.05 - Сольное и хоровое народное пение
# --  53.02.06 - Хоровое дирижирование
# --  53.02.07 - Теория музыки
# --  53.02.08 - Музыкальное звукооператорское мастерство
# --  53.02.09 - Театрально-декорационное искусство (по видам)
# 40) Изобразительное и прикладные виды искусств
# --  54.01.01 - Исполнитель художественно-оформительских работ
# --  54.01.02 - Ювелир
# --  54.01.03 - Фотограф
# --  54.01.04 - Мастер народных художественных промыслов
# --  54.01.05 - Изготовитель художественных изделий из тканей с художественной росписью
# --  54.01.06 - Изготовитель художественных изделий из металла
# --  54.01.07 - Изготовитель художественных изделий из керамики
# --  54.01.08 - Художник декоративной росписи по металлу
# --  54.01.09 - Художник росписи по эмали
# --  54.01.10 - Художник росписи по дереву
# --  54.01.11 - Художник росписи по ткани
# --  54.01.12 - Художник миниатюрной живописи
# --  54.01.13 - Изготовитель художественных изделий из дерева
# --  54.01.14 - Резчик
# --  54.01.15 - Инкрустатор
# --  54.01.16 - Лепщик-модельщик архитектурных деталей
# --  54.01.17 - Реставратор строительный
# --  54.01.18 - Реставратор тканей, гобеленов и ковров
# --  54.01.19 - Реставратор памятников каменного и деревянного зодчества
# --  54.01.20 - Графический дизайнер
# --  54.02.01 - Дизайн (по отраслям)
# --  54.02.02 - Декоративно-прикладное искусство и народные промыслы (по видам)
# --  54.02.03 - Художественное оформление изделий текстильной и легкой промышленности
# --  54.02.04 - Реставрация
# --  54.02.05 - Живопись (по видам)
# --  54.02.06 - Изобразительное искусство и черчение
# --  54.02.07 - Скульптура
# --  54.02.08 - Техника и искусство фотографии
# 41) Экранные искусства
# --  55.01.01 - Киномеханик
# --  55.02.01 - Театральная и аудиовизуальная техника (по видам)
# --  55.02.02 - Анимация (по видам)

# def ():
#     print("")
#
#     choice = input("Введите номер ответа: ")
#
#     if choice == "1":
#         ()
#     elif choice == "2":
#         ()

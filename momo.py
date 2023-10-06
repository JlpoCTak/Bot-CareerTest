GLINOMES = 0
InfTechnology = 0
Energetic = 0
Builder = 0
Promishlennost = 0
Build_Transport = 0
Med_science = 0
I_see_you_hate_people = 0
stick_stick_man = 0

def viberi_ulicu_pls():                     #попытка отсечь как можно больше профессий друг от друга
    print("вы предпочтёте работать:")
    print("1.на улице")
    print("2.в офисе")
    print("3.в мастерской")

    choice = input("Введите номер ответа: ")            #мама выгнала на улицу
    if choice == "1":
        GLINOMES += 1
        Builder += 1
        GLINOMESi()
    elif choice == "2":                         #обиженных закрыли в комнате
        informationalTechnology+=1
        Energetic+=1
        I_see_you_hate_people+=1
        Med_science += 1
        Builder += 1
        popal_v_office()
    elif choice == "3":                          #мама сказал у тебя круто получилось нарисовать палочку
         stick_stick_man += 1
         Promishlennost += 1
         Energetic += 1
         Build_Transport +=1
         prosnulsia_na_rabote()

def GLINOMESi():
    print("Вы бы хотели изучать")
    print("1.Земные породы, архитуктуры")
    print("2.преобразованием химчских элементов, ")
    choice = input("Введите номер ответа: ")                    #глиномесы и строители

    if choice == "1":
        GLINOMES += 1
        Gorlovka_vibrala_tebia()                     #земные науки
    elif choice == "2":
        Builder += 1
        YouAreWalterWhite()                           #хим науки

def Gorlovka_vibrala_tebia():
    print("вы предпочтёте ")
    print("1.обрабатывать землю")
    print("2.изучать земные и горные породы и газы")
    choice = input("Введите номер ответа: ")
    if choice == "1":
        geology()
    elif choice == "2":
        hoz()

                                        #       Прикладная геология, горное дело, нефтегазовое дело и геодезия,
                                        #       Сельское, лесное и рыбное хозяйство,

def geology():
    print("вы предпочтете:")
    print("1.Составлять карты морей и суши, изучать движения, распеределение воды в природе")
    print("2.Изучать погодные явления на Земле, состав воздуха и составлять прогнозы погоды")
    choice = input("Введите номер ответа: ")

    if choice == "1":
        kartograf()
    elif choice == "2":
        meteorolog()

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

def YouAreWalterWhite():
    print("вы предпочтёте:")
    print("1.Проектировать здания")
    print("2.Управлять химическими технологиями")
    print("3.Производить пищевую продукцию")
    print("4.защищать и предотвращать  от ЧС человека и природу")
    choice = input("Введите номер ответа: ")
    if choice == "1":
        arhitec()
    elif choice == "2":
        chem_tech()
    elif choice == "3":
        povar()
    elif choice == "4":
        fireman()

# архитектура
# 11)Химические технологии
#     12)Промышленная экология и биотехнологии
#     13)Техносферная безопасность и природообустройство

def popal_v_office():
    print("вы бы предпочли:")
    print("1.заниматься бумажной работой")
    print("2.Отслеживать изменения химических элементов, следить за качеством строй-химических материалов")

    choice = input("Введите номер ответа: ")

    if choice == "1":
        I_see_you_hate_people += 1
        informationalTechnology += 1
        Energetic += 1

        bumaga()
    elif choice == "2":
        Med_science += 1
        Builder += 1
        Energetic += 1
        YouAreRealWalterWhite()

def popal_v_office():
    print("вы бы предпочли:")
    print("1.")
     print("2.")

     choice = input("Введите номер ответа: ")

    if choice == "1":
        ()
    elif choice == "2":
        ()

        # informationalTechnology += 1
        # Energetic += 1
        # I_see_you_hate_people += 1
        # Med_science += 1
        # Builder += 1

def prosnulsia_na_rabote():
    print("Вы предпочтёте :")
    print("1.Создавать мультимедийные,музыкальные, сценические произведения искусства")
    print("2.Заниматься созданием предметов одежды")
    print("3.Снабжать заводы и города энергией")
    print("4.Создавать и(или) управлять транспортными средствами")

    choice = input("Введите номер выбора: ")

    if choice == "1":
        stick_stick_man()
    elif choice == "2":
        Promishlennost()
    elif choice == "3":
        Energetic()
    elif choice == "4":
        Build_Transport()

def stick_stick_man():
    print("вас интересует история искусств или вы хотите создавать свои произведения искусств:")
    print("1.Да, меня интересует история")
    print("2.Нет, я хочу создавать картины, сценарии фильмов и спецэффекты для них")
    print("3.я хочу написать собственную песню или книгу")
    choice = input("Введите номер ответа: ")

    if choice == "1":
        history()
    elif choice == "2":
        media()
    elif choice == "3":
        music()
    elif chjice == "4":
        picture()

#     36)Искусствознание
#     37)Культуроведение и социокультурные проекты
#     38)Сценические искусства и литературное творчество
#     39)Музыкальное искусство
#     40)Изобразительное и прикладные виды искусств
#     41)Экранные искусства

def Promishlennost():
    print("вы бы предпочли:")
    print("1.изучать взаимосвязь между составом, строением и свойствами материалов")
    print("2.отвечать за технологию создания изделий лёгкой промышленности(одежда)")
    choice = input("Введите номер ответа: ")

    if choice == "1":
        tech_mater()
    elif choice == "2":
        easy_prom()

    # 15)Технологии
    # материалов
    # 21)Технологии
    # легкой
    # промышленности

def Energetic():
    print("вы предпочтёте заниматься:")
    print("1.Изучать ядерную энергетику и тхнологии")
    print("2.Изучать электро и теплоэнергетику")
    choice = input("Введите номер ответа: ")

    if choice == "1":
        electro()
    elif choice == "2":
        nuclear()

def Build_Transport():
    print("вы предпочтете: ")
    print("1.Изучать Технику, технологии наземного транспорта и машиностроения")
    print("2.Изучать авиационную ракетно-космическую технику")
    print("3.Изучать аэронавигацию и эксплуатацию авиационной и ракетно-космической техники")
    print("4.Изучать Технику и технологии кораблестроения и водного транспорта")
    choice = input("Введите номер ответа: ")

    if choice == "1":
        ()
    elif choice == "2":
        avio()
    elif choice == "3":
        pilot()
    elif choice == "4":
        ship()

# def ():
#     print("")
#
#     choice = input("Введите номер ответа: ")
#
#     if choice == "1":
#         ()
#     elif choice == "2":
#         ()
#     else:
#         print("Некорректный выбор. Попробуйте еще раз.")
#         ()
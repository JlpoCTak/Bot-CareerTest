GLINOMES = 0
InfTechnology = 0
Energetic = 0
Builder = 0
Promishlennost = 0
Build_Transport = 0
Med_science = 0
I_see_you_hate_people = 0
stick_stick_man = 0

def viberi_ulicu_pls():                 #попытка отсечь как можно больше профессий друг от друга
    print("вы предпочтёте работать:")
    print("1.на улице")
    print("2.в офисе")
    print("3.в мастерской")

    choice = input("Введите номер ответа: ") #мама выгнала на улицу
    if choice == "1":
        GLINOMES += 1
        Builder += 1
        GLINOMES()

    elif choice == "2":                         #обиженных закрыли в комнате
        informationalTechnology+=1
        Energetic+=1
        I_see_you_hate_people+=1
        Med_science += 1
        Builder += 1
        popal_v_office()

    elif choice == "3":             #мама сказал у тебя круто получилось нарисовать палочку
         stick_stick_man += 1
         Promishlennost += 1
         Energetic += 1
         Build_Transport +=1
         prosnulsia_na_rabote()

    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        viberi_ulicu_pls()

def GLINOMES():
    print("Вы бы хотели изучать")
    print("1.Земные породы, архитуктуры")
    print("2.преобразованием химчских элементов, ")
    choice = input("Введите номер ответа: ")                    #глиномесы и строители

    if choice == "1":
                Gorlovka_bibrala_tebia()             #земные науки
    elif choice == "2":
                YouAreWalterWhite()                  #хим науки
    else:
                print("Некорректный выбор. Попробуйте еще раз.")
                GLINOMES()

def Gorlovka_vibrala_tebia():
    choice = input("Введите номер ответа: ")
    if choice == "1":
        architec()
    elif choice == "2":
        geology()
    elif choice == "3":
        hoz()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        Gorlovka_vibrala_tebia()

                #       Архитектура,
                #       Прикладная геология, горное дело, нефтегазовое дело и геодезия,
                #       Сельское, лесное и рыбное хозяйство,






def YouAreWalterWhite():
    choice = input("Введите номер ответа: ")
    if choice == "1":
                ()
    elif choice == "2":
                ()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        YouAreWalterWhite()




def popal_v_office():
    print("вы бы предпочли:")
    print("1.заниматься бумажной работой")
    print("2.Отслеживать изменения химических элементов, следить за качеством строй-хмических материалов")

        # informationalTechnology += 1
        # Energetic += 1
        # I_see_you_hate_people += 1
        # Med_science += 1
        # Builder += 1


    choice = input("Введите номер ответа: ")

    if choice == "1":
        bumaga()
    elif choice == "2":
        YouAreRealWalterWhite()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        popal_v_office()

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
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        prosnulsia_na_rabote()
def stick_stick_man():
    print("вас интересует история искусств или вы хотите создавать свои произведения искусств:")
    print("1.Да, меня интересует история")
    print("2.Нет, я хочу создавать картины, сценарии фильмов и спецэффекты для них")
    print("3.я хочу написать собственную песню или книгу")
    choice = input("Введите номер ответа: ")

    if choice == "1":
        histiry()
    elif choice == "2":
        multimedia()
    elif choice == "3":
        music()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        ()
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
    # 15)Технологии
    # материалов
    # 21)Технологии
    # легкой
    # промышленности
    choice = input("Введите номер ответа: ")

    if choice == "1":
        tech_mater()
    elif choice == "2":
        easy_prom()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        Promishlennost()
def Energetic():
    print("")

    choice = input("Введите номер ответа: ")

    if choice == "1":
        electro()
    elif choice == "2":
        nuclear()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        Energetic()
def Build_Transport():
    print("вы предпочтете: ")
    print("1.изучать технологии создания,ремонта и сервиса наземного, водного и летательного транспорта")
    print("2.эксплуатировать ракетно-комический транспорт")

    choice = input("Введите номер ответа: ")

    if choice == "1":
        creater()
    elif choice == "2":
        pilot()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        Build_Transport()
#def ():
    # print("")
    #
    # choice = input("Введите номер ответа: ")
    #
    # if choice == "1":
    #     ()
    # elif choice == "2":
    #     ()
    # else:
    #     print("Некорректный выбор. Попробуйте еще раз.")
    #     ()
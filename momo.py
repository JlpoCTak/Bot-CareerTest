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
    print("1. на улице")
    print("2. в офисе")
    print("3. в мастерской")

    choice = input("Введите номер ответа: ") #мама выгнала на улицу
    if choice == "1":
        GLINOMES+=1
        Builder
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
        prologue()

def GLINOMES():
    print("Вы бы хотели изучать")
    print("1.Земные породы, архитуктуры")
    print("2.преобразованием химчских элементов, ")
    choice = input("Введите номер ответа: ")                    #глиномесы и строители

    if choice == "1":
        take_key()
    elif choice == "2":
        look_out_of_window()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        inspect_room()

def popal_v_office():
    print("")

    choice = input("Введите номер выбора: ")

    if choice == "1":
        ()
    elif choice == "2":
        ()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        stay_in_bed()

def prosnulsia_na_rabote():
    print("")

    choice = input("Введите номер выбора: ")

    if choice == "1":
        ()
    elif choice == "2":
        ()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        ()

def ():
    print("Вы подходите к окну и заглядываете вниз.")

    choice = input("Введите номер выбора: ")

    if choice == "1":
        ()
    elif choice == "2":
        ()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        ()

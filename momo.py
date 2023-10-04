def ():
    print("")

    choice = input("Введите номер ответа: ")

    if choice == "1":
        inspect_room()
    elif choice == "2":
        stay_in_bed()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        prologue()

def inspect_room():
    print("Вы осматриваете комнату и замечаете на столе ключ.")
    print("Что будем делать?")
    print("1. Взять ключ и идти к двери.")
    print("2. Подойти к окну и заглянуть вниз.")

    choice = input("Введите номер выбора: ")

    if choice == "1":
        take_key()
    elif choice == "2":
        look_out_of_window()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        inspect_room()

def stay_in_bed():
    print("Вы остаетесь лежать и начинаете задумываться о своем прошлом.")
    print("Прошлое напоминает о важной задаче, которую нужно выполнить.")
    print("Что будем делать?")
    print("1. Встать и начать выполнять задачу.")
    print("2. Остаться лежать и отложить задачу на потом.")

    choice = input("Введите номер выбора: ")

    if choice == "1":
        start_task()
    elif choice == "2":
        postpone_task()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        stay_in_bed()

def take_key():
    print("Вы берете ключ себе и направляетесь к двери.")
    print("Как вы будете открывать дверь?")
    print("1. Вставить ключ в замочную скважину и повернуть его.")
    print("2. Попробовать выломать дверь.")

    choice = input("Введите номер выбора: ")

    if choice == "1":
        open_door_with_key()
    elif choice == "2":
        break_door()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        take_key()

def look_out_of_window():


    if choice == "1":
        go_down_stairs()
    elif choice == "2":
        climb_out_of_window()
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        look_out_of_window()

# Далее можно продолжить с различными сценариями и выборами.

prologue()
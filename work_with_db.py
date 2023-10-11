import json
import time

import ijson



def find_college():
    with open('database/republics.txt', 'r', encoding='utf-8') as rep:
<<<<<<< HEAD
        with open('database/db_backup.json', 'r', encoding='utf-8') as file:
            parser = ijson.parse(file)

            # Ищем начало объекта области
            for prefix, event, value in parser:
                if event == 'start_map':
                    republic = prefix
                    print("Область:", republic)

                    # Внутри области ищем города
                    for prefix, event, value in parser:
                        if event == 'start_map':
                            city = prefix
                            print("Город:", city)

                            # Внутри города ищем специальности
                            for prefix, event, value in parser:
                                if event == 'start_map':
                                    specialty = prefix
                                    print("Специальность:", specialty)

                                    # Внутри специальности ищем информацию
                                    for prefix, event, value in parser:
                                        if event == 'string':
                                            if prefix.endswith('.href'):
                                                href = value
                                                print("Ссылка:", href)
                                            else:
                                                code = prefix.split('.')[-1]
                                                print("Код специальности:", code)
                                                print("Описание:", value)

                                            # Здесь вы можете добавить свой код для обработки данных о специальности

                                        # Проверяем, закончили ли мы специальность
                                        elif event == 'end_map':
                                            break

                                # Проверяем, закончили ли мы город
                                elif event == 'end_map':
                                    break

                        # Проверяем, закончили ли мы область
                        elif event == 'end_map':
                            break
=======
        with open('database/db.json', 'r', encoding='utf-8') as file:
            # for i in range(83):
                # republi = rep.readline().strip()  # считываем файл с областями

                # print(republic)
                republic = ijson.parse(file)
                for prefix,event,value in republic:
                    # if event=='map_key' and prefix=='':
                    #     repub = value #название областей
                    # print(prefix,event,value)
                    # if event=='map_key' and value!='':
                    #     print(prefix,event,value)
                    print(prefix)
>>>>>>> 6359c26bc73b935040e67c259737e1e5a6932441

def main():
    find_college()

if __name__=='__main__':
    main()
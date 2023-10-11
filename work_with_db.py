import json
import time

import ijson



def find_college():
    with open('database/republics.txt', 'r', encoding='utf-8') as rep:
        with open('database/db.json', 'r', encoding='utf-8') as file:
            # for i in range(83):
                # republic = rep.readline().strip()  # считываем файл с областями

                # print(republic)
                republic = ijson.parse(file)
                for prefix,event,value in republic:
                    if event=='map_key':
                        print(prefix, event, value)

                        repubs = ijson.kvitems(file, f'{value}.items')  # получаем значение области ключа
                        print(list(repubs))
                # for repu in repubs:
                    # print(list(repu[1]))
                #
                #     cities = list(repu[1]) #списки городов по областям
                #     # print(list(cities))
                #
                #     for city in list(cities):
                #         # print(city)
                #         break
                #         specs = ijson.items(file, f'{repu[0]}')
                        # print(list(specs))
                        # for spec in specs:
                        #     special = list(spec)
                        #     print(special)
                # republics = list(repubs)[0].keys()  # получаем название областей и республик в списке dict_keys
                # try:
                #
                #
                #
                #     # print(republics)
                #     # for republic in republics:  # области поочередно
                #     #     print(republic)
                #         # cities = ijson.items(file, f'{republic}')
                #         # print(cities)
                #         # try:
                #         #     for city in cities:
                #         #         print(city)
                #     pass
                # except ijson.common.IncompleteJSONError:
                #     print('ошибка ijson.common.IncompleteJSONError, вроде не критично')


def main():
    find_college()

if __name__=='__main__':
    main()
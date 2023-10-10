import json
import time

import ijson



def find_college():
    with open('database/republics.txt', 'r', encoding='utf-8') as rep:
        with open('database/db.json', 'r', encoding='utf-8') as file:
            # for i in range(83):
                republic = rep.readline(0)[:-1]  # считываем файл с областями
                i=0
                # print(republic)
                repubs = ijson.kvitems(file, f'{republic}')  # получаем значение области ключа
                # print(repubs)
                for repu in repubs:
                    cities = list(repu[1]) #список городов по областям
                    for city in cities:
                        # print(city)
                        specs = ijson.kvitems(file, f'{republic}.{city}')
                        print(list(specs))
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
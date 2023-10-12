import ijson
from fuzzywuzzy import process
# import Levenshtein
def find_college(id_spec,city_from_user='1'):
    list_of_href = []
    finaly_list_of_href = []
    with open('database/db.json', 'r', encoding='utf-8') as file:
            republic = ijson.parse(file)
            college = '123'
            pref_href = '0'
            pref_id = '1'

            for prefix,event,value in republic:

                # if event=='map_key' and prefix=='':
                #     repub = value #название областей
                strin = prefix,event,value
                # print(strin)
                if "href" in prefix:
                    pref_href = strin[0] # название где ссылка
                    # print(strin)
                    href = strin[-1] # ссылка
                if value==id_spec:
                    pref_id = strin[0] #название где айди
                    # print(pref_id, '++++++++++')
                    id_ = strin[-1] # id

                if pref_id in pref_href:
                    if 'href' in strin:
                        college = strin[0]
                        # print(pref_href)
                        # print(pref_id)
                        # print(college)
                        # print(prefix)
                if pref_id in pref_href:
                    if pref_href[-5:]=='.href':
                        # print(f'{strin[0][0:-5]}:{strin[-1]}')
                        # final = f'{strin[0][0:-5]}:{strin[-1]}'
                        final = f'{pref_href}:{href}'

                        list_of_href.append(final)
    a = list(set(list_of_href))
    list_of_href = a

    # return len(list_of_href)
    if city_from_user!='1':
        for hrefs in list_of_href:
            if city_from_user in hrefs:
                finaly_list_of_href.append(hrefs)
            # else:
            #     return 'Вашей специальности нет в данном городе'
        for href in finaly_list_of_href:
            if city_from_user in href:
                return finaly_list_of_href
            else:
                return 'Вашей спеальности нет в данном городе'
    else:
        return list_of_href



# print(find_college('23.02.04'))

def search_city(city_from_user):
    with open('database/cities.txt','r',encoding='utf-8') as file:
        cities = []
        for i in range(1423):
            a = file.readline()
            cities.append(a[:-1])
        find = process.extractOne(city_from_user,cities)
        return find[0]


# for x in ints_list: if ints_list.count(x) > 1: ints_list.remove(x)
print(find_college('08.02.02',search_city('Ростов-на-')))
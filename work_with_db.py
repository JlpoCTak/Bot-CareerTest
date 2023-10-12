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
                    pref_href = strin[0]
                    # print(pref_href)
                if value==id_spec:
                    pref_id = strin[0]
                    # print(pref_id, '++++++++++')

                if pref_id in pref_href:
                    if 'href' in strin:
                        college = strin[0]
                        # print(pref_href)
                        # print(pref_id)
                if college in prefix:
                    if prefix[-5:]=='.href':
                        # print(f'{strin[0][0:-5]}:{strin[-1]}')
                        final = f'{strin[0][0:-5]}:{strin[-1]}'
                        list_of_href.append(final)
    # return list_of_href
    # if city_from_user!=1:
    #     for hrefs in list_of_href:
    #         if city_from_user in hrefs:
    #             finaly_list_of_href.append(hrefs)
    #     for href in finaly_list_of_href:
    #         if city_from_user in href:
    #             return finaly_list_of_href
    #         else:
    #             return 'Вашей спеальности нет в данном городе'
    # else:
    #     return list_of_href



# print(find_college('23.02.04'))

def search_city(city_from_user):
    with open('database/cities.txt','r',encoding='utf-8') as file:
        cities = []
        for i in range(1423):
            a = file.readline()
            cities.append(a[:-1])
        find = process.extractOne(city_from_user,cities)
        return find[0]


# print()
print(find_college('31.02.01',search_city('Ростов-на-дону')))
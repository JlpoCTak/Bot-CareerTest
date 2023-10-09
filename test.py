import mechanicalsoup
import json
import time
from config import *
# {
#     city:{
#         college1:[{'id_kval': 'name_kval'},{'id_kval': 'name_kval'},{'id_kval': 'name_kval'}]
#         college2:{'id_kval': 'name_kval'}
#         college3:{'id_kval': 'name_kval'}
#     }
# }

def connection_page_cities():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url_cities)
    page = browser.page
    return page


def find_cities(page_city):
    sections = page_city.find_all('div', 'col l9 s12')
    with open('database/db.json', 'w', encoding='utf-8') as file:
        i = 1
        all_dict = {}

        # json.dump({},file,ensure_ascii=False,indent=4)
        for section in sections:
            sect = section.find_all('section')

            for s in sect:
                dict_repub = {}
                republics = s.find_all('b')
                section_cities = s.find_all('ul')
                # print(section_cities)
                time.sleep(1)
                for republic in republics:

                    r = republic.getText()
                    # print(f'{i}){r}:')
                    #file.write(f'{i}){r}:\n')
                    i += 1
                    for cities in section_cities:
                        city = cities.find_all('a')
                        time.sleep(1)
                        dict_city = {}
                        for ci in city:
                            c = ci.getText()
                            time.sleep(2)
                            city_url = ci.get('href')
                            #file.write(f'\t {c}:  \n')

                            browser = mechanicalsoup.StatefulBrowser()
                            browser.open(f'{url_without_specs}{city_url}')
                            page = browser.page
                            # print(f'\t{c}:')
                            colleges_names = page.find_all('p', 'unit-name')
                            dict_college ={}
                            for href_college_unit in colleges_names:
                                content_college = href_college_unit.find('a')
                                spec_id = 0
                                spec_name = ''
                                href_college = content_college.get('href')
                                time.sleep(2)
                                open_college_page = mechanicalsoup.StatefulBrowser()
                                open_college_page.open(f'{url_without_specs}{href_college}')
                                college_page = open_college_page.page
                                college_name_content = college_page.find_all('div', 'card-content')
                                dict_spec = {}
                                time.sleep(1)
                                for college_name_tag in college_name_content:
                                    time.sleep(1.5)
                                    if college_name_tag.find('h1') is not None:
                                        college_name = college_name_tag.find('h1').getText()
                                        # print(f'\t\t{college_name}:')
                                        #file.write(f'\t\t{college_name}:\n')
                                        college_spec_tag = college_page.find('section', id='lic_okso')
                                        college_s_href = college_page.find('div', 'row contacts')
                                        if college_s_href is not None:

                                            college_site_href = college_s_href.find('a', target='_blank')
                                            if college_s_href.find('a', target='_blank') is not None:
                                                college_sit_href = college_site_href.get('href')
                                                dict_spec['href'] = f'{college_sit_href}'

                                        if college_spec_tag is not None:
                                            # print(college_spec_tag.find_all('tr'))
                                            for test in college_spec_tag.find_all('tr'):

                                                string_id_spec_kval = test.find_all('td')
                                                # print(string_id_spec_kval)
                                                j = 0
                                                for string_id in string_id_spec_kval:
                                                    if j != 2:
                                                        if j == 0:
                                                            spec_id = string_id.getText()
                                                            # print(f'\t\t\t{spec_id} ',end='')
                                                            #file.write(f'\t\t\t{spec_id} ')
                                                        elif j == 1:
                                                            spec_name = string_id.getText()
                                                            # print(f'{spec_name} ', end='')
                                                            #file.write(f'{spec_name} ')
                                                        else:
                                                            pass
                                                            # print()
                                                            #file.write(f'\n')
                                                        j+=1
                                                        dict_spec[f'{spec_id}'] = f'{spec_name}'
                                dict_college[f'{college_name}'] = dict_spec
                            dict_city[f'{c}'] = dict_college
                        dict_repub[f'{r}'] = dict_city
                        json.dump(dict_repub, file, ensure_ascii=False, indent=4)


                time.sleep(2)
                open_college_page.close()

            time.sleep(2)
            browser.close()



def main():
    find_cities(connection_page_cities())
    # write_data_in_file(connection_page_specs())


if __name__ == '__main__':
    main()

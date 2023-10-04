import functools

from config import *
import mechanicalsoup
from pysondb import db

def connection_page_specs():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url)
    page = browser.page
    return page

def connection_page_cities():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url_cities)
    page = browser.page
    return page

def connection_page_colleges_in_cities():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url_without_specs)
    page = browser.page
    return page
def write_data_in_file(page):
    specs = page.find_all('ul', id = 'specs')
    for spec in specs:
        s = spec.find_all('li')
        j=0
        test = (s[1].find('a').get('href'))
        print(test)
        print(f'{url_without_specs}{test}')

        with open('/database/specs.txt', 'w', encoding='utf-8') as file:
            for i in range(620):
                kod = (s[i].find_all('span'))
                name = (s[i].find_all('a'))

                if s[i].find_all('span')==[]:

                    file.write(f'{j+1}) {s[i].getText()} \n')
                    j+=1
                else:

                    for text_name in name:

                        for text_kod in kod:
                            file.write(f'--  {text_kod.getText()} - {text_name.getText()} \n')


def find_cities(page_city):
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(f'{url_without_specs}/1/24')
    page = browser.page

    colleges_names = page.find_all('p', 'unit-name')


    for href_college_unit in colleges_names:
        content_college = href_college_unit.find('a')

        for college_unit_name in content_college:
            college_name = college_unit_name.getText()
            # href_college = college_unit_name.get('href')
            print(content_college)


        page_college = browser.open(f'{url_without_specs}')
    # sections = page_city.find_all('div', 'col l9 s12')
    # with open('database/cities.txt', 'w', encoding='utf-8') as file:
    #     i=1
    #     for section in sections:
    #         sect = section.find_all('section')
    #         for s in sect:
    #             republics = s.find_all('b')
    #             section_cities = s.find_all('ul')
    #             # print(section_cities)
    #
    #             for republic in republics:
    #                 r = republic.getText()
    #
    #                 file.write(f'{i}){r}:\n')
    #                 i+=1
    #                 for cities in section_cities:
    #                     city = cities.find_all('a')
    #
    #                     for ci in city:
    #                         c = ci.getText()
    #
    #                         print(ci.get('href'))
    #                         file.write(f'\t {c}  \n')
    #                         college_url = ci.get('href')
    #                         browser = mechanicalsoup.StatefulBrowser()
    #                         browser.open(f'{url_without_specs}{college_url}')
    #                         page = browser.page
    #
    #                         colleges_names = page.find_all('p', 'unit-name')
    #
    #                         for college_unit_name in colleges_names:
    #                             print(college_unit_name.getText())
















def main():
    find_cities(connection_page_cities())
    # write_data_in_file(connection_page_specs())


if __name__ == '__main__':
    main()

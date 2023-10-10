
import time
from config import *
import mechanicalsoup



def connection_page_specs():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url)
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
        # test = (s[1].find('a').get('href'))
        # print(test)
        # print(f'{url_without_specs}{test}')

        with open('database/specs.txt', 'w', encoding='utf-8') as file:
            for i in range(620):
                kod = (s[i].find_all('span'))
                name = (s[i].find_all('a'))
                time.sleep(0.1)
                if s[i].find_all('span')==[]:

                    #file.write(f'{j+1}) {s[i].getText()} \n')
                    j+=1
                else:

                    for text_name in name:

                        for text_kod in kod:
                            file.write(f'{text_kod.getText()}:{text_name.getText()}\n')

def connection_page_cities():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url_cities)
    page = browser.page
    return page



def find_cities(page_city):

    sections = page_city.find_all('div', 'col l9 s12')
    with open('database/cities.txt', 'w', encoding='utf-8') as file:
        i=1
        for section in sections:
            sect = section.find_all('section')

            for s in sect:
                republics = s.find_all('b')
                section_cities = s.find_all('ul')
                # print(section_cities)
                time.sleep(1)
                for republic in republics:

                    r = republic.getText()
                    # print(f'{i}){r}:')
                    file.write(f'{i}){r}:\n')
                    i+=1
                    for cities in section_cities:
                        city = cities.find_all('a')
                        time.sleep(1)
                        for ci in city:
                            c = ci.getText()
                            time.sleep(2)
                            city_url = ci.get('href')
                            file.write(f'\t {c}:  \n')

                            browser = mechanicalsoup.StatefulBrowser()
                            browser.open(f'{url_without_specs}{city_url}')
                            page = browser.page
                            # print(f'\t{c}:')
                            colleges_names = page.find_all('p', 'unit-name')

                            for href_college_unit in colleges_names:
                                    content_college = href_college_unit.find('a')

                                    href_college = content_college.get('href')
                                    time.sleep(2)
                                    open_college_page = mechanicalsoup.StatefulBrowser()
                                    open_college_page.open(f'{url_without_specs}{href_college}')
                                    college_page = open_college_page.page
                                    college_name_content = college_page.find_all('div', 'card-content')


                                    for college_name_tag in college_name_content:
                                        time.sleep(0.5)
                                        if college_name_tag.find('h1') is not None:
                                            college_name = college_name_tag.find('h1').getText()
                                            # print(f'\t\t{college_name}:')
                                            file.write(f'\t\t{college_name}:\n')
                                            college_spec_tag = college_page.find('section',id = 'lic_okso')

                                            if college_spec_tag is not None:
                                                # print(college_spec_tag.find_all('tr'))
                                                for test in college_spec_tag.find_all('tr'):

                                                    string_id_spec_kval = test.find_all('td')
                                                    # print(string_id_spec_kval)
                                                    j=0
                                                    for string_id in string_id_spec_kval:
                                                        if j !=2:
                                                            if j==0:
                                                                spec_id = string_id.getText()
                                                                # print(f'\t\t\t{spec_id} ',end='')
                                                                file.write(f'\t\t\t{spec_id} ')
                                                            elif j==1:
                                                                spec_name = string_id.getText()
                                                                # print(f'{spec_name} ', end='')
                                                                file.write(f'{spec_name} ')
                                                        else:
                                                            # print()
                                                            file.write(f'\n')
                                                        j+=1
                                    time.sleep(1)
                                    open_college_page.close()
                            time.sleep(1)
                            browser.close()

def write_republics(page):
    with open('database/republics.txt', 'w',encoding='utf-8') as file:
        tags = page.find_all('p')
        for text in tags:
            file.write(f'{text.getText()}\n')


def main():
    write_republics(connection_page_cities())
    # find_cities(connection_page_cities())
    #write_data_in_file(connection_page_specs())


if __name__ == '__main__':
    main()

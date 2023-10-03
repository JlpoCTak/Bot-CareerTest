import functools

from config import url
import mechanicalsoup


def connection_web():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url)
    page = browser.page
    return page
def write_data_in_file(page):
    specs = page.find_all('ul', id = 'specs')
    for spec in specs:
        s = spec.find_all('li')
        j=0
        print(s[0].getText())
        with open('specs.txt', 'w', encoding='utf-8') as file:
            for i in range(620):
                kod = (s[i].find_all('span'))
                name = (s[i].find_all('a'))

                if s[i].find_all('span')==[]:
                    print(f'{j+1}) {s[i].getText()} \n ')
                    file.write(f'{j+1}) {s[i].getText()} \n')
                    j+=1
                else:

                    for text_name in name:

                        for text_kod in kod:
                            file.write(f'--  {text_kod.getText()} - {text_name.getText()} \n')
                            print(text_kod.getText(), ' - ', text_name.getText())












def main():
    write_data_in_file(connection_web())


if __name__ == '__main__':
    main()

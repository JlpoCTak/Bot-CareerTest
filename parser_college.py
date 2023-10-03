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


        if s[0].find_all('span')==[]:
            qwe = (s[1].find_all('span'))
            for data in qwe:
                print(data.getText())
        else:
            continue
        if s[0].find_all('a')==[]:
            qwe = (s[1].find_all('a'))
            for data in qwe:
                print(data.getText())









def main():
    write_data_in_file(connection_web())


if __name__ == '__main__':
    main()

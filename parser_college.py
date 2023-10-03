'''import requests
from bs4 import BeautifulSoup

cookies = {
    'noBotAd': '1',
    'key': 'ObxfJe',
    'SLG_G_WPT_TO': 'ru',
    '_ym_uid': '1696272150443623732',
    '_ym_d': '1696272150',
    'SLG_GWPT_Show_Hide_tmp': '1',
    'SLG_wptGlobTipTmp': '1',
    '_ym_isad': '2',
    '_gid': 'GA1.2.1296749194.1696272151',
    '_pk_id.1.c66d': '839c16ab2c0b6669.1696272151.',
    '_pk_ref.1.c66d': '%5B%22%22%2C%22%22%2C1696272151%2C%22https%3A%2F%2Fyandex.ru%2F%22%5D',
    '_pk_ses.1.c66d': '1',
    'noBotAd': '1',
    '_gcl_au': '1.1.10696264.1696273702',
    '_ga_DJZTCV9WK0': 'GS1.1.1696273701.1.0.1696273701.60.0.0',
    '_ga': 'GA1.2.1007270355.1696272151',
    '_ga_M81DKEKX93': 'GS1.2.1696272151.1.1.1696277691.60.0.0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'noBotAd=1; key=ObxfJe; SLG_G_WPT_TO=ru; _ym_uid=1696272150443623732; _ym_d=1696272150; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1; _ym_isad=2; _gid=GA1.2.1296749194.1696272151; _pk_id.1.c66d=839c16ab2c0b6669.1696272151.; _pk_ref.1.c66d=%5B%22%22%2C%22%22%2C1696272151%2C%22https%3A%2F%2Fyandex.ru%2F%22%5D; _pk_ses.1.c66d=1; noBotAd=1; _gcl_au=1.1.10696264.1696273702; _ga_DJZTCV9WK0=GS1.1.1696273701.1.0.1696273701.60.0.0; _ga=GA1.2.1007270355.1696272151; _ga_M81DKEKX93=GS1.2.1696272151.1.1.1696277691.60.0.0',
    'Referer': 'https://yandex.ru/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition Yx GX)',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Opera GX";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}




url = 'https://college.edunetwork.ru/specs '
def connect_to_web():
    response = requests.get(
        url=url,
        cookies=cookies,
        headers=headers,
    )
    bs = BeautifulSoup(response.text, 'lxml')
    temp = bs.find('div','row')
    print(bs)




def main():
    connect_to_web()


if __name__ == '__main__':
    main()'''


from selenium import webdriver

DRIVER_PATH = 'C:/Users/Игорь/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')


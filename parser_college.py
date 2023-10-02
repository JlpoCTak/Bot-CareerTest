import requests
from bs4 import BeautifulSoup


headers = {
    'authority': 'www.wildberries.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',

    'referer': 'https://www.wildberries.ru/catalog/obuv/muzhskaya/kedy-i-krossovki',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Opera GX";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition Yx GX)',
    'x-requested-with': 'XMLHttpRequest',
    'x-spa-version': '9.3.133',
}

params = {
    'targetUrl': 'https://college.edunetwork.ru/specs',
}


url = 'https://college.edunetwork.ru/specs '
def connect_to_web():
    response = requests.get(
        url=url,
        params=params,
        headers=headers,
    )
    bs = BeautifulSoup(response.content, 'lxml')
    temp = bs.find('div', 'catalog-page__content')
    print(bs)




def main():
    connect_to_web()


if __name__ == '__main__':
    main()
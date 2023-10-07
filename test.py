import mechanicalsoup



open_college_page = mechanicalsoup.StatefulBrowser()
open_college_page.open(f'https://college.edunetwork.ru/34/8/')
college_page = open_college_page.page
college_name_content = college_page.find_all('div', 'card-content')
# open_college_page.close()
print(open_college_page.session)



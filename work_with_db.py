import json
import time

import ijson

dict_rep = [
    "Адыгея Республика",
    "Алтай Республика"
]

def find_college():
    with open('database/db.json','r',encoding='utf-8') as file:
        cities = ijson.items(file,dict_rep[0])
        print(list(cities))

def main():
    find_college()

if __name__=='__main__':
    main()
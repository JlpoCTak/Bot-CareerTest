import json
import time

import ijson

dict_rep = [
    "Адыгея Республика",
    "Алтай Республика"
]

def find_college():
    with open('database/db.json','r',encoding='utf-8') as file:
        with open('database/test.txt','w',encoding='utf-8') as text_w:
            for db in file:
                # db_db1 = file.load(file)
                # time.sleep(0.01)
                text_w.write(db)
                print(db)
                break
def main():
    find_college()

if __name__=='__main__':
    main()
import json
import time

import ijson



def find_college():
    with open('database/republics.txt', 'r', encoding='utf-8') as rep:
        with open('database/db.json', 'r', encoding='utf-8') as file:
            # for i in range(83):
                # republi = rep.readline().strip()  # считываем файл с областями

                # print(republic)
                republic = ijson.parse(file)
                for prefix,event,value in republic:
                    # if event=='map_key' and prefix=='':
                    #     repub = value #название областей
                    # print(prefix,event,value)
                    # if event=='map_key' and value!='':
                    #     print(prefix,event,value)
                    print(prefix)

def main():
    find_college()

if __name__=='__main__':
    main()
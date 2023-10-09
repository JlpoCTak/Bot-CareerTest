import json

def find_college():
    with open('database/db_20k.json','r',encoding='utf-8') as file:
        data_base = json.load(file)
        print(data_base)
def main():
    find_college()

if __name__=='__main__':
    main()
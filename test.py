import sqlite3
import json

with open('database/specs_for_test_holland.json', encoding='utf-8') as groups:
    with sqlite3.connect('database/users.db') as connection:
        cursor = connection.cursor()
        group = json.load(groups)
        dict_code = []
        dict_name = []
        print(group.values())
        for specs in group.values():
            for spec in specs:
                dict_name.append(specs[spec])
                dict_code.append(spec)

        print(dict_code)
        print(dict_name)
        print(len(dict_name))
        for i in range(len(dict_name)):
            cursor.execute('''INSERT INTO specs (code,name) VALUES (?,?)''', (dict_code[i], dict_name[i]))

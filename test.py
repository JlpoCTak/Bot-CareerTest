import asyncio
import sqlite3

def create():
    with sqlite3.connect('database/users.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users_answer (
                        id INTEGER PRIMARY KEY,
                        tg_user_id INTEGER
                        )''')

def add_column():
    with sqlite3.connect('database/users.db') as connection:
        cursor = connection.cursor()
        for i in range(1, 43):
            cursor.execute(f'''ALTER TABLE users_answer ADD answ_{i} TEXT''')

def main():
    create()
    add_column()

if __name__=='__main__':
    main()
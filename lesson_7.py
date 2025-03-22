"БД - Базы Данных"
"СУБД - Система Управления Базами Данных"

import sqlite3

connect = sqlite3.connect("Animation.db") # Подключение к базе данных
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS animators(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               full_name VARCHAR (25) NOT NULL,
               hobby TEXT DEFAULT NULL,
               phone_number INT NOT NULL DEFAULT 996,
               birth_day DATE,
               cuts DOUBLE (5, 2) DEFAULT 0.0,
               is_married BOOLEAN DEFAULT False)""")

def add_student():
    user_full_name = input("Введите имя: ")
    user_hobby = input("Введите ваше хобби: ")
    user_phone_number = int(input("Введите номер телефона: "))
    user_birthday = input("Введите дату рождения: ")

    cursor.execute(f"""INSERT INTO animators
                   (full_name, hobby, phone_number, birth_day)
                   VALUES ('{user_full_name}', '{user_hobby}', {user_phone_number}, '{user_birthday}')""")

    # cursor.execute(
    #     f"""INSERT INTO animators
    #                (full_name, hobby, phone_number, birth_day)
    #                VALUES ('?', '?', ?, '?'), user_full_name, user_hobby, user_phone_number, user_birthday"""
    # )

    connect.commit()

add_student()

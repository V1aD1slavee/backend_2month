"БД - Базы Данных"
"СУБД - Система Управления Базами Данных"

"CRUD - Create, Read, Update, Delete"

import sqlite3

connect = sqlite3.connect("Animation.db") # Подключение к базе данных
cursor = connect.cursor()  # Посредник для работы с базой данных

cursor.execute("""
CREATE TABLE IF NOT EXISTS animators(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               full_name VARCHAR (25) NOT NULL,
               hobby TEXT DEFAULT NULL,
               phone_number INT NOT NULL DEFAULT 996,
               birth_day DATE,
               cuts DOUBLE (5, 2) DEFAULT 0.0,
               is_married BOOLEAN DEFAULT False)""")

def add_animator():
    user_full_name = input("Введите имя: ")
    user_hobby = input("Введите ваше хобби: ")
    user_phone_number = int(input("Введите номер телефона: "))
    user_birthday = input("Введите дату рождения: ")

    cursor.execute(
        f"SELECT phone_number FROM animators WHERE phone_number == {user_phone_number}"
    )
    animator = cursor.fetchone()

    if animator:
        print(f"Пользователь с номером +{user_phone_number} уже существует!")
    else:
        cursor.execute(f"""INSERT INTO animators
                    (full_name, hobby, phone_number, birth_day)
                    VALUES ('{user_full_name}', '{user_hobby}', {user_phone_number}, '{user_birthday}')""")

    # cursor.execute(
    #     f"""INSERT INTO animators
    #                (full_name, hobby, phone_number, birth_day)
    #                VALUES ('?', '?', ?, '?'), 
    #                user_full_name, user_hobby, user_phone_number, user_birthday"""
    # )
    # Этот способ более безопасный для отправки запросов в БД
    
    connect.commit()  # Используется что бы зафиксировать изменения 


def all_animation():
    cursor.execute("SELECT * FROM animators")
    anim = cursor.fetchall()
    print(anim)


def delete_animator():
    user_id = int(input("Введите id пользователя: "))
    cursor.execute(f"SELECT id, full_name FROM animators WHERE id == {user_id}")
    del_anim = cursor.fetchone()

    if del_anim:
        cursor.execute(f"DELETE FROM animators WHERE id == {user_id}")
        connect.commit()
        print(f"Пользователь {del_anim} удалён!")
    else:
        print("Такого пользователя нет в базе данных")


def update_animator():
    user_id = int(input("Введите id пользователя: "))
    user_full_name = input("Введите новое имя: ")
    user_hobby = input("Введите новое хобби: ")
    user_phone_number = int(input("Введите новый номер телефона: "))
    user_birthday = input("Введите новую дату рождения: ")
    user_cut = float(input("Сколько штрафов?: "))
    user_is_married = bool(input("Пользователь в браке? 1 - да 0 - нет: "))

    cursor.execute(f"SELECT id, full_name FROM animators WHERE id == {user_id}")
    anim = cursor.fetchone()

    if anim:
        cursor.execute(
            """UPDATE animators SET 
            full_name = ? , hobby = ?, phone_number = ?,
            birth_day = ?, cuts = ?, is_married = ? WHERE id = ?""",(
            user_full_name,
            user_hobby,
            user_phone_number,
            user_birthday,
            user_cut,
            user_is_married,
            user_id)
        )

        connect.commit()
        print(f"Пользователь {anim} обновлён!")
    else:
        print(f"Пользователь с таким id не существует")

def update_animators_cut():
    user_id = int(input("Введите id пользователя: "))
    user_cut = float(input("Введите количевство штрафов пользователя: "))
    cursor.execute(f"SELECT id, full_name FROM animators WHERE id == {user_id}")
    anim = cursor.fetchone()

    if anim:
        cursor.execute("""UPDATE animators SET cuts = ? WHERE id = ?""", (user_cut, user_id))
        connect.commit()
        print(f"Кол-во штрафов пользователя {anim} успешно изменено")
    else:
        print("Такого пльзователя не существует")

# add_animator()
# all_animation()
# delete_animator()
# update_animator()
# update_animators_cut()

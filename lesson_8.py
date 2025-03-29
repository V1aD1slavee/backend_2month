import sqlite3

connect = sqlite3.connect("Animation.db")
cursor = connect.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS animators(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               full_name VARCHAR (25) NOT NULL,
               hobby TEXT DEFAULT NULL,
               phone_number INT NOT NULL DEFAULT 996,
               birth_day DATE,
               cuts DOUBLE (5, 2) DEFAULT 0.0,
               is_married BOOLEAN DEFAULT False)"""
)

class Egypt:
    def __init__(self):
        self.full_name = None
        self.hobby = None
        self.phone_number = 0
        self.birth_day = None
        self.cuts = 0.0
        self.is_married = False

    def register(self):
        user_full_name = input("Введите имя: ")
        user_hobby = input("Введите ваше хобби: ")
        user_phone_number = int(input("Введите номер телефона: "))
        user_birthday = input("Введите дату рождения: ")

        cursor.execute(f"SELECT phone_number FROM animators WHERE phone_number == {user_phone_number}")
        animator = cursor.fetchone()

        if animator:
            print(f"Пользователь с номером +{user_phone_number} уже существует!")
        else:
            cursor.execute(f"""INSERT INTO animators
                            (full_name, hobby, phone_number, birth_day)
                            VALUES ('{user_full_name}', '{user_hobby}', {user_phone_number}, '{user_birthday}')""")

        connect.commit()
        print("Пользователь успешно добавлен!")

    def all_animation(self):
        cursor.execute("SELECT * FROM animators")
        animator = cursor.fetchall()
        print(animator)

    def update_animation_married(self):
        user_id = int(input("Введите id пользователя: "))
        user_is_married = bool(input("Пользователь в браке? 1 - да 0 - нет: "))

        cursor.execute(f"SELECT id, full_name FROM animators WHERE id == {user_id}")
        anim = cursor.fetchone()

        if anim:
            cursor.execute("UPDATE animators SET is_married = ? WHERE id = ?", (user_is_married, user_id))
            connect.commit()
            print("Статус пользователя обновлён")
        else:
            print("Такого пользователя не существует!")


    def delete_animator(self):
        user_id = int(input("Введите id пользователя: "))
        cursor.execute(f"SELECT id, full_name FROM animators WHERE id == {user_id}")
        del_anim = cursor.fetchone()

        if del_anim:
            cursor.execute(f"DELETE FROM animators WHERE id == {user_id}")
            connect.commit()
            print(f"Пользователь {del_anim} удалён!")
        else:
            print("Такого пользователя нет в базе данных")

    def update_animator(self):
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

    def update_animators_cut(self):
        user_id = int(input("Введите id пользователя: "))
        user_cut = float(input("Введите количевство штрафов пользователя: "))
        cursor.execute(f"SELECT id, full_name FROM animators WHERE id == {user_id}")
        anim = cursor.fetchone()

        if anim:
            cursor.execute("""UPDATE animators SET cuts = ? + ? WHERE id = ?""",
                           (user_cut, user_cut, user_id))
            connect.commit()
            print(f"Кол-во штрафов пользователя {anim} успешно изменено")
        else:
            print("Такого пльзователя не существует")

    def main(self):
        while True:
            print("\nВыберите действие")
            print("0-выход, 1-регистрация, 2-просмотр пользователей, 3-обновление данных аниматора \n4-обновление штрафов, 5-обновленни семейного положения ,6-удаление пользователя")
            command = int(input(": "))

            if command == 0:
                break
            elif command == 1:
                self.register()
            elif command == 2:
                self.all_animation()
            elif command == 3:
                self.update_animator()
            elif command == 4:
                self.update_animators_cut()
            elif command == 5:
                self.update_animation_married()
            elif command == 6:
                self.delete_animator()
            else:
                print("Ответ введён не верно, пожалуйста повторите попытку!")

animator = Egypt()
animator.main()

import sqlite3

connect = sqlite3.connect("Animation.db")  # Подключение к базе данных
cursor = connect.cursor()  # Посредник для работы с базой данных

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

        cursor.execute(
            f"SELECT phone_number FROM animators WHERE phone_number == {user_phone_number}"
        )
        animator = cursor.fetchone()

        if animator:
            print(f"Пользователь с номером +{user_phone_number} уже существует!")
        else:
            cursor.execute(
                f"""INSERT INTO animators
                        (full_name, hobby, phone_number, birth_day)
                        VALUES ('{user_full_name}', '{user_hobby}', {user_phone_number}, '{user_birthday}')"""
            )

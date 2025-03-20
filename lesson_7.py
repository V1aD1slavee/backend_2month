"БД - Базы Данных"
"СУБД - Система Управления Базами Данных"

import sqlite3

connect = sqlite3.connect("Animation.db") # Подключение к базе данных
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE animators(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               full_name VARCHAR (25),
               hobby TEXT,
               phone_number INT,
               birth_day DATE,
)""")
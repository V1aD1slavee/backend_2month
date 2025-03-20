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


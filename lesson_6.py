# from test import add, sub, mult
# from package.test import sub

# add(2,4)
# sub(8,4)
# mult(2,8)

# from test import add as plus  # Перезаписть функции из сторонего модуля
# from test import * # Импортирование всего содержимого модуля

# add(3,30)
# sub(8, 4)
# mult(2,8)

# import package.test as test
# from package import test

# test.sub(2,3)


"""Декомпозиция -- разделение кода по модулям"""

"Кастомные модули: это модули которые мы сделали сами - module , lesson_1, start"
"Встроенные модули: random, math, time, datetime, os, sys"

"random"
# import random

# massiv = ["@1", 12, 14211, "Hello"]
# rand_choice = random.choice(massiv)
# random.shuffle(massiv)


# lucky_num = random.randint(1,10)
# print(lucky_num)
# print(rand_choice)
# print(massiv)


"time"
# # import time
# from time import sleep  # так не советуется

# print("Loading")
# # time.sleep(1)
# print(".")
# sleep(1)  # так не советуется
# print("Done!")

"Внешние модули: colorama, termcolor"
from termcolor import cprint

print("Hello world")
cprint("Hello world", color="blue", on_color="on_light_yellow")

"Win"
"./venv/Scripts/activate" 
"deactivate"

"MacOS, Linux"
"source venv/bin/activate"
"deactivate"

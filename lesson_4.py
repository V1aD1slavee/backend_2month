"Декораторы"

"Создание своего декоратора"
# def decor(a):
#     def start():
#         print("Hello")
#         a()
#         print("Bye")
#     return start()


# @decor
# def add():
#     print(2 + 2)

# add()


# @decor
# def text():
#     print("лялялялл вяы фа тыв фцовшр ф")

# text()


"Множественное наследование"

# class Transport: # Абстрактныйй класс
#     def __init__(self, marka, model, color):
#         self.marka = marka
#         self.model = model
#         self.color = color

#     # def info(self):
#     #     print(f" Марка машины - {self.marka}\n Модель - {self.model}\n Цвет - {self.color}")

#     def __str__(self):
#         return f"Марка машины - {self.marka}\nМодель - {self.model}\nЦвет - {self.color}"


# class FuelCar(Transport):
#     def __init__(self, marka, model, color, fuel_tank):
#         Transport.__init__(self, marka, model, color)
#         self.fuel_tank = fuel_tank

#     def __str__(self):
#         return super().__str__() + f"\nбак {self.fuel_tank}"

#     def drive(self):
#         print(f"Машина: {self.marka}-{self.model} едет на бензине")


# ae_86 = FuelCar("Toyota", "ae-86", "white", 83)
# # ae_86.info()
# print(ae_86)

# class ElectroCar(Transport):
#     def __init__(self, marka, model, color, battery):
#         Transport.__init__(self, marka, model, color)
#         self.battery = battery

#     def drive(self):
#         print(f"Машина: {self.marka}-{self.model} едет на электричестве")

# tesla = ElectroCar("Tesla", "module 3", "black", 100000)
# # tesla.drive()


# class GybydCar(ElectroCar, FuelCar):

#     def __init__(self, marka, model, color, battery, fuel_tank, speed):
#         ElectroCar.__init__(self, marka, model, color, battery)
#         FuelCar.__init__(self, marka, model, color, fuel_tank)
#         self.speed = speed

#     def drive(self):
#         if self.speed <= 60:
#             return ElectroCar.drive(self)
#         else:
#             return FuelCar.drive(self)

# toyota = GybydCar("Toyota", "Prius", "White", 50000, 70, 80)
# toyota.drive()
# print(toyota.fuel_tank)


"Магические методы"

"dunder методы - (double underscore)"

class Math:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def info(self):
        print(f"Первое число - {self.number_1}\nВторое число - {self.number_2}")

    def __str__(self): # print
        return f"Первое число - {self.number_1}\nВторое число - {self.number_2} это str"

    def __repr__(self): # print
        return (f"Первое число - {self.number_1}\nВторое число - {self.number_2} это repr")

    "Метод __call__ автоматически вызывается, когда к объекту обращаются как к функции. "
    def __call__(self, a, b):
        print("Hello world")

    "Магические методы для арифметических действий"
    def __add__(self, other): # "+"
        return Math(self.number_1 + other.number_1, self.number_2)

    def __sub__(self, other):  # "-"
        return Math(self.number_1 + other.number_1, self.number_2)

    def __mul__(self, other):  # "*"
        return Math(self.number_1 + other.number_1, self.number_2)

    def __truediv__(self, other):  # "/"
        return Math(self.number_1 + other.number_1, self.number_2)

    def __floordiv__(self, other):  # "//"
        return Math(self.number_1 + other.number_1, self.number_2)
    
    "Магические методы для оператора сравнения"
    def __gt__(self, other):
        return self.number_1 > other.number_1


math = Math(12,14)
math_2 = Math(13, 113)

# math.info()
# print(math) # str and repr
# math(12,5)    # call

"Магические методы для арифметических действий"
print(math + math_2)
print(math - math_2)
print(math * math_2)
print(math / math_2)
print(math // math_2)

"Магические методы для оператора сравнения"
print(math > math_2)
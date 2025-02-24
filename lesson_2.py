"Насиледование и абстракция"
"DRY - Don't Repeat Yourself == не повторяй себя"
# Родительский класс и дочерний

class Transport: # Абстрактныйй класс
    def __init__(self, marka, model, color):
        self.marka = marka
        self.model = model
        self.color = color


    def info(self):
        print(f" Марка машины - {self.marka}\n Модель - {self.model}\n Цвет - {self.color}")


class Car(Transport): # Родительский класс
    pass 

# auto1 = Car("Mersedes", "212", "Grey")
# auto1.info()

class McLaren(Car): # Дочерний класс
    def __init__(self, marka, model, color, is_spoiler):
        super().__init__(marka, model, color) # Два способа наследования конструктора
        # Car.__init__(self, marka, model, color)
        self.is_spoiler = is_spoiler

    def info(self):
        print(f" Марка машины - {self.marka}\n Модель - {self.model}\n Цвет - {self.color}\n Спойлер - {self.is_spoiler}")

# auto2 = McLaren("McLaren", "650S", "Orange", True)
# auto2.info()

class Animal:
    
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        print("MEOW - MEOW")


class Dog(Animal):
    def make_sound(self):
        print("GAW - GAW")


class Cow(Animal):
    def make_sound(self):
        print("MOO - MOO")


cat = Cat()
dog = Dog()
cow = Cow()

cat.make_sound()
dog.make_sound()
cow.make_sound()

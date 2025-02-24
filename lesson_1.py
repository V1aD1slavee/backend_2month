"Объектно-ориентированное программирование"

"Змеиный регистр"
# snake_case = "string"

"Вербюжий регистр"
# CamelCase = "string"

class Car: # шаблон или же чертёж
    "Атрибут класса"
    # marka = "McLaren"
    # model = "675LT"
    # color = "Orange"

    "__init__ - конструктор "
    "self - ссылка на обьект(сам обьект)"
    def __init__(self,marka,model,color):
        "Атрибут обьекта"
        self.marka = marka
        self.model = model
        self.color = color
        self.is_start = False
        self.bak = 0

    def info(self):
        print(f" Марка машины - {self.marka}\n Модель - {self.model}\n Цвет - {self.color}")

    def start(self):
        but = input("Напишите start что бы завести машину: ")
        if self.bak > 0:
            if but == "start":
                print(f"Машина - {self.marka} - {self.model} заведена")
                self.is_start = True
            else:
                print(f"Машина - {self.marka} - {self.model} заглохла")
        else:
            print(f"В машине {self.marka} - {self.model} нет топлива")

    def drive(self):
        if self.is_start == True:
            print(f"Машина - {self.marka} - {self.model} поехал")
        else:
            print(f"Машина - {self.marka} - {self.model} не заведена")
            way = False

    def stop(self):
        print(f"Машина - {self.marka} - {self.model} заглушена")
        self.is_start == False


auto1 = Car("McLaren","650S", "Orange")
auto2 = Car("BMW", "M5", "Grey")
auto3 = Car("Honda", "Fit", "Wite")

# print(auto.marka)
# print(auto.model)
# print(auto.color)
auto1.info()
auto2.start()
auto2.drive()
auto2.stop()

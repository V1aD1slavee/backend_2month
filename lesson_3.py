"Инкапсуляция"

class Person:
    def __init__(self, name, age, height):
        self.name = name # Публичный
        self._age = age # Защищенный
        self.__height = height # Приватный

    "@ - декоратор"
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,new_height):
        self.height = new_height

    def info(self):
        print(f"Имя - {self.name} Возраст - {self._age} Рост - {self.__height}")

    def _security(self):
        print("Защищеная информация")

    def __private_method(self):
        print("Приватная информация")
        
    def anprivate(self):
        self.__private_method()
        

human = Person("Vlad", 18, 187)
# human.info()

# print(human.name)
# print(human._age)
# print(human.height)

human._security()
human.anprivate()
human.__private_method()

class Animal:
    def __init__(self, weight, width, length, age):
        """Ініціалізує об'єкт класу Animal."""
        self.weight = weight
        self.width = width
        self.length = length
        self.age = age

    def display_info(self):
        """Виводить інформацію про тварину."""
        print(f"Вага: {self.weight} кг")
        print(f"Ширина: {self.width} см")
        print(f"Довжина: {self.length} см")
        print(f"Вік: {self.age} років")


'animal import Animal'

my_animal = Animal(weight=50, width=20, length=50, age=3)
my_animal.display_info()

another_animal = Animal(weight=10, width=5, length=10, age=1)
another_animal.display_info()
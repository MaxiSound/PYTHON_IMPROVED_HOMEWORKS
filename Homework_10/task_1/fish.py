from animal import Animal


class Fish(Animal):
    def __init__(self, fins, name, age):
        super().__init__(name, age)
        self.fins = fins

    def get_fins(self):
        return f'Уникальное свойство для рыб наличие плавников - {self.fins}'

    def __str__(self):
        return f'name = {self.name}, age = {self.age}, wings = {self.fins}'

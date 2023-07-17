from animal import Animal


class Birds(Animal):
    def __init__(self, wings, name, age):
        super().__init__(name, age)
        self.wings = wings

    def get_wings(self):
        return f'Уникальное свойство для птиц наличие крыльев - {self.wings}'

    def __str__(self):
        return f'name = {self.name}, age = {self.age}, wings = {self.wings}'

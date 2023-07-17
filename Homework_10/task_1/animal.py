class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return f'Имя животного - {self.name}'

    def get_age(self):
        return f'Возраст животного = {self.age}'

    def __str__(self):
        return f'name = {self.name}, age = {self.age}'

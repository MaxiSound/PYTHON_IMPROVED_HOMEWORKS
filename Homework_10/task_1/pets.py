from animal import Animal


class Pets(Animal):
    def __init__(self, nickname, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nickname = nickname

    def get_nickname(self):
        return f'Уникальное свойство для домашнего животного кличка - {self.nickname}'

    def __str__(self):
        return f'name = {self.name}, age = {self.age}, wings = {self.nickname}'

from lesson import Lesson
from descriptor import Descriptor_name


class Student:
    """
    Класс студента хранящий в себе его имя, фамилию, отчество
    и список его предметов
    """
    first_name = Descriptor_name()
    last_name = Descriptor_name()
    patronymic = Descriptor_name()

    def __init__(self, first_name, last_name, patronymic):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.list_lesson = []

    def append_lesson(self, lesson: Lesson):
        self.list_lesson.append(lesson)

    def print_list_lesson(self):
        for lesson in self.list_lesson:
            print(lesson)

    def __str__(self):
        print(f'{self.first_name = },{self.last_name = },{self.patronymic = }\n{self.list_lesson = }')

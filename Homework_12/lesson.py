import csv


class Lesson:
    """
    Класс предмета хранящий в себе его название,
    оценки и баллы за тесты полученные учеником
    с выводом средних значений.
    """

    def __init__(self, name_lesson):
        self.name_lesson = name_lesson
        self.list_estimation = []
        self.list_estimation_ball = []

    def lesson_and_estimation(self):
        with open('lesson.csv', 'r', encoding='utf-8') as file:
            read_csv = csv.reader(file)
            for lst_lesson in read_csv:
                for lesson in lst_lesson:
                    if lesson == self.name_lesson:
                        print(lst_lesson)

    def append_estimation(self, estimation):
        if 5 >= estimation >= 2:
            self.list_estimation.append(estimation)
        else:
            print('Оценка может быть только от 2 до 5')

    def append_estimation_ball(self, estimation_ball):
        if 0 <= estimation_ball <= 100:
            self.list_estimation_ball.append(estimation_ball)
        else:
            print('Балл может быть только от 0 до 100')

    def average_estimation(self):
        result = sum(self.list_estimation) / len(self.list_estimation)
        return result

    def average_ball(self):
        result = sum(self.list_estimation_ball) / len(self.list_estimation_ball)
        return result

    def __str__(self):
        return f'{self.name_lesson}\n\
                Средняя оценка по данному предмету - {self.average_estimation()}\n\
                Средний балл по данному предмету - {self.average_ball()}'

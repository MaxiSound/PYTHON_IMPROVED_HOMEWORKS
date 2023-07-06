# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json


def convert_to_json(file_name):
    dic = {}
    with (open(file_name, "r", encoding="UTF-8") as f1, open('task_1.json', "w", encoding="UTF-8") as f2):
        dic = {}
        for i in f1:
            k, v = (i.rstrip()).split(':')
            dic[k.capitalize()] = v
            json.dump(dic, f2, ensure_ascii=False)


convert_to_json('Homework_7_task_3_result.txt')

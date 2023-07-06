# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json
import os.path


def my_func(json_file):
    if os.path.isfile(json_file):
        with open(json_file, 'r', encoding='UTF-8') as f:
            dic = json.load(f)
    else:
        dic = {str(i): {} for i in range(1, 8)}
    while True:
        data = input(
            "Введите имя, личный идентификатор и уровень доступа (от 1 до 7) через пробел ")
        if data == '':
            break
        name, id, level = data.split()
        # flag = False
        # while True:
        #     for i in dic.keys():
        #         if id in dic[i]:
        #             flag = True
        #     if flag == True:
        #         id = input("Введите другой личный идентификатор. Такой идентификатор уже есть в базе. ")
        #         flag = False
        #     else:
        #         break
        if id in dic[level] and dic[level][id] == name:
            dic.setdefault(level, {id: name})[id] = name
        else:
            dic[level][id] = name
        with open(json_file, 'w', encoding='UTF-8') as f2:
            json.dump(dic, f2, ensure_ascii=False, indent=1)


my_func('task_2.json')

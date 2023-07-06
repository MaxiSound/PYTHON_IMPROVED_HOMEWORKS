# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import csv
import json


def json_to_csv(source_file, result_file):
    with (open(source_file, 'r', encoding='UTF-8') as f1,
          open(result_file, 'w', encoding='UTF-8') as f2):
        dic = json.load(f1)
        rows = []
        for level, in_dict in dic.items():
            for id, name in in_dict.items():
                rows.append({'id': id, 'level': int(level), 'name': name})
        print(rows)
        csv_write = csv.DictWriter(f2, fieldnames=['id', 'level', 'name'])
        # запись заголовка
        csv_write.writeheader()
        # матрица
        csv_write.writerows(rows)


json_to_csv('task_2.json', 'task_3.csv')

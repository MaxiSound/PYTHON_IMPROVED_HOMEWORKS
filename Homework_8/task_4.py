# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

import json

def csv_to_json(source_file, result_file):
    with (open(source_file, 'r', encoding='UTF-8') as f1,
          open(result_file, 'w', encoding='UTF-8') as f2):
        file = []
        for i in f1:
            if i != "\n":
                file.append(i.rstrip().split(','))
        print(file)
        header_id, header_name, header_access = file[0]
        lst = []
        for i, name, access in file[1:]:
            lst.append({header_id: i+'0000000', header_name: name,
                       header_access: access, 'hash': hash(i+name)})
        json.dump(lst, f2, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    csv_to_json('task_3.csv', 'task_4.json')

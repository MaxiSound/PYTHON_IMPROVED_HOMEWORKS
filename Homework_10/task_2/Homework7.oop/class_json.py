import os
import json


class ClassJson:
    # запись
    def write_json_file(self, name_json_file, data):
        with open('json_csv_pickle_files/' + name_json_file + '.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, separators=(',', ':'))

# вывод содержимого в терминал
    def print_json_file(self, name_json_file):
        with open('json_csv_pickle_files/' + name_json_file + '.json', 'r', encoding='utf-8') as json_file:
            print(json.load(json_file))

# дозапись
    def append_in_json_file(self, name_json_file, data):
        with open('json_csv_pickle_files/' + name_json_file + '.json', 'a', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, separators=(',', ':'))

# удаление
    def delete_json_file(self, path_file):
        os.remove(os.walk(path_file))

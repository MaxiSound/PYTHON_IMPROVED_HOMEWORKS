import os
import csv


from class_pickle import ClassPickle
from class_csv import ClassCsv
from class_json import ClassJson

# создание класса работы сдерикторией
class WorkingIsDirectory(ClassCsv, ClassJson, ClassPickle):
# создание конструктора класса с принимающим на вход путь к дериктории
    def __init__(self, path_directory: str):
        self.path_directory = path_directory
# создание метода для записи информации директории в словарь
    def file_and_folder_in_directory(self):
        dict_file_and_folder_in_directory = {}
        for dir_path, dir_file, file_name in os.walk(self.path_directory):
            dict_file_and_folder_in_directory[f'DIRECTORY - {dir_path}'] = [
                f'FILE - {i} = {os.path.getsize(os.path.abspath(dir_path + "/" + i))} byte' for i in file_name]
        return dict_file_and_folder_in_directory

# удаление директории
    def delete_work_directory(self):
        os.rmdir(os.walk(self.path_directory))

# переопределение метода записи CSV файла, в словарь
    def write_csv_file(self, name_csv_file, data):
        all_data = [["Dir", "Files"]]
        for key, value in data.items():
            all_data.append([key, value])
        with open('json_csv_pickle_files/' + name_csv_file + '.csv', 'w', newline='', encoding='utf-8') as csv_f:
            write_csv = csv.writer(csv_f, dialect='excel-tab', delimiter=',')
            write_csv.writerows(all_data)

# переопределение метода дозаписи CSV файла, в словарь
    def append_in_csv_file(self, name_csv_file, data):
        all_data = []
        for key, value in data.items():
            all_data.append([key, value])
        with open('json_csv_pickle_files/' + name_csv_file + '.csv', 'a', newline='', encoding='utf-8') as csv_f:
            write_csv = csv.writer(csv_f, dialect='excel-tab', delimiter=',')
            write_csv.writerows(all_data)

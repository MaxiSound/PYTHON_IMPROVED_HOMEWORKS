import os
import csv


class ClassCsv:
    # Запись
    def write_csv_file(self, name_csv_file, data):
        with open('json_csv_pickle_files/' + name_csv_file + '.csv', 'w', newline='', encoding='utf-8') as csv_f:
            write_csv = csv.writer(csv_f, dialect='excel-tab', delimiter=',')
            write_csv.writerows(data)

# вывод содержимого в терминал
    def print_csv_file(self, name_csv_file):
        with open('json_csv_pickle_files/' + name_csv_file + '.csv', 'r', newline='', encoding='utf-8') as csv_file:
            csv_f = csv.reader(csv_file)
            for i in csv_f:
                print(i)

# дозапись
    def append_in_csv_file(self, name_csv_file, data):
        with open('json_csv_pickle_files/' + name_csv_file + '.csv', 'a', newline='', encoding='utf-8') as csv_f:
            write_csv = csv.writer(csv_f, dialect='excel-tab', delimiter=',')
            write_csv.writerows(data)

# удаление
    def delete_csv_file(self, path_file):
        os.remove(os.walk(path_file))

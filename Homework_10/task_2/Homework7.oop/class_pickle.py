import os
import pickle


class ClassPickle:
    def __init__(self):
        pass

# сериализация
    def write_pickle_file(self, name_pickle_file, data):
        with open('json_csv_pickle_files/' + name_pickle_file + '.bin', 'wb') as pickle_file:
            pickle.dump(data, pickle_file)

# десиреализация
    def print_pickle_file(self, name_pickle_file):
        with open('json_csv_pickle_files/' + name_pickle_file + '.bin', 'rb') as pickle_file:
            print(pickle.load(pickle_file))

# дозапись
    def append_in_pickle_file(self, name_pickle_file, data):
        with open('json_csv_pickle_files/' + name_pickle_file + '.bin', 'ab') as pickle_file:
            pickle.dump(data, pickle_file)

#удаление файла
    def delete_pickle_file(self, path_file):
        os.remove(os.walk(path_file))

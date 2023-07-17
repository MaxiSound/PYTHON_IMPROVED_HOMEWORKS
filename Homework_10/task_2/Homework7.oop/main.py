# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.


from working_is_directory import WorkingIsDirectory

# создание экземпляра класса по работе с дерикторией
work_in_directory = WorkingIsDirectory('directory')

# вызываем 3 метода для записи информации о директори в соответствующие файлы
work_in_directory.write_json_file('json_file', work_in_directory.file_and_folder_in_directory())
work_in_directory.write_csv_file('csv_file', work_in_directory.file_and_folder_in_directory())
work_in_directory.write_pickle_file('pickle_file', work_in_directory.file_and_folder_in_directory())

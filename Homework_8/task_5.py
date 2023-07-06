# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import json
import os
import pickle


def all_json_to_pickle(dir_):
    json_files = [i for i in os.listdir() if i.endswith(".json")]
    for i in json_files:
        with (open(os.path.join(dir_, i), 'r', encoding='UTF-8') as f1,
              open((os.path.join(dir_, i.rstrip('.json'))+".pickle"), 'wb') as f2):
            pickle.dump(json.load(f1), f2)


if __name__ == "__main__":
    all_json_to_pickle(os.getcwd())

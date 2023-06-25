# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def my_func(**kwargs):
    dic = {}
    for i, k in kwargs.items():
        if isinstance(k, list) or isinstance(k, dict) or isinstance(k, set):
            dic[str(k)] = i
        else:
            dic[k] = i
    print(dic)


my_func(a=[1, 2, 3], b={2}, c={3: 'value'}, d="output")

# Создайте класс Матрица. Добавьте методы для:
# вывода на печать
# сложения
# сравнения


from class_matrix import *

# Создать два экземпляра класса матриц с указанием размеров
first_matrix = Matrix(5, 5)
second_matrix = Matrix(5, 5)

# Задать рандомные значения в матрицы
first_matrix.to_create_matrix()
second_matrix.to_create_matrix()

# Сложение двух матриц
new_matrix = first_matrix.summa_matrix(second_matrix.matrix)

# вывод новой матрицы
print_matrix(new_matrix)

first_matrix.__str__()
second_matrix.__str__()

first_matrix.__repr__()
second_matrix.__repr__()

# вывод суммы элементов матриц
print('Сумма элементов первой матрицы =', first_matrix.summ_element_matrix)
print('Сумма элементов второй матрицы =', second_matrix.summ_element_matrix)

# Вывод сравнения двух матриц
print(first_matrix == second_matrix)
print(first_matrix != second_matrix)
print(first_matrix > second_matrix)
print(first_matrix >= second_matrix)
print(first_matrix < second_matrix)
print(first_matrix <= second_matrix)

# вывод документации в терминал
help(Matrix)

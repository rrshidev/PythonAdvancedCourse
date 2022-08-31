"""
След матрицы

Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу, которая выводит след
заданной квадратной матрицы.

Формат входных данных
На вход программе подаётся натуральное число nnn — количество строк и столбцов в матрице, затем элементы матрицы
(целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — след заданной матрицы.
Тестовые данные 🟢

Sample Input 1:

3
1 2 3
4 5 6
7 8 9

Sample Output 1:

15
"""


def matrix_trace(m_size):
    matrix = []
    for elem in range(m_size):
        nums = [int(num) for num in input().split()]
        matrix.append(nums)
    trace = []
    for row in range(m_size):
        for col in range(m_size):
            if row == col:
                trace.append(matrix[row][col])
    return sum(trace)


matrix_size = int(input())
print(matrix_trace(matrix_size))

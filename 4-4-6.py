"""
Максимальный в области 2 🌶️

Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

Формат входных данных
На вход программе подаётся натуральное число nnn — количество строк и столбцов в матрице, затем элементы матрицы
(целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

Примечание. Элементы диагоналей также учитываются.
Тестовые данные 🟢

Sample Input 1:

3
1 4 5
6 7 8
1 1 6

Sample Output 1:

8

4
-3 1 4 -3
-9 -3 -3 -10
-4 -3 -3 -2
-3 0 0 -3
"""


def maximum_in_area(m_size):
    matrix = []
    result = float('-inf')
    for row_num in range(m_size):
        nums = [int(num) for num in input().split()]
        matrix.append(nums)
    check_nums = []
    for row_num in range(m_size):
        for col_num in range(m_size):
            if (row_num > col_num) and (row_num < m_size - 1 - col_num) or \
                    (row_num < col_num) and (row_num > m_size - 1 - col_num) or \
                    row_num == col_num or m_size == row_num + col_num + 1:
                check_nums.append(matrix[row_num][col_num])
    result = max(check_nums)
    return result


matrix_size = int(input())
print(maximum_in_area(matrix_size))

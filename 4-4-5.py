"""
Максимальный в области 1

Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

Формат входных данных
На вход программе подаётся натуральное число nnn — количество строк и столбцов в матрице, затем элементы матрицы
(целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести одно число — максимальный элемент в заштрихованной области квадратной матрицы.

Примечание. Элементы главной диагонали также учитываются.
Тестовые данные 🟢

Sample Input 1:

3
1 4 5
6 7 8
1 1 6

Sample Output 1:

7
"""


def maximum_in_area(m_size):
    matrix = []
# attention --> KOSTYLE =)
    result = float('-inf')
    for _ in range(m_size):
        nums = [int(num) for num in input().split()]
        matrix.append(nums)
    for i in range(m_size):
        for j in range(m_size):
            if i >= j:
                nums.append(matrix[i][j])
    result = max(nums)
    return result


matrix_size = int(input())
print(maximum_in_area(matrix_size))

"""
Симметричная матрица

Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

Формат входных данных
На вход программе подаётся натуральное число nnn — количество строк и столбцов в матрице, затем элементы матрицы
построчно через пробел.

Формат выходных данных
Программа должна вывести YES, если матрица симметрична относительно главной диагонали, и слово NO в противном случае.
Тестовые данные 🟢

Sample Input 1:

3
0 1 2
1 2 3
2 3 4

Sample Output 1:

YES
"""


def is_symmetry(size):
    matrix = []
    for row in range(size):
        nums = [int(num) for num in input().split()]
        matrix.append(nums)
    s_matrix = []
    for c in range(size):
        flip_nums = []
        for r in range(size):
            flip_nums.append(matrix[r][c])
        s_matrix.append(flip_nums)
    if matrix == s_matrix:
        print('YES')
    else:
        print('NO')


square_matrix_size = int(input())
is_symmetry(square_matrix_size)

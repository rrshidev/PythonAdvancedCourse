"""
Сложение матриц

Напишите программу для вычисления суммы двух матриц.

Формат входных данных
На вход программе подаются два натуральных числа nnn и mmm — количество строк и столбцов в матрицах, затем элементы
первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
Тестовые данные 🟢

Sample Input 1:

2 4
1 2 3 4
5 6 7 1

3 2 1 2
1 3 1 3

Sample Output 1:

4 4 4 6
6 9 8 4
"""


def sum_the_matrices(matrix_1, matrix_2, n_size, m_size):
    result_matrix = []
    for r in range(n_size):
        row = []
        for c in range(m_size):
            row.append(matrix_1[r][c] + matrix_2[r][c])
        result_matrix.append(row)
    return result_matrix


def main():
    input_sizes = [int(num) for num in input().split()]
    n, m = input_sizes[0], input_sizes[1]

    mat_1 = []
    for r in range(n):
        row = [int(num) for num in input().split()]
        mat_1.append(row)

    empty_str = input()

    mat_2 = []
    for r in range(n):
        row = [int(num) for num in input().split()]
        mat_2.append(row)

    result_matrix = sum_the_matrices(mat_1, mat_2, n, m)
    for r in result_matrix:
        print(*r)


main()

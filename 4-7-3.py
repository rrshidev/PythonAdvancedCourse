"""
Возведение матрицы в степень 🌶️

Напишите программу, которая возводит квадратную матрицу в mmm-ую степень.

Формат входных данных
На вход программе подаётся натуральное число nnn — количество строк и столбцов в матрице, затем элементы матрицы,
затем натуральное число mmm.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
Тестовые данные 🟢

Sample Input 1:

3
1 2 3
4 5 6
7 8 9
2

Sample Output 1:

30 36 42
66 81 96
102 126 150
"""


def exponentiation(matrix_1, n_size, iter):

    matrix_2 = matrix_1

    for _ in range(iter - 1):
        result_matrix = []
        for r in range(n_size):
            row = []
            for c in range(n_size):
                res_num = 0
                for cc in range(n_size):
                    res_num += matrix_1[r][cc] * matrix_2[cc][c]
                    if cc == n_size - 1:
                        row.append(res_num)
            result_matrix.append(row)
        matrix_2 = result_matrix
    return result_matrix


def main():
    mat_1 = []
    n = int(input())
    for r in range(n):
        row = [int(num) for num in input().split()]
        mat_1.append(row)
    i = int(input())
    result_matrix = exponentiation(mat_1, n, i)
    for r in result_matrix:
        print(*r)


main()

"""
Умножение матриц 🌶️

Напишите программу, которая перемножает две матрицы.

Формат входных данных
На вход программе подаются два натуральных числа nnn и mmm — количество строк и столбцов в первой матрице, затем
элементы первой матрицы, затем пустая строка. Далее следуют числа mmm и kkk — количество строк и столбцов второй
матрицы затем элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

Тестовые данные 🟢

Sample Input 1:

2 2
1 2
3 2

2 2
3 2
1 1

Sample Output 1:

5 4
11 8
"""


def multiplication_the_matrices(matrix_1, matrix_2, n_size, m_size):
    result_matrix = []
    if matrix_2 == [[0], [0]]:
        result_matrix.append([0])
    elif n_size == m_size:
        for r in range(n_size):
            row = []
            for c in range(m_size):
                res_num = 0
                for cc in range(n_size):
                    res_num += matrix_1[r][cc] * matrix_2[cc][c]
                    if cc == n_size - 1:
                        row.append(res_num)
            result_matrix.append(row)
    else:
        if n_size > m_size:
            diff = n_size - m_size
        elif n_size < m_size:
            diff = m_size - n_size
        for r in range(n_size + diff):
            row = []
            for c in range(m_size):
                res_num = 0
                for cc in range(n_size):
                    res_num += matrix_1[r][cc] * matrix_2[cc][c]
                    if cc == n_size - 1:
                        row.append(res_num)
            result_matrix.append(row)


    return result_matrix


def main():
    mat_1 = []
    mat_2 = []
    for iteration in range(2):
        input_sizes = [int(num) for num in input().split()]
        n, m = input_sizes[0], input_sizes[1]
        for r in range(n):
            row = [int(num) for num in input().split()]
            if iteration == 0:
                mat_1.append(row)
            else:
                mat_2.append(row)
        if iteration == 0:
            empty_str = input()
        else:
            continue
    result_matrix = multiplication_the_matrices(mat_1, mat_2, n, m)
    for r in result_matrix:
        print(*r)


main()

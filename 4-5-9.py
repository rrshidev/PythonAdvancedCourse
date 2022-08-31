"""
Магический квадрат 🌶️

Магическим квадратом порядка nnn называется квадратная таблица размера n×nn \times nn×n, составленная из всех
чисел 1,2,3,…,n21, 2, 3, \ldots, n^21,2,3,…,n2 так, что суммы по каждому столбцу, каждой строке и каждой из двух
диагоналей равны между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим
квадратом.

Формат входных данных
На вход программе подаётся натуральное число nnn — количество строк и столбцов в матрице, затем элементы матрицы:
nnn строк, по nnn чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.
Тестовые данные

Sample Input 1:

3
8 1 6
3 5 7
4 9 2

Sample Output 1:

YES

Sample Input 2:

3
8 2 6
3 5 7
4 9 1

Sample Output 2:

NO
"""


def sum_checker(magic_matrix):
    reference = sum(magic_matrix[0])
    main_sum = 0
    secondary_sum = 0
    test_nums = [num for num in range(1, (len(magic_matrix)**2)+1)]
    for i in range(len(magic_matrix)):
        sum_check = 0
        for j in range(len(magic_matrix)):
            if magic_matrix[i][j] in test_nums:
                test_nums.remove(magic_matrix[i][j])
            else:
                return print('NO')
            sum_check += magic_matrix[i][j]
            if i == j:
                main_sum += magic_matrix[i][j]
            if i + j + 1 == len(magic_matrix):
                secondary_sum += magic_matrix[i][j]
        if sum_check == reference:
            continue
        elif main_sum == reference:
            continue
        elif secondary_sum == reference:
            continue
        else:
            return print('NO')
    for j in range(len(magic_matrix)):
        trance_sum_check = 0
        for i in range(len(magic_matrix)):
            trance_sum_check += magic_matrix[i][j]
        if trance_sum_check == reference:
            continue
        else:
            return print('NO')

    return print('YES')


def input_matrix():
    mat_size = int(input())
    matrix = []
    for i in range(mat_size):
        nums = [int(num) for num in input().split()]
        matrix.append(nums)
    return sum_checker(matrix)


input_matrix()

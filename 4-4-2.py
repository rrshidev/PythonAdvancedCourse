"""
Вывести матрицу 2

На вход программе подаются два натуральных числа nnn и mmm, каждое на отдельной строке — количество строк и столбцов
в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала
первой строки, затем второй, и т.д.

Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы, выводит пустую строку,
и снова ту же матрицу, но уже поменяв местами строки со столбцами: первая строка выводится как первый столбец, и так
далее.

Формат входных данных
На вход программе подаются два числа nnn и mmm — количество строк и столбцов в матрице, далее идут n×mn \times mn×m
слов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести считанную матрицу, за ней пустую строку, и ту же матрицу, но поменяв местами строки со
столбцами. Элементы матрицы разделять одним пробелом.
Тестовые данные 🟢

Sample Input 1:

4
2
и
швец
и
жнец
и
на
дуде
игрец

Sample Output 1:

и швец
и жнец
и на
дуде игрец

и и и дуде
швец жнец на игрец

Sample Input 2:

2
3
не
в
бровь
а
в
глаз

Sample Output 2:

не в бровь
а в глаз

не а
в в
бровь глаз
"""


def print_matrix(row_cnt, col_cnt):
    matrix = []
    for r in range(row_cnt):
        nums = []
        for c in range(col_cnt):
            str_in = input().split()
            nums.append(str_in)
        matrix.append(nums)
    for r in range(row_cnt):
        for c in range(col_cnt):
            print(str(*matrix[r][c]), end=' ')
        print()
    print()
    for c in range(col_cnt):
        for r in range(row_cnt):
            print(str(*matrix[r][c]), end=' ')
        print()


n, m = int(input()), int(input())
print_matrix(n, m)
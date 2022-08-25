'''
Обмен диагоналей

Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и побочной диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами элемент на главной диагонали и на побочной диагонали).

Формат входных данных
На вход программе подаётся натуральное число nnn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести матрицу с элементами главной и побочной диагонали, поменявшимися своими местами.
Тестовые данные 🟢

Sample Input 1:

3
1 2 3
4 5 6
7 8 9

Sample Output 1:

7 2 9
4 5 6
1 8 3
'''

def matrix_diagonal(S_M_S):
    matrix = []
    for row in range(S_M_S):
        temp = [int(elem) for elem in input().split()]
        matrix.append(temp)
    t_matrix = []
    for c in range(S_M_S):
        tmp = []
        for r in range(S_M_S):
            tmp.append(matrix[r][c])
        t_matrix.append(tmp)
    for i in range(S_M_S):
        t_matrix[i][S_M_S - i - 1], t_matrix[i][i] = t_matrix[i][i], t_matrix[i][S_M_S-i-1]
    for c in range(S_M_S):
        tmp = []
        for r in range(S_M_S):
            tmp.append(t_matrix[r][c])
        print(*tmp)


square_matrix_size = int(input()) #shortly name of it value - SMS =)
matrix_diagonal(square_matrix_size)
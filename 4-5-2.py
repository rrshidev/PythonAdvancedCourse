'''
Максимум в таблице

На вход программе подаются два натуральных числа nnn и mmm — количество строк и столбцов в матрице, затем nnn строк по mmm целых чисел в каждой, отделенных символом пробела.

Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального элемента.

Формат входных данных
На вход программе на разных строках подаются два числа nnn и mmm — количество строк и столбцов в матрице, затем сами элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести два числа: номер строки и номер столбца, в которых стоит наибольший элемент таблицы. Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.

Примечание. Считайте, что нумерация строк и столбцов начинается с нуля.
Тестовые данные 🟢

Sample Input 1:

3
4
0 3 2 4
2 3 5 5
5 1 2 3

Sample Output 1:

1 2
'''


def maxiMatrix(amount_rows, amount_cols):
    matrix = []
    for row in range(amount_rows):
        tmp = [int(element) for element in input().split()]
        matrix.append(tmp)

    temp_maximums = []
    for row in matrix:
        temp_maximums.append(max(row))

    for r in range(amount_rows):
        for c in range(amount_cols):
            if matrix[r][c] == max(temp_maximums):
                temp = []
                temp.append(r)
                temp.append(c)
                return temp



size_n, size_m = int(input()), int(input())
print(*maxiMatrix(size_n, size_m))

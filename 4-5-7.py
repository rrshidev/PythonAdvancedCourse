'''
Поворот матрицы

Напишите программу, которая поворачивает квадратную матрицу чисел на 90∘90^{\circ}90∘ по часовой стрелке.

Формат входных данных
На вход программе подаётся натуральное число nnn — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести результат на экран, числа должны быть разделены одним пробелом.
Тестовые данные 🟢

Sample Input 1:

3
1 2 3
4 5 6
7 8 9

Sample Output 1:

7 4 1
8 5 2
9 6 3
'''

def turn(n):
    matrix = []
    for row in range(n):
        temp = [int(element) for element in input().split()]
        matrix.append(temp)
    for c in range(n):
        tmp = []
        for r in range(n - 1, -1, -1):
            tmp.append(matrix[r][c])
        print(*tmp)


matrix_size = int(input())
turn(matrix_size)

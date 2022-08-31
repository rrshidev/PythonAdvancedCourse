"""
Шахматная доска

На вход программе подаются два натуральных числа nnn и mmm. Напишите программу для создания матрицы размером n×mn \times mn×m, заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка. Выведите полученную матрицу на экран, разделяя элементы пробелами.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nnn и mmm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу, описанную в условии задачи.
Тестовые данные 🟢

Sample Input 1:

3 4

Sample Output 1:

. * . *
* . * .
. * . *
"""


def create_matrix(n_size, m_size):
    matrix = []
    for i in range(n_size):
        star_point = []
        for j in range(m_size):
            if i % 2 == 0 and j % 2 == 0:
                star_point.append('.')
            elif i % 2 == 0 and j % 2 != 0:
                star_point.append('*')
            elif i % 2 != 0 and j % 2 != 0:
                star_point.append('.')
            else:
                star_point.append('*')
        matrix.append(star_point)

    return matrix


def main():
    sizes = [int(num) for num in input().split()]
    matrix = create_matrix(sizes[0], sizes[1])

    for row in matrix:
        for num in row:
            print(str(num).ljust(3), end='')
        print()


main()

"""
  Заполнение 2

На вход программе подаются два натуральных числа nnn и mmm. Напишите программу, которая создает матрицу размером n×mn \times mn×m заполнив её в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nnn и mmm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 333 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇
Тестовые данные 🟢

Sample Input 1:

3 7

Sample Output 1:

1  4  7  10 13 16 19
2  5  8  11 14 17 20
3  6  9  12 15 18 21
"""


def fill_matrix(n, m):
    matrix = []
    for r in range(n):
        limit_cnt = 1 + r
        nums = []
        for c in range(m):
            nums.append(limit_cnt)
            limit_cnt += n
        matrix.append(nums)

    return matrix


def main():
    size_of_matrix = [int(num) for num in input().split()]
    n_size = size_of_matrix[0]
    m_size = size_of_matrix[1]
    matrix = fill_matrix(n_size, m_size)

    for row in matrix:
        for num in row:
            print(str(num).ljust(3), end='')
        print()


main()

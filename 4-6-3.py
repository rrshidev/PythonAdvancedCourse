"""
Заполнение 1

На вход программе подаются два натуральных числа nnn и mmm. Напишите программу, которая создает матрицу размером
n×m и заполняет её числами от 111 до n⋅mn \cdot mn⋅m в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nnn и mmm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 333 символа на каждый элемент.
Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение
Тестовые данные

Sample Input 1:

3 4

Sample Output 1:

1  2  3  4
5  6  7  8
9  10 11 12
"""


def fill_matrix(n, m):
    matrix = []
    limit_cnt = 1
    for r in range(n):
        nums = []
        for c in range(m):
            nums.append(limit_cnt)
            limit_cnt += 1
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

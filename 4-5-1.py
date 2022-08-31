"""
Таблица умножения

На вход программе подаются два натуральных числа nnn и mmm — количество строк и столбцов в матрице. Создайте матрицу 
mult размером n×mn \times mn×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.

Формат входных данных
На вход программе на разных строках подаются два числа nnn и mmm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 333 символа (для этого используйте 
строковый метод ljust()).
Тестовые данные 🟢

Sample Input 1:

4
6

Sample Output 1:

0  0  0  0  0  0
0  1  2  3  4  5
0  2  4  6  8  10
0  3  6  9  12 15
"""


def multi_matrix(amount_rows, amount_cols):
    matrix_mul = []
    for r in range(amount_rows):
        res = []
        for c in range(amount_cols):
            res.append(r * c)
        matrix_mul.append(res)
    for string in range(amount_rows):
        print(*matrix_mul[string])


size_n, size_m = int(input()), int(input())
multi_matrix(size_n, size_m)

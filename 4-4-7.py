"""
Суммы четвертей

Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю,
левую и правую.

Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой
четверти.

Формат входных данных
На вход программе подаётся натуральное число nnn — количество строк и столбцов в матрице, затем элементы матрицы
(целые числа) построчно через пробел.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Элементы диагоналей не учитываются.
Тестовые данные 🟢

Sample Input 1:

4
1 2 3 4
5 6 7 8
3 4 5 6
1 2 3 4

Sample Output 1:

Верхняя четверть: 5
Правая четверть: 14
Нижняя четверть: 5
Левая четверть: 8
"""


def sum_of_area(m_size):
    matrix = []
    sum_up, sum_right, sum_down, sum_left = 0, 0, 0, 0
    for r_number in range(m_size):
        nums = [int(num) for num in input().split()]
        matrix.append(nums)
    for r_number in range(m_size):
        for c_number in range(m_size):
            if (r_number < c_number) and (r_number < m_size - 1 - c_number):
                sum_up += matrix[r_number][c_number]
            elif (r_number < c_number) and (r_number > m_size - 1 - c_number):
                sum_right += matrix[r_number][c_number]
            elif (r_number > c_number) and (r_number > m_size - 1 - c_number):
                sum_down += matrix[r_number][c_number]
            elif (r_number > c_number) and (r_number < m_size - 1 - c_number):
                sum_left += matrix[r_number][c_number]
    print('Верхняя четверть:', sum_up)
    print('Правая четверть:', sum_right)
    print('Нижняя четверть:', sum_down)
    print('Левая четверть:', sum_left)


matrix_size = int(input())
sum_of_area(matrix_size)

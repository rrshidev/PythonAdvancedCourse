"""
Произведение чисел

Напишите программу для определения, является ли число произведением двух чисел из данного набора, выводящую результат
в виде ответа «ДА» или «НЕТ».

Формат входных данных
В первой строке подаётся число n (0 < n < 1000) – количество чисел в наборе. В последующих
n строках вводятся целые числа, составляющие набор (могут повторяться). Затем следует целое число, которое является
или не является произведением двух каких-то чисел из набора.

Формат выходных данных
Программа должна вывести «ДА» или «НЕТ» в соответствии с условием задачи.

Примечание 1. Само на себя число из набора умножиться не может, другими словами, два множителя должны иметь разные
индексы в наборе.

Примечание 2. Для решения задачи используйте вложенные циклы.
"""


def multi_check(nums, product):
    for i in range(len(nums)):
        multiplicand = nums[i]
        for j in range(i + 1, n):
            multiplier = nums[j]
            if multiplicand * multiplier == product:
                return 'ДА'
    return 'НЕТ'


n = int(input())
input_nums = [int(input()) for _ in range(n)]
input_product = int(input())
print(multi_check(input_nums, input_product))

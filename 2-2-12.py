"""
Предикат делимости
Напишите функцию func(num1, num2), принимающую в качестве аргументов два натуральных числа num1 и num2 и возвращающую
значение True если число num1 делится без остатка на число num2 и False в противном случае.
Результатом вывода программы должно быть "делится" (если функция func() вернула True) и "не делится" (если функция
func() вернула False).
"""


# The names of these variables and function are dictated by the conditions of the task.
def func(n1, n2):
    return n1 % n2 == 0


num1, num2 = int(input()), int(input())
if func(num1, num2):
    print('делится')
else:
    print('не делится')

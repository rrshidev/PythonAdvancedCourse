"""
На вход программе подается строка текста, содержащая натуральные числа, расположенные по неубыванию. Из строки формируется список чисел. Напишите программу для подсчета количества разных элементов в списке.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела, расположенные по неубыванию.

Формат выходных данных
Программа должна вывести одно число – количество различных элементов списка.

Примечание. Задачу можно решить без множеств.
"""


tim_choice, rus_choice = input(), input()
stone, scissors, paper, lizard, spock = 'камень', 'ножницы', 'бумага', 'ящерица', 'Спок'

if (tim_choice == paper and rus_choice == stone) or \
        (tim_choice == paper and rus_choice == spock) or \
        (tim_choice == stone and rus_choice == scissors) or \
        (tim_choice == scissors and rus_choice == paper) or \
        (tim_choice == stone and rus_choice == lizard) or \
        (tim_choice == scissors and rus_choice == lizard) or \
        (tim_choice == spock and rus_choice == scissors) or \
        (tim_choice == spock and rus_choice == stone) or \
        (tim_choice == lizard and rus_choice == spock) or \
        (tim_choice == lizard and rus_choice == paper):
    print('Тимур')
elif tim_choice == rus_choice:
    print('ничья')
else:
    print('Руслан')

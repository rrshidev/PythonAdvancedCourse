'''
На вход программе подается строка текста, содержащая натуральные числа, расположенные по неубыванию. Из строки формируется список чисел. Напишите программу для подсчета количества разных элементов в списке.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела, расположенные по неубыванию.

Формат выходных данных
Программа должна вывести одно число – количество различных элементов списка.

Примечание. Задачу можно решить без множеств.
'''

Tim, Rus = input(), input()
stone, scissors, paper, lizard, spock = 'камень', 'ножницы', 'бумага', 'ящерица', 'Спок'

if (Tim == paper and Rus == stone) or \
        (Tim == paper and Rus == spock) or\
        (Tim == stone and Rus == scissors) or \
        (Tim == scissors and Rus == paper) or \
        (Tim == stone and Rus == lizard) or \
        (Tim == scissors and Rus == lizard) or \
        (Tim == spock and Rus == scissors) or \
        (Tim == spock and Rus == stone) or \
        (Tim == lizard and Rus == spock) or \
        (Tim == lizard and Rus == paper):
    print('Тимур')
elif Tim == Rus:
    print('ничья')
else:
    print('Руслан')
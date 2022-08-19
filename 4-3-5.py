'''
На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.

Формат выходных данных
Программа должна вывести указанный вложенный список

Sample Input 1:

a b c d

Sample Output 1:

[['a'], ['b'], ['c'], ['d']]

Sample Input 2:

w w w o r l d g g g g r e a t t e c c h e m g g p w w

Sample Output 2:

[['w', 'w', 'w'], ['o'], ['r'], ['l'], ['d'], ['g', 'g', 'g', 'g'], ['r'], ['e'], ['a'], ['t', 't'], ['e'], ['c', 'c'], ['h'], ['e'], ['m'], ['g', 'g'], ['p'], ['w', 'w']]
'''

def groupizm(s):
    in_list = []
    tmp = []
    res = []
    for char in s:
        in_list.append(list(char))
    in_list.append([])
    for i in range(1, len(in_list)):
        if in_list[i-1] == in_list[i]:
            tmp += in_list[i-1]
        elif in_list[i-1] != in_list[i] and tmp != []:
            tmp += in_list[i-1]
            res.append(tmp)
            tmp = []
        elif in_list[i-1] != in_list[i] and in_list.index(in_list[i]) != -1:
            res.append(in_list[i-1])
    return res

in_str = input().split(' ')
print(groupizm(in_str))
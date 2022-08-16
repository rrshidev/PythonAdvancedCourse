'''
На вход программе подаются две строки, на одной символы, на другой число nnn. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков указанной длины.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число nnn на отдельной строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Примечание. Не забудьте вызвать функцию chunked(), чтобы вывести результат 😀.
Тестовые данные 🟢

Sample Input 1:

a b c d e f
2

Sample Output 1:

[['a', 'b'], ['c', 'd'], ['e', 'f']]
'''


def chunked(s, n):
    s_list, res_list, tmp_list = [], [], []
    cnt = 0

    for i in s:
        s_list.append(list(i))

    if n == 1:
        return s_list

    s_list.append([])

    for i in s_list:
        tmp_list += i
        cnt += 1
        if cnt == n:
            res_list.append(tmp_list)
            tmp_list = []
            cnt = 0
    return res_list


in_str = input().split(' ')
n_group = int(input())

print(chunked(in_str, n_group))
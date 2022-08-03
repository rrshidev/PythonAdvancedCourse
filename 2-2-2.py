'''
Формат входных данных
На вход программе подается строка текста из разделенных пробелами натуральных чисел.

Формат выходных данных
Программа должна вывести одно число – количество элементов списка, больших предыдущего.
'''
nums = input().split(' ')
listOfNums = []
cnt = 0
moreThanThePrevious = 0
for i in nums:
    listOfNums.append(int(i))
for i in listOfNums:
    if i > moreThanThePrevious:
        moreThanThePrevious = i
        cnt += 1
print(cnt - 1)
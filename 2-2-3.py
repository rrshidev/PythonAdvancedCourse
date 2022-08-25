'''
На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.).
Если в списке нечетное количество элементов, то последний остается на своем месте.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.

Формат выходных данных
Программа должна вывести измененный список, разделяя его элементы одним пробелом.

'''


inputString = input().split(' ')
nums, outputList, outputList_, resultList = [], [], [], []

for i in inputString:
    nums.append(i)
for i in range(1, len(nums), 2):
    outputList.append(nums[i])
for i in range(0, len(inputString), 2):
    outputList_.append(nums[i])
for i in range(0, len(outputList)):
    resultList.append(int(outputList[i]))
    resultList.append(int(outputList_[i]))

if len(nums) % 2 != 0:
    resultList.append(int(nums[-1]))

print(*resultList)

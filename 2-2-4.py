stringInput = input().split(' ')
unicum = set(stringInput)

resultList = []
for i in unicum:
    resultList.append(i)

print(len(resultList))

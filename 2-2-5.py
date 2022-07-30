stringInput = input().split(' ')
resultList, resultList_ = [], []
for i in stringInput:
    resultList.append(i)
for i in range(1):
        resultList.insert(0, resultList.pop())
print(*resultList)
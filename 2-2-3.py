inputString = input().split(' ')
inputList, outputList, outputList_, resultList = [], [], [], []

for i in inputString:
    inputList.append(i)
for i in range(1, len(inputList), 2):
    outputList.append(inputList[i])
for i in range(0, len(inputString), 2):
    outputList_.append(inputList[i])
for i in range(0, len(outputList)):
    resultList.append(int(outputList[i]))
    resultList.append(int(outputList_[i]))

if len(inputList) % 2 != 0:
    resultList.append(int(inputList[-1]))

print(*resultList)

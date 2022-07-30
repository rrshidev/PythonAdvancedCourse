n = int(input())
stringInputList = [input() for i in range(0, n)]
mul = int(input())

def multiChek():
    result = 'НЕТ'
    for i in range(n):
        x = int(stringInputList[i])
        for j in range(n):
            y = int(stringInputList[j])
            if i != j:
                if x * y == mul:
                    result = 'ДА'
                    return result
    return result

print(multiChek())

'''
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.

Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

Формат входных данных
В первой строке подаётся число nnn – количество холодильников. В последующих nnn строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 555 до 100100100 символов.

Формат выходных данных
Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.
'''

#MAIN FUNCTION
def whereIsAnton(testString):
    standardString = 'anton'
    resultString = ''
    numberOfString = 0
    listOfNumberString = []
    numberSymbol = []
    testSortIndex = numberSymbol.sort()

    if testString.count('n') != 0:

        for symbol in testString:
            if symbol in standardString and symbol not in resultString:
                resultString += symbol
                numberSymbol.append(testString.index(symbol))
                #print(numberSymbol)
    #print(resultString)
    if standardString == resultString + 'n' or standardString == testString and numberSymbol == testSortIndex:
        numberOfString += 1
        listOfNumberString.append(numberOfString)
        resultString = ''
        numberSymbol = []
    else:
        numberOfString += 1
        resultString = ''
        numberSymbol = []
    return listOfNumberString



#INPUT
n = int(input())
l=[]
l.append(listOfNumber)

for i in range(n):
    testString = input()
    whereIsAnton(testString)

print(*listOfNumberString)
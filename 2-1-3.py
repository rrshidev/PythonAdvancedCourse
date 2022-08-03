'''Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ (в том числе пробел) стоит 606060 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести стоимость строки.'''

inputString = input()
priceStringOfKopecks = len(inputString) * 60
priceStringOfRubles = float(priceStringOfKopecks / 100)
resultPriceOfString = str(priceStringOfRubles)
resultPriceOfString.replace('.', ' р. ')
if resultPriceOfString[-1] != 0:
    resultPriceOfString += ' коп.'
else:
    resultPriceOfString += '0 коп.'

print(resultPriceOfString)
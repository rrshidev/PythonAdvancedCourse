'''Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ (в том числе пробел) стоит 606060 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести стоимость строки.'''

inputString = input()
price_kopecks = len(inputString) * 60
price_rubles = float(price_kopecks / 100)
result_price = str(price_rubles)
result_price.replace('.', ' р. ')
if result_price[-1] != 0:
    result_price += ' коп.'
else:
    result_price += '0 коп.'

print(result_price)
"""
Формат входных данных
В первой строке записано количество точек. Каждая следующая строка состоит из двух целых чисел — координат точки
(сначала абсцисса – xxx, затем ордината – yyy), разделенных символом пробела.

Формат выходных данных
Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.

Примечание. Учтите, что точки, лежащие на осях координат, не принято относить к какой-либо координатной четверти.
"""


num_point = int(input())
cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
for i in range(0, num_point):
    coord = input().split(' ')
    x, y = int(coord[0]), int(coord[1])
    if x > 0 and y > 0:
        cnt1 += 1
    elif x < 0 < y:
        cnt2 += 1
    elif x < 0 and y < 0:
        cnt3 += 1
    elif y < 0 < x:
        cnt4 += 1
    else:
        continue

print('Первая четверть: ', cnt1)
print('Вторая четверть: ', cnt2)
print('Третья четверть: ', cnt3)
print('Четвертая четверть: ', cnt4)

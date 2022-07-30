numPoint = int(input())
l = []
cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
for i in range(0, numPoint):
    decard = input().split(' ')
    x, y = int(decard[0]), int(decard[1])
    if x > 0 and y > 0:
        cnt1 += 1
    elif x < 0 and y > 0:
        cnt2 += 1
    elif x < 0 and y < 0:
        cnt3 += 1
    elif x > 0 and y < 0:
        cnt4 += 1
    else:
        continue

print('Первая четверть: ', cnt1)
print('Вторая четверть: ', cnt2)
print('Третья четверть: ', cnt3)
print('Четвертая четверть: ', cnt4)
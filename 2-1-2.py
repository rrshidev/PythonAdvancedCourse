weight = float(input())
growth = float(input())

BMI = weight / (growth ** 2)

if 18.5 <= BMI <= 25:
    print('Оптимальная масса')
elif BMI < 18.5:
    print('Недостаточная масса')
elif BMI > 25:
    print('Избыточная масса')
# у тебя есть число и если это число делиться на 3 то нужно вывести Fiz, если делить на 5, то Baz, а если и на 3 и на 5 то FizBaz
# 1: ..
# 2: ..
# 3: Fiz
# 4: ..
# 5: Baz
# ..
# 15: FizBaz

def fiz_baz(n):
    if n % 3 == 0:


print('Fiz')
elif n % 5 == 0:
print('Baz')
elif n % 5 == 0 and n % 3 == 0:
print('FizBaz')
else:
print(n)

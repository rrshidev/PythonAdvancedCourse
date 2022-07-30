nums = input().split(' ')
l = []
cnt = 0
comp = 0
for i in nums:
    l.append(int(i))
for i in l:
    if i > comp:
        comp = i
        cnt += 1
print(cnt - 1)
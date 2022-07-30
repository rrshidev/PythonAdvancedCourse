n, k = int(input()), int(input())
cnt = 0

for i in range(1, n+1):
    cnt = (cnt + k) % i
print(cnt + 1)

'''
for i in range(1, n + 1):
    l.append(i)

def shiftDelIns(l, k):
    while len(l) != 1:
        for i in range(n-k):

            l.insert(0, l.pop())
            l.pop()
            #l.append('*')
    print(l)

shiftDelIns(l, k)
'''


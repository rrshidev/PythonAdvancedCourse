numbers = int(input())
s_num = str(numbers)
if len(s_num) == 5:
    s_num = s_num[-1::-1]
    for i in s_num:
        if i != '0':
            print(s_num)
            break
        else:
            s_num = s_num[1:]
elif len(s_num) == 6:
    s_num = s_num[0] + s_num[-1:0:-1]
    for i in s_num:
        if i != '0':
            print(s_num)
            break
        else:
            s_num = s_num[1:]
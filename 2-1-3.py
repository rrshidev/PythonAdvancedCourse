s = input()
sum_k = len(s) * 60
sum_r = float(sum_k / 100)
sum_str = str(sum_r)
sum_str_result = sum_str
sum_str_result = sum_str_result.replace('.', ' р. ')
if sum_str_result[-1] !=0:
    sum_str_result + = ' коп.'
else:
    sum_str_result + = '0 коп.'

print(sum_str_result)
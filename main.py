# Quality-Adjusted Life-Year

userData = int(input())
sum = 0.0

for i in range(0, userData):
    # we can not use the i in userData
    # it will report error:TypeError:
    # 'int' object is not iterable

    Qdata = float(input())
    Year = float(input())
    result = Qdata * Year
    sum += result

print(format(sum,'.3f'))
print('%.3f'%sum)

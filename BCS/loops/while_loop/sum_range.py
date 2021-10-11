num = int(input('Enter the range.\n'))

res = 0
i = 0

while i <= num :
    res += i
    i += 1

print('Sum of numbers till {} is {}.' .format(num, res))
num = int(input('Enter the number.\n'))

res = 0

for i in str(num) :
    res += int(i)

print('Sum of digits in {} is {}.' .format(num, res))
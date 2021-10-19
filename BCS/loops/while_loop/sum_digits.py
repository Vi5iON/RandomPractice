num = int(input('Enter the number.\n'))

test_num = num
res = 0

while test_num >=  0 :
    res += test_num % 10
    test_num = test_num//10

print('Sum of digits in {} is {}.' .format(num, res))
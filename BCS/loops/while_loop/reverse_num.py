num = int(input('Enter the number.\n'))

res = 0
test_num = num

while test_num != 0 :
    e_num = test_num % 10
    res = res*10 + e_num
    test_num = test_num//10

print('Pallendrome of {} is {}.' .format(num, res))
num = int(input('Enter the number.\n'))

count = 0
test_num = num

while test_num :
    test_num //= 10
    count += 1

test_num = num
res = 0

while test_num :
    res += (test_num%10)**count
    test_num //= 10

if num == res :
    print(num, 'is amstrong number.')
else :
    print(num, 'isn\'t amstrong number.')
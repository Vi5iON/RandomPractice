num = int(input('Enter the number.\n'))

test_num = num
res = 0

while test_num :
    mod_num = test_num % 10
    fact = 1
    
    for i in range(1, mod_num+1) :
        fact *= i
    
    res += fact
    test_num //= 10

if num == res :
    print(num, 'is a strong number.')
else :
    print(num, 'isn\'t a strong number.')
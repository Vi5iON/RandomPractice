#not a good method as there is a redundent variable i which isn't used.

num = int(input('Enter the number.\n'))

res = 0
test_num = num

for i in str(test_num) :
    e_num = test_num % 10
    res = res*10 + e_num
    test_num = test_num//10

if num == res :
    print(num, 'is a pallendrome.')
else :
    print(num, 'isn\'t a pallendrome.')

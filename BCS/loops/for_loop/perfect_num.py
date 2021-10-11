num = int(input('Enter a number.\n'))

res = 0

#finding factors and suming them

for i in range(1, num) :
    if num % i == 0 :
        res += i

#checking for perfect number or not

if res == num :
    print(num, 'is a perfect number.\n')
else :
    print(num, 'isn\'t a perfect number.\n')
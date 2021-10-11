num = int(input('Enter the number.\n'))

i = 1
res = 0

while i < num :
    if num % i == 0 :
        res += i
    i += 1

if res == num :
    print(num,'is a perfect number.')
else :
    print(num,'isn\'t a perfect number.')
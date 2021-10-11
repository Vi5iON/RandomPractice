num = int(input('Enter the number.\n'))

i = 1
count = 0

while i <= num :
    if num % i == 0 :
        count += 1
    i += 1

if count == 2 :
    print(num,'is prime.')
else :
    print(num,'isn\'t prime.')
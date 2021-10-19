num = int(input('Enter the number.\n'))

count = 0

for i in range(2, int(num ** 0.5)) :
    if num % i == 0 :
        count += 1
        break

if count == 0 :
    print(num, 'is prime.')
else :
    print(num, 'isn\'t prime.')
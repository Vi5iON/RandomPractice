num = int(input('Enter the number.\n'))

i = 1
res = 0

while i <= num :
    if num % i == 0 :
        res += i
    i += 1

print('Sum of factors of {} is {}.' .format(num, res))
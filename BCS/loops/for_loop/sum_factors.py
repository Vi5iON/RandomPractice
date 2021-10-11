num = int(input('Enter the number.\n'))

sum = 0

#finding factors of a 'num' and adding them

for i in range(1, num+1) :
    if num % i == 0 :
        sum += i

print('\nSum of factors of {} is {}' .format(num, sum))
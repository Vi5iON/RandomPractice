num = int(input('Enter the number.\n'))

i = 1
fact = 1

while i <= num :
    fact *= i
    i += 1

print('Factorial of {} is {}.' .format(num, fact))
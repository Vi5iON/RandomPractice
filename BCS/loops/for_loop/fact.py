num = int(input('Enter the number.\n'))

#number multiplied by 1 is the number itself also factorial of zero is 1

fact = 1

#finding factorial of 'num' and printing it

for i in range(1, num+1) :
    fact *= i

print('\nFactorial of {} is {}' .format(num, fact))
# find greatest of three numbers
# use of place holder is shown here by using .format()

num1 = int(input('Enter number1.\n'))
num2 = int(input('Enter number2.\n'))
num3 = int(input('Enter number3.\n'))

if num1 > num2 and num1 > num3 :
    print('{} greater than {} and {}.' .format(num1, num2, num3))
elif num2 > num3 :
    print('{} greater than {} and {}.' .format(num2, num1, num3))
else :
    print('{} greater than {} and {}.' .format(num3, num1, num2))
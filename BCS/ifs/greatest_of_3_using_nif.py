# find greatest of three numbers

num1 = int(input('Enter number1.\n'))
num2 = int(input('Enter number2.\n'))
num3 = int(input('Enter number3.\n'))

if num1 < num2 or num1 < num3 :
    if num2 > num3 :
        print(num2, 'is greatest.\n')
    else :
        print(num3, 'is greatest.\n')
else :
    print(num1, 'is greatest.\n')
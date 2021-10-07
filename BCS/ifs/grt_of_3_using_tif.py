# find greatest of three using ternary if

num1 = int(input('Enter number1.\n'))
num2 = int(input('Enter number2.\n'))
num3 = int(input('Enter number3.\n'))

# des are wrong as ternary if shouldnt end with if but with else
#print(num1,'is greater.\n') if num1 > num2 and num1 > num3 else print(num2, 'is greater.\n') if num2 > num1 and num2 > num3 else print(num3, 'is greater.\n') if num3 > num1 and num3 > num2
#res = str(num1)+' is greater.\n' if num1 > num2 and num1 > num3 else str(num2)+' is greater.\n' if num2 > num1 and num2 > num3 else str(num3)+' is greater.\n'
#print(res)

print(str(num1)+' is greater.\n' if num1 > num2 and num1 > num3 else str(num2)+' is greater.\n' if num2 > num1 and num2 > num3 else str(num3)+' is greater.\n')

# below stament would be considered wrong as print will concatinate num1, num2, num3
#print(num1,' is greater.\n' if num1 > num2 and num1 > num3 else num2,' is greater.\n' if num2 > num1 and num2 > num3 else num3,' is greater.\n')

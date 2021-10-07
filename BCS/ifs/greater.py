# find the greatest

num1 = int(input('Enter first number\n'))
num2 = int(input('Enter second number\n'))

if num1 < num2 :
    print(num2,'is greater than',num1)
elif num2 < num1:
    print(num1,'is greater than',num2)
else :
    print('Both are equal.')
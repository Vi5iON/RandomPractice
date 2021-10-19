num = int(input('Enter the number.\n'))

# find square of number.

square_num = num**2
res = 0

#sum of digits of square of number

while square_num :
    res += square_num % 10
    square_num //= 10

#comparing if neon or not

if num == res :
    print(num, 'is neon number.')
else :
    print(num, 'isn\'t neon number.')
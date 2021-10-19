num = int(input('Enter the number.\n'))

square_num = num * num
temp_num = num
flag = True

#pulling last digit and checking.
#while condition is temp_num as we need to compare for length of num only.

while temp_num :
    if temp_num % 10 != square_num % 10 :
        flag = False
        break
    
    temp_num //= 10
    square_num //= 10

if flag :
    print(num, 'is a automorphic number.')
else :
    print(num, 'isn\'t a automorphic number.')
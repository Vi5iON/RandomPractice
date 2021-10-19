#very lengthy codes try not to write such codes!!!!!!!!!!!!!
#find the shortest logic to achive the result.

num = int(input('Enter the number.\n'))

square_num = num ** 2
temp_num = num
count = 0

while temp_num :
    temp_num //= 10
    count += 1

temp_num = num
new_num = 0

while count :
    new_num = (new_num * 10) + (temp_num % 10)
    temp_num //= 10
    count -= 1

temp_num = 0

while new_num :
    temp_num = (temp_num * 10) + (new_num % 10)
    new_num //= 10

if num == temp_num :
    print(num, 'is automorphic.')
else :
    print(num, 'isn\'t automorphic.')
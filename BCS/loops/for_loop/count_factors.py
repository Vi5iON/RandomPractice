num = int(input('Enter a number.\n'))

count = 0

#finding number of factors for given number

for i in range(1, num+1) :
    if num % i == 0 :
        count += 1
    
print('\n{} has {} factors.' .format(num, count))
num = int(input('Enter the number.\n'))

i = 1

print('Factors of', num,'are :')
while i <= num :
    if num % i == 0 :
        print(i,'', end="")
    i += 1
num = int(input('Enter the number.\n'))

print('\nFactors of',num,'are :')

#finding factors of a 'num' and printing them

for i in range(1, num+1) :
    if num % i == 0 :
        print(str(i)+' ', end="")

print()
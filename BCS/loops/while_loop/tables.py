num1 = int(input('Enter the number.\n'))
end_multiplier = int(input('Enter the end multiplier.\n'))

i = 0

while i <= end_multiplier :
    print('{} * {}  = {}' .format(num1, i, num1*i))
    i += 1
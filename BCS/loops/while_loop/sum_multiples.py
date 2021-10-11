num1 = int(input('Enter the number.\n'))
end_multiplier = int(input('Enter the end multiplier.\n'))

i = 0
res = 0

while i <= end_multiplier :
    res += i*num1
    i += 1

print('Sum of multiples of {} from 1 to {} is {}.' .format(num1, end_multiplier, res))
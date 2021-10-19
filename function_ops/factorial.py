print('Start\n')

def fact() :
    num = int(input('Enter a number.\n'))
    
    temp = num
    res = 1

    while temp :
        res *= temp
        temp -= 1

    print(f'Factorial of {num} is {res}')

fact()

print('\nEnded')
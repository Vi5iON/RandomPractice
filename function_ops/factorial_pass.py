print('Start\n')

def fact(num) :
    
    temp = num
    res = 1

    while temp :
        res *= temp
        temp -= 1

    print(f'Factorial of {num} is {res}')

fact(8)
fact(5)

print('\nEnded')
print('Start\n')

def fact(num) :

    temp = num
    res = 1

    while temp :
        res *= temp
        temp -= 1
    
    return f'Factorial of {num} is {res}.'

print(fact(int(input('Enter the number.\n'))))
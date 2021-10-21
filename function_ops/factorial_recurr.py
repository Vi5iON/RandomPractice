def main() :
    
    num = int(input('Enter a number.\n'))
    print(f'Factorial of {num} is {fact(num)}')


def fact(num) :

    if num :
        return num * fact(num-1)
    return 1


if __name__ == '__main__' :
    main()
# main is the user interface.
#trying to find if it's prime or not
def main() :
    num = int(input('Enter the number.\n'))
    if is_prime(num) :
        print(f'{num} is prime.')
    else :
        print(f'{num} isn\'t prime.')

#is_prime(num) check number for factors returned from count_of_factors(num)

def is_prime(num:int)->bool :
    if count_of_factors(num) :
        return False
    return True

#count_of_factors(num) checks for number for factors running a loop from 2 to root of the number.

def count_of_factors(num:int)->int :
    for i in range(2, sqrt(num)+1) :
        if num % i == 0:
            return 1
    return 0

# squrt(num) provides root of a number.

def sqrt(num:int)->int :
    return int(num ** 0.5) 

if __name__ == '__main__' :
    main()
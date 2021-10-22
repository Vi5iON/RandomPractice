'''
main block that accepts upper and lower limit.
Finds the prime numbers within this range.
'''
def main() :
    lower = int(read('Enter the lower range.\n'))
    upper = int(read('Enter the upper range.\n'))
    print(f'\nPrime numbers within the range ({lower},{upper}) are:')
    for i in range(lower, upper) :
        if is_prime(i) :
            print(f'{i}')


#checks if the given number is prime
def is_prime(num: int)->bool :
    for i in range(2, sqrt(num)+1) :
        if num % i == 0 :
            return False
    return True

#returns square root of given number
def sqrt(num: int)->int:
    return int(num ** 0.5)


#simply read user input
def read(msg: str)->str :
    return input(msg) 


if __name__ == '__main__' :
    main()